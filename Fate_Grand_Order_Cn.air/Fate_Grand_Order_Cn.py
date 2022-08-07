# Encoding utf8
# Python 3.7.7
# Update in 2022/8/7
# Author by Yui_Roma

__author__ = "YuiSaka"

import json
from airtest.core.api import *

auto_setup(__file__)

def load_config():
    # Get current resolution
    w, h = device().get_current_resolution()
    
    # Coordinate information
    # First: [1](110,870);[2](245,870);[3](375,870)
    # Second:[1](890,870);[2](720,870);[3](850,870)
    # Third: [1](1065,870);[2](1195,870);[3](1330,870)
    # Hero:  [Main](1790,480)
    #        [1](1360,470);[2](1495,470);[3](1630,870)
    # Skill: [1](475,690);[2](960,690);[3](1420,690)
    # Config initial
    with open("Fate_Grand_Order_Cn_Config.json", "r") as file_obj:
        config = json.load(file_obj)

    for ck in config["coordinate"].keys():
        for ckk in config["coordinate"][ck].keys():
            config["coordinate"][ck][ckk] = [round(config["coordinate"][ck][ckk][0] / config["resolution"][0] * w, 0), 
                                             round(config["coordinate"][ck][ckk][1] / config["resolution"][1] * h, 0)]
    return config
    
