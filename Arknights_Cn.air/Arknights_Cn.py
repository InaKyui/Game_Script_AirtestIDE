# -*- encoding=utf8 -*-
__author__ = "YuiSaka"

from airtest.core.api import *

auto_setup(__file__)

def start_game():
    # Start game
    start_app("com.hypergryph.arknights")
    time.sleep(20)

    # Updates will cause errors
    wait(Template("start.png", record_pos=(-0.001, 0.250), resolution=(1920, 1080)))
    # Enter game
    touch(Template("start.png", record_pos=(-0.001, 0.250), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template("start_2.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(15)
    # Receive login rewards
    touch(Template("login_rewards.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    #time.sleep(3)
    touch(Template("close.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(5)
    touch(Template("close.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)

def sanity():
    # Sanity
    touch(Template("terminal.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(5)
    # 1. Event quest
    if exists(Template("event_quest.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
        touch([1800,880])
        time.sleep(3)
        for i in range(130//21):
            touch(Template("start_action.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
            touch(Template("start_action_2.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(180)
            wait(Template("finish_action.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            touch(Template("finish_action.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(5)
            if exists(Template("sanity_break.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
                touch(Template("cancel.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
                time.sleep(5)
                break
    else:
        #touch([w//2, h//2])
        touch(Template("daily_resource.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(3)
        # 2. Coin quest
        if exists(Template("coin_resource.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("coin_resource.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
            touch(Template("ce_5.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
            for i in range(130//30):
                touch(Template("start_action.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
                time.sleep(3)
                touch(Template("start_action_2.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
                time.sleep(150)
                wait(Template("finish_action.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
                touch(Template("finish_action.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
                time.sleep(5)
                if exists(Template("sanity_break.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
                    touch(Template("cancel.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
                    time.sleep(5)
                    break
        # 3. Exp quest
        elif exists(Template("exp_resource.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("exp_resource.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
            touch(Template("ls_5.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
            for i in range(130//30):
                touch(Template("start_action.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
                time.sleep(3)
                touch(Template("start_action_2.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
                time.sleep(150)
                wait(Template("finish_action.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
                touch(Template("finish_action.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
                time.sleep(5)
                if exists(Template("sanity_break.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
                    touch(Template("cancel.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
                    time.sleep(5)
                    break
    # Back to home page
    touch(Template("back.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template("back.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template("back.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)

def source_center():
    # Source Center
    touch(Template("source_center.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template("exchange.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template("harvest.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template("resource_rewards.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)
    # Back to home page
    touch(Template("back.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)

def change_member(room, coordinate):
    x, y = coordinate[0], coordinate[1]
    if not (x == 0 and y == 0):
        click([x, y])
        time.sleep(5)
    
    # member count = cycle * 2
    room_cycle = {}
    room_cycle["center"] = 5
    room_cycle["trade"] = 2
    room_cycle["manufacture"] = 2
    room_cycle["dormitory"] = 5
    room_cycle["meeting"] = 2
    room_cycle["office"] = 1
    
    cycle = room_cycle[room]

    if not exists(Template("release.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
        touch(Template("member_info.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(3)
    touch(Template("release.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)
    if exists(Template("ensure.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
        touch(Template("ensure.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
        time.sleep(3)
    touch(Template("member.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)
    if cycle >= 1:
        click([735,295])
        time.sleep(1)
    if cycle >= 2:
        click([735,695])
        time.sleep(1)
    if cycle >= 3:
        click([945,295])
        time.sleep(1)
    if cycle >= 4:
        click([945,695])
        time.sleep(1)
    if cycle >= 5:
        click([1175,295])
        time.sleep(1)
    touch(Template("confirm.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)
    if room == "dormitory":
        if exists(Template("confirm_2.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080))):
            touch(Template("confirm_2.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
            time.sleep(3)
    touch(Template("back.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(5)

def infrastructure():
    # Infrastructure
    touch(Template("infrastructure.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(7)
    touch(Template("notification.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template("exp_ore.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template("coin.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template("trust.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)
    touch(Template("to_do.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(3)
    # Center
    touch(Template("center.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(5)
    change_member("center", [0, 0])
    # Trading - A
    change_member("trade", [100, 460])
    # Trading - B
    change_member("trade", [415, 460])
    # Manufacturing - A
    change_member("manufacture", [730, 460])
    # Manufacturing - B
    change_member("manufacture", [100, 780])
    # Manufacturing - C
    change_member("manufacture", [415, 780])
    # Manufacturing - D
    change_member("manufacture", [730, 780])
    # Dormitory - A
    change_member("dormitory", [1075, 460])
    # Dormitory - B
    change_member("dormitory", [1235, 620])
    # Dormitory - C
    change_member("dormitory", [1075, 780])
    # Dormitory - D
    change_member("dormitory", [1235, 940])
    # Meeting
    change_member("meeting", [1840, 300])
    # Office
    change_member("office", [1890, 615])
    # Back to home page
    touch(Template("back.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(5)

def mission_complete():
    # Mission
    touch(Template("mission.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(5)
    touch(Template("receive.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    time.sleep(1)
    #touch(Template("back.png", record_pos=(-0.001, 0.115), resolution=(1920, 1080)))
    #time.sleep(5)

def main():
    # Get resolution
    w,h = device().get_current_resolution()

    start_game()
    source_center()
    infrastructure()
    sanity()
    mission_complete()
    
if __name__ == '__main__':
    main()
