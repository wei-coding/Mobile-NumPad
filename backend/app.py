from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pyautogui as pg
import socket
import uvicorn
import subprocess

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

keymap = [
    'num0',
    'num1',
    'num2',
    'num3',
    'num4',
    'num5',
    'num6',
    'num7',
    'num8',
    'num9',
    'decimal',
    'return',
    'backspace'
]

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/api/v1/key/{key_id}")
async def keydown(key_id: int):
    pg.press(keymap[key_id])
    return {"status": "ok", "key_id": key_id}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
