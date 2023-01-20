import os
import time
import keyboard
import psutil as psutil


def auto_keepass(password):
    path = os.environ.get('KEEPASS_PATH')[:-11]
    app = os.environ.get('KEEPASS_PATH')[-11:]

    if not is_keepass_open():
        os.startfile(path + app)
        time.sleep(1.5)
        keyboard.write(password)
        keyboard.press_and_release('enter')
    else:
        print('[WARNING] Keepass is already open')


def is_keepass_open():
    app = os.environ.get('KEEPASS_PATH')[-11:]

    for proc in psutil.process_iter():
        if proc.name() == app:
            return True
    return False


if __name__ == '__main__':
    auto_keepass(os.environ.get('KEEPASS_PWD'))