import os, platform
os.system('git pull')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from POWER404 import menu
    menu()
elif bit == '32bit':
    from POWER404 import menu
    menu()