def start_game():
    # Start game
    # [Adb_Command] adb shell pm list packages
    start_app("com.bilibili.fatego")
    # Updates will cause errors
    wait(Template("start_touch.png", record_pos=(-0.001, 0.250), resolution=(1920, 1080)), timeout=60, interval=10, intervalfunc=restart_game)
    time.sleep(1)    
    touch(Template("start_touch.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(30)
    # Enter game
    touch(Template("start_logo.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(20)
    # Close announcement
    touch(Template("start_close.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)
    # Receive login rewards
    for i in range(3):
        if exists(Template("button_close.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("button_close.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
        else:
            break
        
def restart_game():
    stop_app("com.bilibili.fatego")
    time.sleep(5)
    start_game()

def daily_quest(cycle=4):
    coordinate = config["coordinate"]
    
    # Entrance at the top of scroll bar
    if not exists(Template("daily_entrance.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
        click(coordinate["scroll"]["start"])
        time.sleep(1)
    try:
        touch(Template("daily_entrance.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(1)
    except Exception:
        raise "[Error][Daily_Quest] Cant find daily entrance."
    
    # Quest at the buttom of scroll bar
    if not exists(Template("daily_quest.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
        click([coordinate["scroll"]["start"][0] + coordinate["scroll"]["interval"][0] * 3, 
               coordinate["scroll"]["start"][1] + coordinate["scroll"]["interval"][1] * 3])
        time.sleep(1)
    try:
        touch(Template("daily_quest.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(1)
    except Exception:
        raise "[Error][Daily_Quest] Cant find daily quest."
    
    # Quest at the buttom of scroll bar
    click([coordinate["scroll"]["start"][0] + coordinate["scroll"]["interval"][0] * 3, 
           coordinate["scroll"]["start"][1] + coordinate["scroll"]["interval"][1] * 3])
    time.sleep(1)
    if not exists(Template("daily_coin_level_4.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
        click([coordinate["scroll"]["start"][0] + coordinate["scroll"]["interval"][0], 
               coordinate["scroll"]["start"][1] + coordinate["scroll"]["interval"][1]])
        time.sleep(1)
    try:
        touch(Template("daily_coin_level_4.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(1)
    except Exception:
        raise "[Error][Daily_Quest] Cant find coin level."
    
    for c in range(cycle):
        # Find equipment
        for i in range(5):
            if not exists(Template("equipment_monalisa.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
                click([coordinate["scroll"]["start"][0] + coordinate["scroll"]["interval"][0] * i, 
                       coordinate["scroll"]["start"][1] + coordinate["scroll"]["interval"][1] * i])
                time.sleep(1)
            else:
                break
        try:
            touch(Template("equipment_monalisa.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
        except Exception:
            raise "[Error][Daily_Quest] Cant find equipment monalisa."
        # Only select at once
        if c == 0:
            for x in range(10):
                if not exists(Template("quest_team_name.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
                    click([coordinate["scroll"]["start"][0] + coordinate["scroll"]["interval"][0], 
                           coordinate["scroll"]["start"][1] + coordinate["scroll"]["interval"][1]])
                    time.sleep(1)
                else:
                    touch(Template("button_start_quest.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
                    time.sleep(1)
                    break

        # Round 1
        wait(Template("quest_attack.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)), timeout=60, interval=10)
        time.sleep(1.5)
        click(coordinate["first"]["skill1"])
        time.sleep(5)
        click(coordinate["second"]["skill1"])
        time.sleep(1.5)
        click(coordinate["skill"]["target1"])
        time.sleep(5)
        click(coordinate["second"]["skill2"])
        time.sleep(1.5)
        click(coordinate["skill"]["target1"])
        time.sleep(5)
        click(coordinate["third"]["skill1"])
        time.sleep(5)
        click(coordinate["third"]["skill2"])
        time.sleep(1.5)
        click(coordinate["skill"]["target1"])
        time.sleep(5)
        click(coordinate["third"]["skill3"])
        time.sleep(1.5)
        click(coordinate["skill"]["target1"])
        time.sleep(5)
        click(coordinate["hero"]["main"])
        time.sleep(1.5)
        click(coordinate["hero"]["skill2"])
        time.sleep(1.5)
        click(coordinate["skill"]["target1"])
        time.sleep(5)
        click(coordinate["attack"]["main"])
        time.sleep(3)
        click(coordinate["attack"]["master1"])
        time.sleep(1.5)
        click(coordinate["attack"]["card1"])
        time.sleep(1.5)
        click(coordinate["attack"]["card2"])
        # Round 2
        wait(Template("quest_attack.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)), timeout=60, interval=10)
        time.sleep(1.5)
        click(coordinate["attack"]["main"])
        time.sleep(1.5)
        click(coordinate["attack"]["master1"])
        time.sleep(1.5)
        click(coordinate["attack"]["card1"])
        time.sleep(1.5)
        click(coordinate["attack"]["card2"])
        # Round 3
        wait(Template("quest_attack.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)), timeout=60, interval=10)
        time.sleep(1.5)
        click(coordinate["attack"]["main"])
        time.sleep(1.5)
        click(coordinate["attack"]["master1"])
        time.sleep(1.5)
        click(coordinate["attack"]["card1"])
        time.sleep(1.5)
        click(coordinate["attack"]["card2"])
        # Checkout
        wait(Template("quest_fetters.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)), timeout=60, interval=10)
        time.sleep(1.5)
        touch(Template("quest_fetters.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(3)
        touch(Template("quest_exp.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(3)
        touch(Template("quest_next.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(5)
        if i < 3:
            touch(Template("quest_continue.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(5)
        else:
            touch(Template("button_close.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(1.5)

def exp_quest(cycle=300):
    coordinate = config["coordinate"]

    for c in range(cycle):
        # Find character
        for i in range(5):
            if not exists(Template("character_berserker_arjuna.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
                # Select class
                if i == 0:
                    touch(Template("class_berserker.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
                    time.sleep(3)
                click([coordinate["scroll"]["start"][0] + coordinate["scroll"]["interval"][0] * i, 
                       coordinate["scroll"]["start"][1] + coordinate["scroll"]["interval"][1] * i])
                time.sleep(1)
            else:
                break
        try:
            touch(Template("character_berserker_arjuna.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
        except Exception:
            raise "[Error][Exp_Quest] Cant find character arjuna."
        # Only select at once
        if c == 0:
            touch(Template("button_start_quest.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))                    
            time.sleep(1)
        # Round 1
        wait(Template("quest_attack.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)), timeout=60, interval=10)
        time.sleep(1.5)
        click(coordinate["first"]["skill3"])
        time.sleep(5)
        click(coordinate["hero"]["main"])
        time.sleep(1.5)
        click(coordinate["hero"]["skill2"])
        time.sleep(1.5)
        click(coordinate["skill"]["target1"])
        time.sleep(5)
        click(coordinate["attack"]["main"])
        time.sleep(1.5)
        click(coordinate["attack"]["master1"])
        time.sleep(1.5)
        click(coordinate["attack"]["card1"])
        time.sleep(1.5)
        click(coordinate["attack"]["card2"])
        # Round 2
        wait(Template("quest_attack.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)), timeout=60, interval=10)
        time.sleep(1.5)
        click(coordinate["second"]["skill2"])
        time.sleep(5)
        click(coordinate["attack"]["main"])
        time.sleep(1.5)
        click(coordinate["attack"]["master2"])
        time.sleep(1.5)
        click(coordinate["attack"]["card1"])
        time.sleep(1.5)
        click(coordinate["attack"]["card2"])
        # Round 3
        wait(Template("quest_attack.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)), timeout=60, interval=10)
        time.sleep(1.5)
        click(coordinate["third"]["skill1"])
        time.sleep(5)
        click(coordinate["attack"]["main"])
        time.sleep(1.5)
        click(coordinate["attack"]["master3"])
        time.sleep(1.5)
        click(coordinate["attack"]["card1"])
        time.sleep(1.5)
        click(coordinate["attack"]["card2"])
        # Checkout
        wait(Template("quest_fetters.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)), timeout=60, interval=10)
        time.sleep(1.5)
        touch(Template("quest_fetters.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(3)
        # Friendship level up
        if exists(Template("quest_fetters.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("quest_fetters.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
        touch(Template("quest_exp.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(3)
        touch(Template("quest_next.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(3)
        if exists(Template("quest_complete.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("quest_complete.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
        else:
            touch(Template("quest_continue.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(5)
        if exists(Template("quest_apple_silver.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("quest_apple_silver.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(1.5)
            touch(Template("button_decide.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(5)

def event_quest(cycle=3):
    coordinate = config["coordinate"]

    for c in range(cycle):
        # Find character
        for i in range(5):
            if not exists(Template("character_caster_arthur.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
                # Select class
                if i == 0:
                    touch(Template("class_caster.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
                    time.sleep(3)
                click([coordinate["scroll"]["start"][0] + coordinate["scroll"]["interval"][0] * i, 
                       coordinate["scroll"]["start"][1] + coordinate["scroll"]["interval"][1] * i])
                time.sleep(1)
            else:
                break
        try:
            touch(Template("character_caster_arthur.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
        except Exception:
            raise "[Error][Event_Quest] Cant find character arthur."
        # Only select at once
        if c == 0:
            touch(Template("button_start_quest.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))                    
            time.sleep(1)
        # Round 1
        wait(Template("quest_attack.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)), timeout=60, interval=10)
        time.sleep(1.5)
        click(coordinate["third"]["skill1"])
        time.sleep(5)
        click(coordinate["third"]["skill2"])
        time.sleep(1.5)
        click(coordinate["skill"]["target2"])
        time.sleep(5)
        click(coordinate["third"]["skill3"])
        time.sleep(1.5)
        click(coordinate["skill"]["target2"])
        time.sleep(5)
        click(coordinate["hero"]["main"])
        time.sleep(1.5)
        click(coordinate["hero"]["skill3"])
        time.sleep(1.5)
        click(coordinate["Character"]["third"])
        time.sleep(1)
        click(coordinate["Character"]["Fourth"])
        time.sleep(1)
        click(coordinate["Character"]["Confirm"])
        time.sleep(7)
        click(coordinate["third"]["skill1"])
        time.sleep(5)
        click(coordinate["third"]["skill2"])
        time.sleep(1.5)
        click(coordinate["skill"]["target2"])
        time.sleep(5)
        click(coordinate["third"]["skill3"])
        time.sleep(1.5)
        click(coordinate["skill"]["target2"])
        time.sleep(5)
        click(coordinate["first"]["skill1"])
        time.sleep(5)
        click(coordinate["second"]["skill1"])
        time.sleep(5)
        click(coordinate["first"]["skill2"])
        time.sleep(5)
        click(coordinate["first"]["skill3"])
        time.sleep(1.5)
        click(coordinate["skill"]["target2"])
        time.sleep(5)
        click(coordinate["attack"]["main"])
        time.sleep(1.5)
        click(coordinate["attack"]["master2"])
        time.sleep(1.5)
        click(coordinate["attack"]["card1"])
        time.sleep(1.5)
        click(coordinate["attack"]["card2"])
        # Round 2
        wait(Template("quest_attack.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)), timeout=60, interval=10)
        time.sleep(1.5)
        click(coordinate["hero"]["main"])
        time.sleep(1.5)
        click(coordinate["hero"]["skill1"])
        time.sleep(5)
        click(coordinate["attack"]["main"])
        time.sleep(1.5)
        click(coordinate["attack"]["master1"])
        time.sleep(1.5)
        click(coordinate["attack"]["card1"])
        time.sleep(1.5)
        click(coordinate["attack"]["card2"])
        # Round 3
        wait(Template("quest_attack.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)), timeout=60, interval=10)
        time.sleep(1.5)
        click(coordinate["second"]["skill2"])
        time.sleep(1.5)
        click(coordinate["skill"]["target2"])
        time.sleep(5)
        click(coordinate["second"]["skill3"])
        time.sleep(5)
        click(coordinate["attack"]["main"])
        time.sleep(1.5)
        click(coordinate["attack"]["master2"])
        time.sleep(1.5)
        click(coordinate["attack"]["card1"])
        time.sleep(1.5)
        click(coordinate["attack"]["card2"])
        # Checkout
        wait(Template("quest_fetters.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)), timeout=60, interval=10)
        time.sleep(1.5)
        touch(Template("quest_fetters.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(3)
        # Friendship level up
        if exists(Template("quest_fetters.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("quest_fetters.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
        touch(Template("quest_exp.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(3)
        touch(Template("quest_next.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(3)
        if exists(Template("quest_next.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("quest_next.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
        
        if exists(Template("quest_complete.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("quest_complete.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
        else:
            touch(Template("quest_continue.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(5)
        if exists(Template("quest_apple_golden.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("quest_apple_golden.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(1.5)
            touch(Template("button_decide.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)

def event_reward():
    coordinate = config["coordinate"]

    while True:
        touch(Template("pool_draw.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(3)
        click(int(config["resolution"][0] * 0.2), int(config["resolution"][1] * 0.2))
        time.sleep(1)
        for i in range(29):
            try:
                print(i)
                touch(Template("pool_draw.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
                time.sleep(1.5)
            except:
                break
        click(int(config["resolution"][0] * 0.2), int(config["resolution"][1] * 0.2))
        time.sleep(3)
        if exists(Template("pool_reset.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("pool_reset.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(1.5)
            touch(Template("button_execute.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(1.5)
            touch(Template("button_close.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(5)
    
if __name__ == '__main__':
    # Load global config
    config = load_config()
    
    #start_game()
    #daily_quest()
    exp_quest()
    #event_quest()
    #event_reward()
    
