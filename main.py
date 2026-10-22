import os
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    # WebApp havolasini keyin Render'dan olgan havolangizga o'zgartirasiz
    web_app_url = "https://sizning-sayt-nomingiz.onrender.com"
    
    kb = [
        [types.InlineKeyboardButton(text="⚽ DLS Turnirni Ochish", web_app=types.WebAppInfo(url=web_app_url))]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer("Xush kelibsiz! DLS Turnir Mini App orqali turnirlarga qo'shiling:", reply_markup=keyboard)

@app.get("/")
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
