from fastapi import FastAPI
import uvicorn
from todo import todo_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ['http://localhost:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(todo_router)

if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)