from fastapi import APIRouter, Path
from model import Todo

todo_router = APIRouter()

todo_list = []
todo_counter = 0

@todo_router.post('/todo')
async def post_todo(todo: Todo) -> dict:
    global todo_counter
    todo.id = todo_counter
    todo_list.append(todo)
    todo_counter += 1
    return {"message": "Todo created successfully"}

@todo_router.get('/todo')
async def get_todos() -> dict:
    return {"todos": todo_list}

@todo_router.get('/todo/{id}')
async def get_todo_by_id(id: int = Path(..., title="The ID of the todo")) -> dict:
    for todo in todo_list:
        if todo.id == id:
            return {"todo" : todo}
    return {"message": "Todo not found"}  

@todo_router.delete('/todo/{id}')
async def delete_todo_by_id(id: int = Path(..., title="The ID of the todo")) -> dict:
    for index, todo in enumerate(todo_list):
        if todo.id == id:
            del todo_list[index]
            return {"message": "Todo deleted successfully"}
    return {"message": "Todo not found"}