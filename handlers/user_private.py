from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram import  Router, F

user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Salom Men online admin man qanday yordam bera olaman")
    
    
@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer("Bot menu")

@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer("Bot about")
    
    
@user_private_router.message(Command('payments'))
async def payment_cmd(message: types.Message):
    await message.answer("Bot payments")
    
    
@user_private_router.message(Command('shipping'))
async def shipping_cmd(message: types.Message):
    await message.answer("Bot yetqazib berish")
        
        
@user_private_router.message(F.text)
async def shipping_cmd(message: types.Message):
    await message.answer("Bu filtir")
    
 