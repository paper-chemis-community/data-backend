'''
读取反应定义文件列表和内容
'''
import json

def readReactionList() -> dict:
    with open("resources/reactions/list.json", "r", encoding="utf8") as f:
        text = f.read()
        result = json.loads(text)
    
    return result

reaction_list = readReactionList()

def readReaction(id: str):
    path = reaction_list.get(id, -1)
    if (path == -1):
        return {"message": f"No Reaction {id}"}
    with open(f"resources/reactions/{path}.json", "r", encoding="utf8") as f:
        text = f.read()
        result = json.loads(text)
        
    return {"message": "OK", "content": result}