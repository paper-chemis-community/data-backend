'''
读取反应定义文件列表和内容
'''
import json

def readReactionList() -> dict:
    with open("resources/reactions/list.json", "r", encoding="utf8") as f:
        text = f.read()
        result = json.loads(text)
    
    return result

def readMatchList() -> dict:
    with open("resources/reactions/match.json", "r", encoding="utf8") as f:
        text = f.read()
        result = json.loads(text)
    
    return result

reaction_list = readReactionList()
match_list = readMatchList()

def readReaction(id: str):
    path = reaction_list.get(id, -1)
    if (path == -1):
        return {"message": f"No Reaction {id}"}
    with open(f"resources/reactions/{path}.json", "r", encoding="utf8") as f:
        text = f.read()
        result = json.loads(text)
        
    return {"message": "OK", "content": result}


def selectReaction(id: str):
    matter_id = match_list.get(id, -1)
    if matter_id == -1:
        return {"message": f"No Matter {id}"}
    
    return matter_id