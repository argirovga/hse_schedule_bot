import logging

from aiogram import Bot, Dispatcher, executor, types

from configs.bot_configs import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def alarm(message: types.Message):
    await message.answer(f"Ваш ID: {message.from_user.id}")


@dp.callback_query_handler(text='user_id')
async def user_id_inline_callback(callback_query: types.CallbackQuery):
    await callback_query.answer(f"Ваш ID: {callback_query.from_user.id}", True)


if __name__ == '__main__':
    executor.start_polling(dp)