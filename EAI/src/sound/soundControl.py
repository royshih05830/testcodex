import threading
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
# 初始化 pygame.mixer
pygame.mixer.init()

# 定義音效播放的 Thread
class SoundThread(threading.Thread):
    def __init__(self, sound_file):
        super().__init__()
        self.sound_file = sound_file
        self.stop_event = threading.Event()

    def run(self):
        """執行音效播放，直到被停止"""
        pygame.mixer.music.load(self.sound_file)
        pygame.mixer.music.play()
        while not self.stop_event.is_set() and pygame.mixer.music.get_busy():
            time.sleep(0.1)  # 每 0.1 秒檢查是否停止

    def stop(self):
        """停止音效播放"""
        self.stop_event.set()
        pygame.mixer.music.stop()
