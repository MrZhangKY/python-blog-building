import os
import sys
from colorama import init
init(autoreset=True)

BASE_PATH = os.path.dirname(os.getcwd())
sys.path.append(BASE_PATH)
from core.src import run

if __name__ == '__main__':
    run()