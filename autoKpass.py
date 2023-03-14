import os
import time
import keyboard
import psutil as psutil

app = os.environ.get('KEEPASS_PATH')[-11:]
path = os.environ.get('KEEPASS_PATH')[:-11]


def auto_keepass(password):
    app = 'KeePass.exe'
    if not is_keepass_open(app):
        os.startfile(path + app)
        time.sleep(1.6)
        keyboard.write(password, delay=0)
        keyboard.press_and_release('enter')
    else:
        print('[WARNING] Keepass is already open')


def is_keepass_open(app):
    for proc in psutil.process_iter():
        if proc.name() == app:
            return True
    return False


if __name__ == '__main__':
    auto_keepass(os.environ.get('KEEPASS_PWD'))
