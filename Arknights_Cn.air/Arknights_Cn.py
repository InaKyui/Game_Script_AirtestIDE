# Encoding utf8
# Python 3.7.7
# Update in 2022/8/21
# Author by Yui_Roma

import json
from airtest.core.api import *

auto_setup(__file__)

def load_config():
    # Get current resolution
    w, h = device().get_current_resolution()
    
    # Coordinate information
    # Room information
    # Member information
    # Config initial
    with open("Arknights_Cn_Config.json", "r") as file_obj:
        config = json.load(file_obj)

    for ck in config["coordinate"].keys():
        for ckk in config["coordinate"][ck].keys():
            config["coordinate"][ck][ckk] = [round(config["coordinate"][ck][ckk][0] / config["resolution"][0] * w, 0), 
                                             round(config["coordinate"][ck][ckk][1] / config["resolution"][1] * h, 0)]
    return config   

def start_game():
    # Start game
    # [Adb_Command] adb shell pm list packages
    start_app("com.hypergryph.arknights")
    # Updates will cause errors
    wait(Template("login_start.png", record_pos=(-0.001, 0.250), resolution=(1920, 1080)), timeout=60, interval=10)
    time.sleep(1)
    # Enter game
    touch(Template("login_start.png", record_pos=(-0.001, 0.250), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template("login_enter.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    # Receive login rewards
    wait(Template("login_rewards.png", record_pos=(-0.001, 0.250), resolution=(1920, 1080)), timeout=60, interval=10)
    time.sleep(1)
    touch(Template("login_rewards.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template("login_close.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)
    # Close event announcement
    for i in range(5):
        if exists(Template("login_close.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("login_close.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
        else: break

def source_center():
    # Source Center
    touch(Template("entrance_source_center.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template("source_center_exchange.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(1.5)
    touch(Template("source_center_harvest.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(1.5)
    touch(Template("source_center_resource_rewards.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)
    # Exchange item
    
    # Back to home page
    touch(Template("button_back.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)

def change_member(room):
    coordinate = config["coordinate"]
    member_count = config["member_count"][room]

    # Enter room
    click(coordinate["room"][room])
    time.sleep(5)
    # Removal of members
    if not exists(Template("member_release.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
        touch(Template("member_info.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(3)
    touch(Template("member_release.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(1.5)
    if exists(Template("button_ensure.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
        touch(Template("button_ensure.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(1.5)
    # Deployment of members
    touch(Template("member_deployment.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)
    if member_count >= 1:
        click(coordinate["member"]["first"])
        time.sleep(1)
    if member_count >= 2:
        click(coordinate["member"]["second"])
        time.sleep(1)
    if member_count >= 3:
        click(coordinate["member"]["third"])
        time.sleep(1)
    if member_count >= 4:
        click(coordinate["member"]["fourth"])
        time.sleep(1)
    if member_count >= 5:
        click(coordinate["member"]["fifth"])
        time.sleep(1)
    for i in range(3):
        exist_count = 0
        if exists(Template("member_confirm.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("member_confirm.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
            exist_count = exist_count + 1
        if exists(Template("member_confirm_double.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("member_confirm_double.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            exist_count = exist_count + 1
        if exist_count == 0:
            break
    # Back to home page
    touch(Template("button_back.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(5)

def infrastructure():
    # Infrastructure
    touch(Template("entrance_infrastructure.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(5)
    if exists(Template("infrastructure_notification.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
        touch(Template("infrastructure_notification.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(1.5)
        # Harvest resources
        if exists(Template("infrastructure_exp_ore.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("infrastructure_exp_ore.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(1.5)
        if exists(Template("infrastructure_coin.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("infrastructure_coin.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(1.5)
        if exists(Template("infrastructure_trust.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("infrastructure_trust.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(1.5)
        # Exit harvesting interface
        if exists(Template("infrastructure_to_do.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("infrastructure_to_do.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
    # Center
    touch(Template("infrastructure_center.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(5)
    change_member("center")
    # Trading - A
    change_member("trade_a")
    # Trading - B
    change_member("trade_b")
    # Manufacturing - A
    change_member("manufacture_a")
    # Manufacturing - B
    change_member("manufacture_b")
    # Manufacturing - C
    change_member("manufacture_c")
    # Manufacturing - D
    change_member("manufacture_d")
    # Dormitory - A
    change_member("dormitory_a")
    # Dormitory - B
    change_member("dormitory_b")
    # Dormitory - C
    change_member("dormitory_c")
    # Dormitory - D
    change_member("dormitory_d")
    # Meeting
    # change_member("meeting")
    # Office
    change_member("office")
    # Back to home page
    for i in range(5):
        if exists(Template("button_back.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("button_back.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
        else: break

def daily_quest():
    # Sanity
    touch(Template("entrance_terminal.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(5)
    touch(Template("daily_resource.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(1.5)
    # 1. Coin quest
    if exists(Template("daily_coin.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
        touch(Template("daily_coin.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(3)
        touch(Template("daily_coin_ce_5.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(3)
        for i in range(130//30):
            touch(Template("quest_formation.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
            if exists(Template("quest_break.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
                touch(Template("quest_cancel.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
                time.sleep(5)
                break
            touch(Template("quest_start.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            wait(Template("quest_finish.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)), timeout=180, interval=15)
            time.sleep(1)
            touch(Template("quest_finish.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(5)
    # 2. Exp quest
    elif exists(Template("daily_exp.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
        touch(Template("daily_exp.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(3)
        touch(Template("daily_exp_ls_5.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(3)
        for i in range(130//30):
            touch(Template("quest_formation.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
            if exists(Template("quest_break.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
                touch(Template("quest_cancel.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
                time.sleep(5)
                break
            touch(Template("quest_start.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            wait(Template("quest_finish.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)), timeout=180, interval=15)
            time.sleep(1)
            touch(Template("quest_finish.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(5)
    # Back to home page
    for i in range(5):
        if exists(Template("button_back.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("button_back.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
        else: break

def recruit_check_tag():
    tag_selected = None
    # Tag format = [str/[list]]
    tag_list = [
        # Star 6
        Template("recruit_tag_top_senior.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)),
        # Star 5
        #Template("recruit_tag_senior.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)),
        #Template("recruit_tag_summon.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)),
        # Star 4
        Template("recruit_tag_weaken.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)),
        Template("recruit_tag_erupt.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)),
        Template("recruit_tag_resurrection.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)),
        Template("recruit_tag_move.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)),
        Template("recruit_tag_special.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))
    ]
    for tag in tag_list:
        # Check combo tag
        if isinstance(tag, list):
            match_flag = False
            for t in tag:
                if exists(t):
                    if t == tag[-1]:
                        # All tag matched.
                        match_flag = True
                    else: continue
                else: break
            # Tag matched & Select combo tag
            if match_flag:
                for t in tag:
                    touch(t)
                    time.sleep(1)
                tag_selected = tag
                time.sleep(1.5)
                break
        # Check single tag
        else:
            if exists(tag):
                if tag == Template("recruit_tag_top_senior.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)):
                    input("[Recruit] Top senior. Please check.")
                    time.sleep(1)
                    continue
                touch(tag)
                time.sleep(1.5)
                tag_selected = tag
                time.sleep(3)
                break
    # Select default tag
    if tag_selected == None:
        click(config["coordinate"]["recruit"]["default_tag"])

def recruit_center():
    # Enter recruit center
    touch(Template("entrance_recruit.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)
    # Check accelerate status
    for i in range(4):
        if exists(Template("recruit_accelerate.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("recruit_accelerate.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(1.5)
            if exists(Template("button_ensure.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
                touch(Template("button_ensure.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
                time.sleep(1.5)
            else: break
        else: break
    # Handle old recruit at first
    for i in range(4):
        if exists(Template("recruit_complete.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("recruit_complete.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(5)
            touch(Template("button_skip.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(7)
            click(config["coordinate"]["recruit"]["blank"])
            time.sleep(3)
        else: break
    # New recruit order
    index = ["first", "second", "third", "fourth"]
    for i in range(len(index)):
        click(config["coordinate"]["recruit"][index[i]])
        time.sleep(3)
        click(config["coordinate"]["recruit"]["max_time"])
        time.sleep(1.5)
        recruit_check_tag()
        time.sleep(3)
        touch(Template("recruit_ensure.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(1.5)


    # Back to home page
    for i in range(5):
        if exists(Template("button_back.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("button_back.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
        else: break

def mission_complete():
    # Mission
    touch(Template("entrance_mission.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template("mission_receive.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(1)
    # Back to home page
    # touch(Template("button_back.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    # time.sleep(5)

def event_quest():
    for i in range(100):
        if exists(Template("quest_formation.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("quest_formation.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
            # if exists(Template("quest_break.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            #     touch(Template("quest_cancel.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            #     time.sleep(5)
            #     break
            touch(Template("quest_start.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            wait(Template("quest_finish.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)), timeout=180, interval=15)
            time.sleep(1)
            touch(Template("quest_finish.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(5)

def daily_mission():
    source_center()
    infrastructure()
    daily_quest()
    recruit_center()
    mission_complete()
    
if __name__ == '__main__':
    # Load global config
    config = load_config()
    
    start_game()
    daily_mission()
    #event_quest()
    
