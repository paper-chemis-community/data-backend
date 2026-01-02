import json

def readCardList() -> dict:
    with open("cards/list.json", "r", encoding="utf8") as f:
        text = f.read()
        result = json.loads(text)
    
    return result

def readCard(id: str):
    return readCardList().get(id, -1)