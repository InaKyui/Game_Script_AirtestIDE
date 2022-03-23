# -*- encoding=utf8 -*-
__author__ = "YuiSaka"

from airtest.core.api import *

auto_setup(__file__)


def start_game():
    # Start game
    start_app("com.bilibili.fatego")
    time.sleep(20)
    # Updates will cause errors
    wait(Template("start_touch.png", record_pos=(-0.001, 0.250), resolution=(1920, 1080)))
    touch(Template("start_touch.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(20)
    # Enter game
    touch(Template("start_logo.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(25)
    # Close notice
    touch(Template("close.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)
    # Receive login rewards
    touch(Template("accept.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)

def main():
    # Get resolution
    w,h = device().get_current_resolution()

    start_game()
    
if __name__ == '__main__':
    main()


