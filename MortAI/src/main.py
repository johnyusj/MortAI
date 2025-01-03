from fastapi import FastAPI
from .PostgreSQL import engine, Base
from .routes import example_routes
from fastapi.middleware.cors import CORSMiddleware

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routes
app.include_router(example_routes.router)

origins = [
    "http://localhost:3000",  # React front-end
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows React app to communicate with FastAPI
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/api/greet")
def greet():
    return {"message": "Hello from FastAPI!"}