from fastapi import FastAPI

application = FastAPI()

@application.get("/")
async def root():
    return {"message": "Hello World"}

# This is the WSGI application variable that Vercel looks for
app = application
