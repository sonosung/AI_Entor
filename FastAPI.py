from fastapi import FastAPI

app = FastAPI()

@app.get("/helloworld")
def get_helloworld():
    return "hello world"

#cart 실습.
items = {
			0: {"name": "brot",
				"price": 1000},
		    1: {"name": "water",
			    "price": 500},
		    2: {"name": "라면",
				"price": 1200}
	    }

#경로에 파라미터를 넣을 수 있는 path parameter
# Path Parameter ex.1
@app.get("/items/{item_id}")

def read_item(item_id: int):
    item = items[item_id]
    return item

# Path Parameter ex.2
@app.get("/items/{item_id}/{key}")

def read_item_and_key(item_id: int, key: str): 
    item = items[item_id][key]
    return item

#Query Parameter 주소창의 경로 뒤에 "?"로 경로를 가리키는 쿼리 파라미터
@app.get("/item-by-name")

def read_tiem_by_name(name: str):
    for item_id, item in items.items():
        if item['name'] == name:
            return item
    return {"error": "data not found"}   