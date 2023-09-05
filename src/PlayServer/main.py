from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from PlayServer.routers import auth, user, playlist, channel, ws
from PlayServer import webapp

app = FastAPI()

app.include_router(auth.router, prefix="/api")
app.include_router(user.router, prefix="/api")
app.include_router(playlist.router, prefix="/api")
app.include_router(channel.router, prefix="/api")
app.include_router(ws.router, prefix="/api")

app.mount(
    "",
    StaticFiles(directory=webapp.__path__[0], html=True),
    name="static"
)


@app.get("/api/hello")
async def hello():
    return {"message": "Hello, World!"}
