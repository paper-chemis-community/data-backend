'''
读取物质定义文件列表和内容
'''
import json

def readMatterList() -> dict:
    with open("resources/matters/list.json", "r", encoding="utf8") as f:
        text = f.read()
        result = json.loads(text)
    
    return result



matter_list = readMatterList()


def readMatter(id: str):
    path = matter_list.get(id, -1)
    if (path == -1):
        return {"message": f"No Matter {id}"}
    with open(f"resources/matters/{path}.json", "r", encoding="utf8") as f:
        text = f.read()
        result = json.loads(text)
        
    return {"message": "OK", "content": result}
