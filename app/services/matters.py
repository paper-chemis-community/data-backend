import json

def readMatterList() -> dict:
    with open("resources/matters/list.json", "r", encoding="utf8") as f:
        text = f.read()
        result = json.loads(text)
    
    return result

def readMatter(id: str):
    path = readMatterList().get(id, -1)
    if (path == -1):
        return {"message": f"No Matter {id}"}
    with open(f"resources/matters/{path}.json", "r", encoding="utf8") as f:
        text = f.read()
        result = json.loads(text)
        
    return {"message": "OK", "content": result}