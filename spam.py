import traceback
from pyrogram import *
import glob, os
from config import *
import time
import schedule
import asyncio
from threading import Thread
from pyrogram import Client, filters, idle
import argparse



async def getinf_and_spam(file):
    print(file)
    try: 
        file = file.replace('.session', '')
        
        app = Client(file, api_id , api_hash )
        async with app:
            #test = app.start()
            #print(test)
            print('КЛиент запущен2')
            while True:
                try:
                    #app.send_message('me', 'Запущен')
                    #chat = app.get_chat("https://t.me/+dXlP6IrfcbRhYzUy")
                    chat_id = (await app.get_chat("me"))['id']
                    last =  await app.get_history(chat_id, limit=3)

                    time_limit = str(last[-1]['text'])
                    links = str(last[1]['text'])
                    text = str(last[0]['text'])
                    list_links = links.split('\n')
                    for i in list_links:
                        chat = (await app.get_chat(i))['id']
                        await app.send_message(chat, text)
                        await asyncio.sleep(30)
                    await asyncio.sleep(int(time_limit))
                except:
                    await asyncio.sleep(20)
        
    except Exception as e:
        traceback.print_exc()

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--a")
args = parser.parse_args()
name = args.a


'''
async def main():
    os.chdir(os.getcwd())
    #for file in glob.glob("*.session"):
    list_sessions_ = list() 
    list_sessions = glob.glob("*.session")
    for file in list_sessions:
            
            list_sessions_.append(Client(file[0].replace('.session', '')))
            task1 = asyncio.create_task(getinf_and_spam(file))

            await task1

    while True:
        if list_sessions != glob.glob("*.session"):
            
            file = glob.glob("*.session") - list_sessions
            list_sessions_.append(Client(file[0].replace('.session', '')))
            task1 = asyncio.create_task(getinf_and_spam(file[0]))

            await task1

            
        else:
            pass
'''


if __name__ == "__main__":
    try:
        asyncio.run(getinf_and_spam(name))
    except :
        pass