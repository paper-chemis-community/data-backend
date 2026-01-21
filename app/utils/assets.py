'''
读取资源文件列表和路径
'''
import json

def readAssetsList() -> dict:
    with open("resources/assets/index.json", "r", encoding="utf8") as f:
        text = f.read()
        result = json.loads(text)
        
    return result

assets_list = readAssetsList()

def readPicPath(id: str):
    return assets_list["pics"][id]

def readSoundPath(id: str):
    return assets_list["sounds"][id]