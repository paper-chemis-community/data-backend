import json

def readMatterList() -> dict:
    with open("matters/list.json", "r", encoding="utf8") as f:
        text = f.read()
        result = json.loads(text)
    
    return result

def readMatter(id: str):
    return readMatterList().get(id, -1)