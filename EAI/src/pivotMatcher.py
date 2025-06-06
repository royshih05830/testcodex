import cv2
import datetime
import os
import numpy as np
class Matcher:
    def __init__(self) -> None:
        self.pattern = None
        self.pattern_roi = None
        pass
    def __intersect_rectangles(self, rect1, rect2):
        """
        Calculates the intersection area of two ROIs defined by bounding rectangles.
        Args:
            roi1: A tuple (x1, y1, w1, h1) representing ROI 1 (top-left x, top-left y, width, height).
            roi2: A tuple (x2, y2, w2, h2) representing ROI 2 (top-left x, top-left y, width, height).
        Returns:
            A tuple (x_intersect, y_intersect, w_intersect, h_intersect) representing the intersection ROI,
            or None if there is no intersection.
        """
        # Extract coordinates
        x1, y1, w1, h1 = rect1
        x2, y2, w2, h2 = rect2
        # Calculate overlapping ranges
        x_overlap = max(0, min(x1 + w1, x2 + w2) - max(x1, x2))
        y_overlap = max(0, min(y1 + h1, y2 + h2) - max(y1, y2))
        # Check if there is an intersection
        if x_overlap > 0 and y_overlap > 0:
            # Calculate intersection coordinates
            x_intersect = max(x1, x2)
            y_intersect = max(y1, y2)
            w_intersect = x_overlap
            h_intersect = y_overlap
            return (x_intersect, y_intersect, w_intersect, h_intersect)
        else:
            return None
    def __crop_pattern_from_image(self, image, roi):
        image_boundary = (0, 0, image.shape[1], image.shape[0])
        intersect_roi = self.__intersect_rectangles(image_boundary, roi)
        # Extract ROI coordinates
        left, top, width, height = intersect_roi
        x_start = left
        y_start = top
        x_end = left + width - 1
        y_end = top + height - 1
        # Get the ROI as a separate Mat object (might be a view)
        cropped_image = image[y_start:y_end, x_start:x_end]
        return cropped_image, intersect_roi
    def __draw_search_result(self, image, x, y):
        # 畫出最佳匹配區域
        cv2.rectangle(image, (x, y), (x + self.pattern.shape[1], y + self.pattern.shape[0]), (0, 255, 0), 2)
        # 顯示結果
        cv2.imshow('Search Image', image)
        # 等待按鍵
        cv2.waitKey(0)
        cv2.imwrite(f'{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.jpg', image)
    
    def set_pattern(self, image, roi):
        cropped_image, intersect_roi = self.__crop_pattern_from_image(image, roi)
        
        if self.pattern is not None:
            self.pattern.release()
        self.pattern = cropped_image.copy()
        self.pattern_roi = intersect_roi

    def set_pattern_image(self, image):
        self.pattern = image.copy()
    def get_pattern(self):
        return self.pattern, self.pattern_roi

    def is_overlap(self, box1, box2, overlap_threshold, pattern_size):
        x1, y1 = box1
        x2, y2 = box2
        w, h = pattern_size
        x1_min, y1_min = x1, y1
        x1_max, y1_max = x1 + w, y1 + h
        x2_min, y2_min = x2, y2
        x2_max, y2_max = x2 + w, y2 + h

        return not (x1_max - overlap_threshold < x2_min or x1_min > x2_max - overlap_threshold or
                    y1_max - overlap_threshold < y2_min or y1_min > y2_max - overlap_threshold)

    def match(self, image, threshold, search_window=None, method=cv2.TM_CCOEFF_NORMED, display=False, save=False,
              overlap_threshold=0):
        boundary = (0, 0, image.shape[1], image.shape[0])  # (left, top, width, height)
        # Set the search boundary if search_window is given.
        if search_window is not None:
            boundary = search_window

        search_image, search_window = self.__crop_pattern_from_image(image, boundary)
        # Perform pattern matching
        result = cv2.matchTemplate(search_image, self.pattern, method)

        # Apply the threshold to filter the results
        loc = np.where(result >= threshold)
        w, h = self.pattern.shape[:2]

        # Store the found boxes and their corresponding values
        boxes = list(zip(*loc[::-1]))
        values = result[loc]

        # Group overlapping boxes
        groups = []
        while boxes:
            base_box = boxes.pop(0)
            base_value = values[0]
            group = [base_box]
            group_values = [base_value]
            to_remove = []

            for i, other_box in enumerate(boxes):
                if self.is_overlap(base_box, other_box, overlap_threshold, (w, h)):
                    group.append(other_box)
                    group_values.append(values[i])
                    to_remove.append(i)

            # Remove grouped boxes
            for index in sorted(to_remove, reverse=True):
                boxes.pop(index)
                values = np.delete(values, index)

            groups.append((group, group_values))

        # Find the box with the highest value in each group
        filtered_matches = []
        filtered_scores = []
        for group, group_vals in groups:
            max_index = np.argmax(group_vals)
            filtered_matches.append(group[max_index])
            filtered_scores.append(group_vals[max_index])

        # Print the groups
        for i, (group, _) in enumerate(groups):
            print(f"Group {i + 1}: {group}")

        if display:
            # Display the result for debugging purposes
            for pt in filtered_matches:
                cv2.rectangle(image, pt, (pt[0] + self.pattern.shape[1], pt[1] + self.pattern.shape[0]), (0, 255, 0), 2)
            cv2.imshow('Detected', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        if save:
            # Save the cropped image
            for pt in filtered_matches:
                cv2.rectangle(image, pt, (pt[0] + self.pattern.shape[1], pt[1] + self.pattern.shape[0]), (0, 255, 0), 2)
            output_path = "Detected_image.png"  # Change this to your desired path
            cv2.imwrite(output_path, image)
            print(f"Cropped pattern image saved to {output_path}")

        # Return the filtered match locations and the corresponding values
        print(filtered_matches, filtered_scores)
        return filtered_matches, filtered_scores
if __name__ == '__main__':
    # required path
    exec_path = os.path.dirname(__file__)
    image_folder = os.path.join(exec_path, 'images')
    golden_image_path = os.path.join(image_folder, '0.png')
    inspect_image_path = os.path.join(image_folder, 'match_test.png')
    print(f'golden image path = {golden_image_path}')
    print(f'inspect image path = {inspect_image_path}')
    golden_image = cv2.imread(golden_image_path)
    inspect_image = cv2.imread(inspect_image_path)
    pivot = (363, 3187)
    pattern_size = (100, 100)
    #pattern_roi = (pivot[0] - int(pattern_size[0]/2), pivot[1] - int(pattern_size[1]/2), pattern_size[0], pattern_size[1])
    pattern_roi=(0,0,golden_image.shape[1],golden_image.shape[0])
    matcher = Matcher()
    matcher.set_pattern(golden_image, pattern_roi)
    search_window_size = (300, 300)
    #search_window = (pivot[0] - int(search_window_size[0]/2), pivot[1] - int(search_window_size[1]/2), search_window_size[0], search_window_size[1])
    search_window=(0,0,50,500)

    matched_pivot_x, matched_pivot_y = matcher.match(inspect_image, 0.9,search_window, display=True)


    print('test pivot match done')