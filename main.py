import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


def check_spisok():
    response = requests.get('https://abitlist.pskgu.ru/lists/spd-4a76db24aa.html')
    a = response.text
    symb = '''<>/?\\-="!{}():;./,@#qwertyuiop[]asdfghjkl;zxcvbnm,./QWERTYUIOPASDFGHJKLZXCVBNM*%№'''
    ans = []
    for i in symb:
        b = a.replace(i, ' ')
        ans.append(b.strip())
        a = b.strip()
    stroka = ans[-1]
    otvet = ''
    # print([ans[-1]])
    for i in range(len(ans[-1])):
        try:
            if stroka[i] == ' ' and stroka[i + 1] == ' ':
                pass
            elif stroka[i] != ' ' or stroka[i] == ' ' and stroka[i + 1] != ' ':
                otvet += stroka[i]
        except Exception:
            pass
    ans = ' '.join(otvet.split()[-10:])
    return ans


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(check_spisok())


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(check_spisok())


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, check_spisok())


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()


