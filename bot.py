import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import CommandObject

from app import openai_request
from keys import TG_TOKEN


logging.basicConfig(level=logging.INFO)

bot = Bot(token=TG_TOKEN)

dp = Dispatcher()

@dp.message(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Hello!")
    
@dp.message(commands=["openai"])
async def openai_answer(message: types.Message, command: CommandObject):
    if command.args:
        sent = await message.reply('Секунду, думаю...')
        await sent.edit_text(openai_request(command.args))
    else:
        await message.reply("Пожалуйста, введите ваш запрос после команды /openai!")
        
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())