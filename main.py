from spam import *
import subprocess
import sys
import threading

def run(file):
    subprocess.run([
        sys.executable, 'spam.py', '--a', file
    ])
async def main():
    os.chdir(os.getcwd())
    #for file in glob.glob("*.session"):
    list_sessions_ = list() 
    list_sessions = glob.glob("*.session")
    for file in list_sessions:
        x = threading.Thread(target=run, args=(file,))
        x.start()
    while True:
        os.chdir(os.getcwd())
        if list_sessions != glob.glob('*.session'):
            sess = glob.glob('*.session') - list_sessions
            for i in sess:
                x = threading.Thread(target=run, args=(file,))
                x.start()
        

asyncio.run(main())
#while True:


        