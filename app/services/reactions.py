import json

def readReactionList() -> dict:
    with open("reactions/list.json", "r", encoding="utf8") as f:
        text = f.read()
        result = json.loads(text)
    
    return result

def readReaction(id: str):
    return readReactionList().get(id, -1)