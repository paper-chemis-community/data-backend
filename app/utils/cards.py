import json

def readCardList() -> dict:
    with open("resources/cards/list.json", "r", encoding="utf8") as f:
        text = f.read()
        result = json.loads(text)
    
    return result

def readCard(id: str):
    path = readCardList().get(id, -1)
    if (path == -1):
        return {"message": f"No Card {id}"}
    with open(f"resources/cards/{path}.json", "r", encoding="utf8") as f:
        text = f.read()
        result = json.loads(text)
        
    return {"message": "OK", "content": result}