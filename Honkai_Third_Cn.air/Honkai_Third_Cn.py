# -*- encoding=utf8 -*-
__author__ = "YuiSaka"

from airtest.core.api import *

auto_setup(__file__)

def start_game():
    # Start game
    # [Adb_Command] adb shell pm list packages
    start_app("com.miHoYo.enterprise.NGHSoD")
    time.sleep(50)
    wait(Template(r"game_flag.png", record_pos=(-0.015, 0.130), resolution=(1920, 1080)))
    touch(Template(r"game_flag.png", record_pos=(-0.015, 0.130), resolution=(1920, 1080)))
    time.sleep(20)
    touch(Template(r"game_start_receive.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template(r"confirm.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    if exists(Template(r"game_start_receive.png", record_pos=(0.085, 0.235), resolution=(1920, 1080))):
        touch(Template(r"game_start_receive.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
        time.sleep(3)
        touch(Template(r"confirm.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
        time.sleep(3)
    if exists(Template(r"start_abyss.png", record_pos=(0.085, 0.235), resolution=(1920, 1080))):
        touch(Template(r"start_abyss.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
        time.sleep(3)
    touch(Template(r"close_button.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    if exists(Template(r"close_button.png", record_pos=(0.085, 0.235), resolution=(1920, 1080))):
        touch(Template(r"close_button.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
        time.sleep(3)
    
        

def home_receive():
    touch(Template(r"home_button.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template(r"coin_receive.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template(r"quest.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template(r"menu.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    
    for i in range(4):
        click([1435,135])
        time.sleep(3)
        touch(Template(r"confirm.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
        time.sleep(3)

    for i in range(4):
        click([1435,135])
        time.sleep(3)
        touch(Template(r"dispatch.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
        time.sleep(3)
        touch(Template(r"start_work.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
        time.sleep(3)
    touch(Template(r"back_button.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template(r"story_sweep.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    coordinate = [[1420,365], [1420,555], [1420,745]]
    click(coordinate[0])
    time.sleep(3)
    touch(Template(r"confirm.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    for i in range(3):
        click(coordinate[i])
        time.sleep(3)
        touch(Template(r"dispatch.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
        time.sleep(3)
        touch(Template(r"confirm_story.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
        time.sleep(3)
    touch(Template(r"resource_button.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    click(coordinate[0])
    time.sleep(3)
    touch(Template(r"confirm.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    for i in range(3):
        click(coordinate[i])
        time.sleep(3)
        touch(Template(r"dispatch.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
        time.sleep(3)
        touch(Template(r"confirm_story.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
        time.sleep(3)
    touch(Template(r"main_menu.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)

def fleet_receive():
    touch(Template(r"fleet_button.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template(r"fleet_mission_button.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template(r"fleet_entrust.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template(r"fleet_accept.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    for i in range(8):
        touch(Template(r"fleet_submit.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
        time.sleep(3)
        touch(Template(r"fleet_entrust_submit.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
        time.sleep(3)
        touch(Template(r"fleet_put.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
        time.sleep(3)
        
    touch(Template(r"fleet_bonus.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template(r"fleet_receive.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template(r"confirm.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template(r"main_menu.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)

def mission_complete(receive_flag=False):
    touch(Template(r"mission_button.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template(r"receive_button.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template(r"confirm.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    if receive_flag:
        click([1825,1000])
        time.sleep(3)
        touch(Template(r"confirm.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
        time.sleep(3)
    touch(Template(r"back_button.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(5)

def mission_quest():
    touch(Template(r"attack_button.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template(r"resource_quest.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template(r"event_attack_button.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template(r"event_confirm.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template(r"confirm.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template(r"main_menu.png", record_pos=(0.085, 0.235), resolution=(1920, 1080)))
    time.sleep(3)
    
    
def main():
    # Get resolution
    w,h = device().get_current_resolution()

    #start_game()
    mission_complete(False)
    home_receive()
    mission_quest()
    fleet_receive()
    mission_complete(True)
    
if __name__ == '__main__':
    main()