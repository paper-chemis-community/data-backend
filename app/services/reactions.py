import json

def readReactionList() -> dict:
    with open("resources/reactions/list.json", "r", encoding="utf8") as f:
        text = f.read()
        result = json.loads(text)
    
    return result

def readReaction(id: str):
    path = readReactionList().get(id, -1)
    if (path == -1):
        return {"message": f"No Reaction {id}"}
    with open(f"resources/reactions/{path}.json", "r", encoding="utf8") as f:
        text = f.read()
        result = json.loads(text)
        
    return {"message": "OK", "content": result}