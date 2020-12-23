from subprocess import run
from time import sleep

restart_timer = 2
def start_script():
    try:
        run('python get_presence.py', check=True) 
    except:
        handle_crash()

def handle_crash():
    sleep(restart_timer)
    start_script()

start_script()