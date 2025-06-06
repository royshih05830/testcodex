import requests
import xml.etree.ElementTree as ET
import json

def getProductNumber(url,SN):        
    base_url = f"{url}"
   
    params = {
        "SN": SN,
        "MC": "TPMC"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
                
        return ET.fromstring(response.text).text
        
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None
    
def getProductNumber2(url,SN):        
    base_url = f"{url}"
   
    params = {
        "SerialNo": SN,
        "MC": "TPMC"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        data = json.loads(ET.fromstring(response.text).text.strip())
        code = data['code']
        if code == 0:
            value = data['value']
            PN = data['value']['PN']
            
            #Level,Product_Code,Version = PN.split('-')                                    
            
            
            #print(Level,Product_Code,Version)
        
            return PN,value
        else:
            #print(f'URL: {base_url}')
            #print(f'SN: {SN}')
            #print(f'Return code: {code}')
            return None,{}
        
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None, {}
    
def findPNfromResponse(text,SN):
    
    if text:        
        responseList = text.split(';')
        if responseList[0]==SN:
            return responseList[1]   
        else:
            print(f'Response serinal number({responseList[0]}) is different from the entered serinal number({SN}).') 
    else:
        print('response is empty')
        
    return None
        

if __name__ == '__main__':        
    url = 'http://172.16.65.183/MESWebService_3.5/MESWebService.asmx/GetSNBasis'
    SN = 'BA36NB1056'
    text = getProductNumber(url,SN)
    result = findPNfromResponse(text,SN)
    
    
    
    
    url = 'http://itetp.adlinktech.com/Modules/SmartFactory/AutomationTP.asmx/GetADLINKSNInfoJson'
    SN = '2471100GM2'
    
    PN,_ = getProductNumber2(url,SN)   
    
    print(PN)

    
    
    
    