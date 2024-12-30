from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import FSInputFile

import yt_dlp
import os

BOT_TOKEN = '7102363016:AAHgwDr-MC2rqKT52e3fDnLSik8pNJ8hm_0'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

ydl_opts = {
            'outtmpl': 'media/%(title)s.%(ext)s',
            'quiet': False,
            'no_warnings': True
        }

def dwl_vid(video_url):
    ydl_opts = {
        'outtmpl': 'media/%(title)s.%(ext)s',
        'quiet': False,
        'no_warnings': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        ydl.download([video_url])
    return {
        'path': f'media/{info["title"]}.mp4'
    }

def info_video(video_url):
    ydl_opts = {
        'outtmpl': 'media/%(title)s.%(ext)s',
        'quiet': False,
        'no_warnings': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        print(info["prew"])

def dwn_mp3(music_url):
    ydl_opts = {'format': 'bestaudio', 'outtmpl': 'media/%(title)s.mp3'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(music_url, download=False)
        ydl.download([music_url])
    return {
        'path': f'media/{info["title"]}.mp3'
    }
@dp.message(Command("start"))
async def start(message: Message):
    await message.reply("Здравствуйте, этот бот поможет вам скачать видио из YouTube. Введите Команду /download, ссылку на видио и формат который вы хотите получить (пока доступны mp4 и mp3)")

@dp.message(Command("download"))
async def download(message: Message, command: CommandObject):
    if(command.args != None):
        input_args = command.args.split()
        if input_args[1] == "mp4":
            data = dwl_vid(input_args[0])
            await message.reply_video(FSInputFile(data['path']))
            os.remove(data['path'])
        elif input_args[1] == "mp3":
            data = dwn_mp3(input_args[0])
            await message.reply_audio(FSInputFile(data['path']))
            os.remove(data['path'])
        else:
            await message.reply("Такой формат не поддерживается")
    else:
        await message.reply("Вы не ввели формат или ссылку!")


@dp.message(Command("info"))
async def info(message: Message, command: CommandObject):
    info_video(command.args)

if __name__ == '__main__':
 dp.run_polling(bot)

#ydytrdyd