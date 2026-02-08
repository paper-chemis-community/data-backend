'''
读取 description.json 的内容
'''
import json

def readIndex() -> dict:
    
    with open("resources/description.json", "r", encoding="utf8") as f:
        text = f.read()
        result = json.loads(text)
    
    return result