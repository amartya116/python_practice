from fastapi import FastAPI
from pydantic import BaseModel

class TodoList(BaseModel):
    Deadline: str
    Job: str
    priority:str

List=[]
app = FastAPI()

@app.get("/name/{name}")
async def greet_name(name: str):  # Renamed the function to avoid conflict
    return {"message": f"hello {name}"}

@app.get("/agesUsers")
async def get_age(age: int = 10):  # Renamed the function to avoid conflict
    return {"message": f"you are {age} years old"}

# @app.post('/items')
# async def create_list(user:User):
#     return {"message":f"greetings {user.name} umar {user.age} saal"}

@app.post('/todo')
async def create_list(todolist: TodoList):
    # Access the attributes of the instance `todolist`
    List.append({
        "Deadline": todolist.Deadline,
        "Job": todolist.Job,
        "priority": todolist.priority
    })
    return {"message": "Todo item added successfully", "data": List}

@app.put('/todo/{index}')
async def update_list(index: int, todolist: TodoList):
    if 0 <= index < len(List):
        List[index] = {
            "Deadline": todolist.Deadline,
            "Job": todolist.Job,
            "priority": todolist.priority
        }
        return {"message": "Todo item updated successfully", "data": List}
    else:
        return {"message": "Index out of range"}
@app.delete('/todo/{index}')
async def delete_list(index: int):
    if 0 <= index < len(List):
        deleted_item = List.pop(index)
        return {"message": "Todo item deleted successfully", "data": List}
    else:
        return {"message": "Index out of range"}
