from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

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
    
    #아이템 삭제시 안내를 위한 if문
    if item_id not in items:
        return {"error": f"{item_id}번 품목이 없습니다."}
        #return {"error": f"there's no item id: {"item_id"}"}

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


#데이터 CRUD 기능 실습.

#BaseModel을 상속받는 Item 클래스 생성.
class Item(BaseModel):
    name: str
    price: int

@app.post("/items/{item_id}")

def create_item(item_id: int, item: Item):
    if item_id in items:
        return {"error": "there's already existing key."}
    items[item_id] = dict(item) #아이템의 형태가 dictionary 형태로 관리되기 때문에, 같은 형식인 dict로 바꿔주는 것임.
    print(items) #터미널에 출력 확인용.
    return {"success": "ok"}


#Update
class ItemForUpdate(BaseModel):
    name: Optional[str]
    price: Optional[int] 
    
#Post 방식에서는 유효성 검사를 거치기 때문에, name이나 price 에서 하나만 빠져도 유효성 검사에서 걸린다.
#이 부분을 개선하기 위해서 Optional를 사용해서, 변경이 된 값 넘길 수 있도록 해준다.

@app.put("/items/{item_id}")

def update_item(item_id: int, item: ItemForUpdate):
    #유효성 검사
    if item_id not in items: 
        return {"error": f"there's no item id: {item_id}"}
    
    if item.name:
        items[item_id]['name'] = item.name

    if item.price:
        items[item_id]['price'] = item.price

    return {"success": "ok"}

#삭제 구현
@app.delete("/items/{item_id}")

def delete_item(item_id: int):
    items.pop(item_id)
    return{"success": "ok"}
