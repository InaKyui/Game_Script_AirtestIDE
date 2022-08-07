import os
import json

# Profile Information
profile = {}

# [Setting] Start
setting = {}

# [Adb_path]
# Tips: The first and last quotation marks are required
# "C:\Program Files\MuMu\emulator\nemu\vmonitor\bin\adb_server.exe"
# "C:\Program Files (x86)\MuMu\emulator\nemu\vmonitor\bin\adb_server.exe"
setting["adb_path"] = r"F:\LDPlayer\LDPlayer4.0\adb.exe"
setting["package_name"] = "com.bilibili.priconne"
setting["activity_name"] = "com.bilibili.permission.PermissionActivity"

# [Resolution]
# Tips: Aspect ratio must be 16:9
resolution = {}
resolution["x"] = 1920
resolution["y"] = 1080
resolution["dpi"] = 280

setting["resolution"] = resolution

# [Task]
task = {}

initial_task = []
initial_task.append("initial")
task["initial_task"] = initial_task

start_task = []
start_task.append("game_start")
start_task.append("receive_energy")
task["start_task"] = start_task

random_task = []
random_task.append("shopping")
random_task.append("mission_guild")
random_task.append("mission_gashapon")
random_task.append("mission_explore")
random_task.append("mission_dungeons")
random_task.append("mission_arena")
random_task.append("mission_princess_arena")
task["random_task"] = random_task

end_task = []
end_task.append("mission_complete")
end_task.append("mission_quest")
task["end_task"] = end_task

setting["task"] = task
# [Setting] Finish

# [Coordinate] Start
total_coordinate = {}

# [Game_Start]
coordinate_dic = {}

coordinate = {}
coordinate["x"] = 0
coordinate["y"] = 0
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 10
coordinate["action"] = "click"
coordinate_dic["blank_button"] = coordinate

total_coordinate["initial"] = coordinate_dic

# [Game_Start]
coordinate_dic = {}

coordinate = {}
coordinate["x"] = 20
coordinate["y"] = 135
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 10
coordinate["action"] = "click"
coordinate_dic["blank_button"] = coordinate

coordinate = {}
coordinate["x"] = 1215
coordinate["y"] = 50
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 15
coordinate["action"] = "click"
coordinate_dic["skip_button"] = coordinate

coordinate = {}
coordinate["x"] = 640
coordinate["y"] = 640
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["close_button"] = coordinate

total_coordinate["game_start"] = coordinate_dic

# [Receive_Energy]
coordinate_dic = {}

coordinate = {}
coordinate["x"] = 830
coordinate["y"] = 685
coordinate["error_x"] = 20
coordinate["error_y"] = 15
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["home_button"] = coordinate

coordinate = {}
coordinate["x"] = 1200
coordinate["y"] = 565
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["receive_button"] = coordinate

coordinate = {}
coordinate["x"] = 60
coordinate["y"] = 40
coordinate["error_x"] = 10
coordinate["error_y"] = 10
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["blank_button"] = coordinate

total_coordinate["receive_energy"] = coordinate_dic

# [Shopping]
coordinate_dic = {}

coordinate = {}
coordinate["x"] = 120
coordinate["y"] = 685
coordinate["error_x"] = 20
coordinate["error_y"] = 10
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["main_button"] = coordinate

coordinate = {}
coordinate["x"] = 820
coordinate["y"] = 575
coordinate["error_x"] = 10
coordinate["error_y"] = 10
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["shop_button"] = coordinate

coordinate = {}
coordinate["x"] = 515
coordinate["y"] = 200
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 1
coordinate["action"] = "click"
coordinate_dic["first_cargo"] = coordinate

coordinate = {}
coordinate["x"] = 745
coordinate["y"] = 200
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 1
coordinate["action"] = "click"
coordinate_dic["second_cargo"] = coordinate

coordinate = {}
coordinate["x"] = 970
coordinate["y"] = 200
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 1
coordinate["action"] = "click"
coordinate_dic["third_cargo"] = coordinate

coordinate = {}
coordinate["x"] = 1200
coordinate["y"] = 200
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 1
coordinate["action"] = "click"
coordinate_dic["fourth_cargo"] = coordinate

coordinate = {}
coordinate["x"] = 1050
coordinate["y"] = 585
coordinate["error_x"] = 100
coordinate["error_y"] = 5
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["buy_button"] = coordinate

coordinate = {}
coordinate["x"] = 785
coordinate["y"] = 635
coordinate["error_x"] = 50
coordinate["error_y"] = 10
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["ok_button"] = coordinate

coordinate = {}
coordinate["x"] = 185
coordinate["y"] = 210
coordinate["error_x"] = 10
coordinate["error_y"] = 10
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["blank_button"] = coordinate

total_coordinate["shopping"] = coordinate_dic

# [Mussion_Guild]
coordinate_dic = {}

coordinate = {}
coordinate["x"] = 120
coordinate["y"] = 685
coordinate["error_x"] = 20
coordinate["error_y"] = 15
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["main_button"] = coordinate

coordinate = {}
coordinate["x"] = 920
coordinate["y"] = 575
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["guild_button"] = coordinate

coordinate = {}
coordinate["x"] = 60
coordinate["y"] = 140
coordinate["error_x"] = 10
coordinate["error_y"] = 10
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["blank_button"] = coordinate

coordinate = {}
coordinate["x"] = 315
coordinate["y"] = 465
coordinate["error_x"] = 15
coordinate["error_y"] = 5
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["friend_button"] = coordinate

coordinate = {}
coordinate["x"] = 1100
coordinate["y"] = 420
coordinate["error_x"] = 10
coordinate["error_y"] = 5
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["like_button"] = coordinate

total_coordinate["mission_guild"] = coordinate_dic

# [Mission_Gashapon]
coordinate_dic = {}

coordinate = {}
coordinate["x"] = 1000
coordinate["y"] = 685
coordinate["error_x"] = 20
coordinate["error_y"] = 15
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["gashapon_button"] = coordinate

coordinate = {}
coordinate["x"] = 60
coordinate["y"] = 140
coordinate["error_x"] = 10
coordinate["error_y"] = 10
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["blank_button"] = coordinate

coordinate = {}
coordinate["x"] = 1195
coordinate["y"] = 100
coordinate["error_x"] = 10
coordinate["error_y"] = 5
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["normal_button"] = coordinate

coordinate = {}
coordinate["x"] = 960
coordinate["y"] = 460
coordinate["error_x"] = 30
coordinate["error_y"] = 10
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["free_button"] = coordinate

coordinate = {}
coordinate["x"] = 785
coordinate["y"] = 490
coordinate["error_x"] = 15
coordinate["error_y"] = 5
coordinate["idle_time"] = 10
coordinate["action"] = "click"
coordinate_dic["ok_button"] = coordinate

coordinate = {}
coordinate["x"] = 640
coordinate["y"] = 590
coordinate["error_x"] = 15
coordinate["error_y"] = 5
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["receive_button"] = coordinate

total_coordinate["mission_gashapon"] = coordinate_dic

# [Mission_Explore]
coordinate_dic = {}

coordinate = {}
coordinate["x"] = 640
coordinate["y"] = 685
coordinate["error_x"] = 20
coordinate["error_y"] = 15
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["adventure_button"] = coordinate

coordinate = {}
coordinate["x"] = 980
coordinate["y"] = 185
coordinate["error_x"] = 15
coordinate["error_y"] = 15
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["explore_button"] = coordinate

coordinate = {}
coordinate["x"] = 780
coordinate["y"] = 320
coordinate["error_x"] = 15
coordinate["error_y"] = 15
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["exp_button"] = coordinate

#coordinate = {}
#coordinate["x"] = 1075
#coordinate["y"] = 320
#coordinate["error_x"] = 15
#coordinate["error_y"] = 15
#coordinate["idle_time"] = 5
#coordinate["action"] = "click"
#coordinate_dic["mana_button"] = coordinate

coordinate = {}
coordinate["x"] = 960
coordinate["y"] = 200
coordinate["error_x"] = 20
coordinate["error_y"] = 10
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["level_button"] = coordinate

#coordinate = {}
#coordinate["x"] = 1170
#coordinate["y"] = 440
#coordinate["error_x"] = 5
#coordinate["error_y"] = 5
#coordinate["idle_time"] = 1
#coordinate["action"] = "click"
#coordinate_dic["add_button"] = coordinate

coordinate = {}
coordinate["x"] = 1010
coordinate["y"] = 440
coordinate["error_x"] = 15
coordinate["error_y"] = 5
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["attack_button"] = coordinate

coordinate = {}
coordinate["x"] = 785
coordinate["y"] = 490
coordinate["error_x"] = 15
coordinate["error_y"] = 5
coordinate["idle_time"] = 7
coordinate["action"] = "click"
coordinate_dic["ok_button"] = coordinate

coordinate = {}
coordinate["x"] = 60
coordinate["y"] = 140
coordinate["error_x"] = 10
coordinate["error_y"] = 10
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["blank_button"] = coordinate

total_coordinate["mission_explore"] = coordinate_dic

# [Mission_Dungeons]
coordinate_dic = {}

coordinate = {}
coordinate["x"] = 640
coordinate["y"] = 685
coordinate["error_x"] = 20
coordinate["error_y"] = 15
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["adventure_button"] = coordinate

coordinate = {}
coordinate["x"] = 1170
coordinate["y"] = 185
coordinate["error_x"] = 15
coordinate["error_y"] = 15
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["dungeons_button"] = coordinate

coordinate = {}
coordinate["x"] = 1105
coordinate["y"] = 325
coordinate["error_x"] = 30
coordinate["error_y"] = 30
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["last_extreme_button"] = coordinate

coordinate = {}
coordinate["x"] = 785
coordinate["y"] = 575
coordinate["error_x"] = 15
coordinate["error_y"] = 15
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["ok_button"] = coordinate

coordinate = {}
coordinate["x"] = 905
coordinate["y"] = 360
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["first_enemy"] = coordinate

coordinate = {}
coordinate["x"] = 635
coordinate["y"] = 345
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["second_enemy"] = coordinate

coordinate = {}
coordinate["x"] = 295
coordinate["y"] = 325
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["third_enemy"] = coordinate

coordinate = {}
coordinate["x"] = 655
coordinate["y"] = 335
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["fourth_enemy"] = coordinate

coordinate = {}
coordinate["x"] = 1120
coordinate["y"] = 610
coordinate["error_x"] = 15
coordinate["error_y"] = 10
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["challenge_button"] = coordinate

coordinate = {}
coordinate["x"] = 1150
coordinate["y"] = 120
coordinate["error_x"] = 15
coordinate["error_y"] = 5
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["my_team_button"] = coordinate

coordinate = {}
coordinate["x"] = 1055
coordinate["y"] = 275
coordinate["error_x"] = 30
coordinate["error_y"] = 5
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["call_button"] = coordinate

coordinate = {}
coordinate["x"] = 1115
coordinate["y"] = 605
coordinate["error_x"] = 15
coordinate["error_y"] = 10
coordinate["idle_time"] = 35
coordinate["action"] = "click"
coordinate_dic["attack_button"] = coordinate

coordinate = {}
coordinate["x"] = 1110
coordinate["y"] = 655
coordinate["error_x"] = 30
coordinate["error_y"] = 5
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["next_button"] = coordinate

coordinate = {}
coordinate["x"] = 60
coordinate["y"] = 140
coordinate["error_x"] = 10
coordinate["error_y"] = 10
coordinate["idle_time"] = 7
coordinate["action"] = "click"
coordinate_dic["blank_button"] = coordinate

coordinate = {}
coordinate["x"] = 1085
coordinate["y"] = 570
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 3 
coordinate["action"] = "click"
coordinate_dic["retreat_button"] = coordinate

coordinate = {}
coordinate["x"] = 785
coordinate["y"] = 495
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 3 
coordinate["action"] = "click"
coordinate_dic["comfirm_button"] = coordinate

total_coordinate["mission_dungeons"] = coordinate_dic

# [Mission_Arena]
coordinate_dic = {}

coordinate = {}
coordinate["x"] = 640
coordinate["y"] = 685
coordinate["error_x"] = 20
coordinate["error_y"] = 15
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["adventure_button"] = coordinate

coordinate = {}
coordinate["x"] = 775
coordinate["y"] = 540
coordinate["error_x"] = 50
coordinate["error_y"] = 20
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["arena_button"] = coordinate

coordinate = {}
coordinate["x"] = 60
coordinate["y"] = 140
coordinate["error_x"] = 10
coordinate["error_y"] = 10
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["blank_button"] = coordinate

coordinate = {}
coordinate["x"] = 395
coordinate["y"] = 455
coordinate["error_x"] = 10
coordinate["error_y"] = 10
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["receive_button"] = coordinate

coordinate = {}
coordinate["x"] = 805
coordinate["y"] = 235
coordinate["error_x"] = 10
coordinate["error_y"] = 10
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["first_person"] = coordinate

coordinate = {}
coordinate["x"] = 1115
coordinate["y"] = 600
coordinate["error_x"] = 30
coordinate["error_y"] = 10
coordinate["idle_time"] = 7
coordinate["action"] = "click"
coordinate_dic["attack_button"] = coordinate

coordinate = {}
coordinate["x"] = 1220
coordinate["y"] = 475
coordinate["error_x"] = 10
coordinate["error_y"] = 10
coordinate["idle_time"] = 7
coordinate["action"] = "click"
coordinate_dic["skip_button"] = coordinate

coordinate = {}
coordinate["x"] = 1110
coordinate["y"] = 655
coordinate["error_x"] = 30
coordinate["error_y"] = 10
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["next_button"] = coordinate

total_coordinate["mission_arena"] = coordinate_dic

# [Mission_Princess_Arena]
coordinate_dic = {}

coordinate = {}
coordinate["x"] = 640
coordinate["y"] = 685
coordinate["error_x"] = 20
coordinate["error_y"] = 15
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["adventure_button"] = coordinate

coordinate = {}
coordinate["x"] = 1100
coordinate["y"] = 540
coordinate["error_x"] = 50
coordinate["error_y"] = 20
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["princess_arena_button"] = coordinate

coordinate = {}
coordinate["x"] = 60
coordinate["y"] = 140
coordinate["error_x"] = 10
coordinate["error_y"] = 10
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["blank_button"] = coordinate

coordinate = {}
coordinate["x"] = 395
coordinate["y"] = 455
coordinate["error_x"] = 10
coordinate["error_y"] = 10
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["receive_button"] = coordinate

coordinate = {}
coordinate["x"] = 805
coordinate["y"] = 235
coordinate["error_x"] = 10
coordinate["error_y"] = 10
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["first_person"] = coordinate

coordinate = {}
coordinate["x"] = 1115
coordinate["y"] = 600
coordinate["error_x"] = 30
coordinate["error_y"] = 10
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["next_team_button"] = coordinate

coordinate = {}
coordinate["x"] = 1115
coordinate["y"] = 600
coordinate["error_x"] = 30
coordinate["error_y"] = 10
coordinate["idle_time"] = 10
coordinate["action"] = "click"
coordinate_dic["attack_button"] = coordinate

coordinate = {}
coordinate["x"] = 1220
coordinate["y"] = 475
coordinate["error_x"] = 10
coordinate["error_y"] = 10
coordinate["idle_time"] = 10
coordinate["action"] = "click"
coordinate_dic["skip_button"] = coordinate

coordinate = {}
coordinate["x"] = 1075
coordinate["y"] = 655
coordinate["error_x"] = 30
coordinate["error_y"] = 10
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["next_button"] = coordinate

total_coordinate["mission_princess_arena"] = coordinate_dic

# [Mission_Complete]
coordinate_dic = {}

coordinate = {}
coordinate["x"] = 120
coordinate["y"] = 685
coordinate["error_x"] = 20
coordinate["error_y"] = 15
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["main_button"] = coordinate

coordinate = {}
coordinate["x"] = 1115  
coordinate["y"] = 575
coordinate["error_x"] = 10
coordinate["error_y"] = 10
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["mission_button"] = coordinate

coordinate = {}
coordinate["x"] = 1125
coordinate["y"] = 585
coordinate["error_x"] = 100
coordinate["error_y"] = 15
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["receive_button"] = coordinate

coordinate = {}
coordinate["x"] = 60
coordinate["y"] = 140
coordinate["error_x"] = 10
coordinate["error_y"] = 10
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["blank_button"] = coordinate

total_coordinate["mission_complete"] = coordinate_dic

# [Mussion_Quest]
coordinate_dic = {}

coordinate = {}
coordinate["x"] = 640
coordinate["y"] = 685
coordinate["error_x"] = 20
coordinate["error_y"] = 15
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["adventure_button"] = coordinate

coordinate = {}
coordinate["x"] = 550
coordinate["y"] = 565
coordinate["error_x"] = 10
coordinate["error_y"] = 10
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["quest_button"] = coordinate

coordinate = {}
coordinate["x"] = 5
coordinate["y"] = 100
coordinate["error_x"] = 3
coordinate["error_y"] = 3
coordinate["idle_time"] = 10
coordinate["action"] = "click"
coordinate_dic["blank_button"] = coordinate

coordinate = {}
coordinate["x"] = 100
coordinate["y"] = 100
coordinate["error_x"] = 3
coordinate["error_y"] = 3
coordinate["idle_time"] = 10
coordinate["action"] = "click"
coordinate_dic["sec_blank_button"] = coordinate

coordinate = {}
coordinate["x"] = 740
coordinate["y"] = 105
coordinate["error_x"] = 1
coordinate["error_y"] = 1
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["map_button"] = coordinate

coordinate = {}
coordinate["x"] = 155
coordinate["y"] = 470
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["first_button"] = coordinate

coordinate = {}
coordinate["x"] = 1240
coordinate["y"] = 330
coordinate["error_x"] = 1
coordinate["error_y"] = 1
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["change_button"] = coordinate

coordinate = {}
coordinate["x"] = 1155
coordinate["y"] = 350
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["boss_button"] = coordinate

coordinate = {}
coordinate["x"] = 1170
coordinate["y"] = 440
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 1
coordinate["action"] = "click"
coordinate_dic["add_button"] = coordinate

coordinate = {}
coordinate["x"] = 1010
coordinate["y"] = 445
coordinate["error_x"] = 3
coordinate["error_y"] = 3
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["sweep_button"] = coordinate

coordinate = {}
coordinate["x"] = 785
coordinate["y"] = 495
coordinate["error_x"] = 3
coordinate["error_y"] = 3
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["ok_button"] = coordinate

coordinate = {}
coordinate["x"] = 890
coordinate["y"] = 605
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["cancel_button"] = coordinate

coordinate = {}
coordinate["x"] = 1120
coordinate["y"] = 620
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["challenge_button"] = coordinate

coordinate = {}
coordinate["x"] = 1115
coordinate["y"] = 605
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 100
coordinate["action"] = "click"
coordinate_dic["attack_button"] = coordinate

coordinate = {}
coordinate["x"] = 1080
coordinate["y"] = 655
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 5
coordinate["action"] = "click"
coordinate_dic["next_button"] = coordinate

coordinate = {}
coordinate["x"] = 1215
coordinate["y"] = 570
coordinate["error_x"] = 1
coordinate["error_y"] = 1
coordinate["idle_time"] = 3
coordinate["action"] = "click"
coordinate_dic["quest_mission_button"] = coordinate

coordinate = {}
coordinate["x"] = 1125
coordinate["y"] = 585
coordinate["error_x"] = 5
coordinate["error_y"] = 5
coordinate["idle_time"] = 1
coordinate["action"] = "click"
coordinate_dic["complete_button"] = coordinate

total_coordinate["mission_quest"] = coordinate_dic

for tk in total_coordinate.keys():
    for tkk in total_coordinate[tk].keys():
        total_coordinate[tk][tkk]["x"] = round(total_coordinate[tk][tkk]["x"] / 1280, 4)
        total_coordinate[tk][tkk]["y"] = round(total_coordinate[tk][tkk]["y"] / 720, 4)
# print(total_coordinate)
# [Coordinate] Finish


# [Step] Start
total_step = {}

# [Initial]
step = []
step.append("blank_button")

total_step["initial"] = step

# [Game_Start]
step = []
step.append("blank_button")
step.append("blank_button")
step.append("blank_button")
step.append("blank_button")
step.append("blank_button")
step.append("skip_button")
step.append("close_button")
step.append("blank_button")

total_step["game_start"] = step

# [Receive_Energy]
step = []
step.append("home_button")
step.append("receive_button")
step.append("blank_button")

total_step["receive_energy"] = step

# [Shopping]
step = []
step.append("main_button")
step.append("shop_button")
step.append("first_cargo")
step.append("second_cargo")
step.append("third_cargo")
step.append("fourth_cargo")
step.append("buy_button")
step.append("ok_button")
step.append("blank_button")

total_step["shopping"] = step

# [Mission_Guild]
step = []
step.append("main_button")
step.append("guild_button")
step.append("blank_button")
step.append("friend_button")
step.append("like_button")
step.append("blank_button")

total_step["mission_guild"] = step

# [Mission_Gashapon]
step = []
step.append("gashapon_button")
step.append("blank_button")
step.append("normal_button")
step.append("free_button")
step.append("ok_button")
step.append("receive_button")

total_step["mission_gashapon"] = step

# [Mission_Explore]
step = []
step.append("adventure_button")
step.append("explore_button")
step.append("exp_button")
step.append("level_button")
#step.append("add_button")
step.append("attack_button")
step.append("ok_button")
step.append("blank_button")
#step.append("mana_button")
step.append("level_button")
#step.append("add_button")
step.append("attack_button")
step.append("ok_button")
step.append("blank_button")

total_step["mission_explore"] = step

# [Mission_Dungeons]
step = []
step.append("adventure_button")
step.append("dungeons_button")
step.append("last_extreme_button")
step.append("ok_button")
step.append("first_enemy")
step.append("challenge_button")
step.append("my_team_button")
step.append("call_button")
step.append("attack_button")
step.append("next_button")
step.append("blank_button")

step.append("second_enemy")
step.append("challenge_button")
step.append("attack_button")
step.append("next_button")
step.append("blank_button")

step.append("third_enemy")
step.append("challenge_button")
step.append("attack_button")
step.append("next_button")
step.append("blank_button")

step.append("fourth_enemy")
step.append("challenge_button")
step.append("attack_button")
step.append("next_button")
step.append("blank_button")

step.append("retreat_button")
step.append("comfirm_button")

total_step["mission_dungeons"] = step

# [Mission_Arena]
step = []
step.append("adventure_button")
step.append("arena_button")
step.append("blank_button")
step.append("receive_button")
step.append("blank_button")
step.append("first_person")
step.append("attack_button")
step.append("skip_button")
step.append("next_button")
step.append("blank_button")
step.append("blank_button")

total_step["mission_arena"] = step

# [Mission_Princess_Arena]
step = []
step.append("adventure_button")
step.append("princess_arena_button")
step.append("blank_button")
step.append("receive_button")
step.append("blank_button")
step.append("first_person")
step.append("next_team_button")
step.append("next_team_button")
step.append("attack_button")
step.append("skip_button")
step.append("next_button")
step.append("blank_button")
step.append("blank_button")

total_step["mission_princess_arena"] = step

# [Mission_Quest]
step = []
step.append("adventure_button")
step.append("quest_button")
step.append("blank_button")
step.append("blank_button")
step.append("blank_button")
step.append("blank_button")
step.append("blank_button")
step.append("blank_button")
step.append("blank_button")
# Prevent dialogue & do not to overlap with level buttons
step.append("map_button")

step.append("first_button")
step.append("add_button")
step.append("add_button")
step.append("sweep_button")
step.append("ok_button")
step.append("sec_blank_button")
step.append("sec_blank_button")
step.append("change_button")

step.append("add_button")
step.append("add_button")
step.append("sweep_button")
step.append("ok_button")
step.append("sec_blank_button")
step.append("sec_blank_button")
step.append("change_button")

step.append("add_button")
step.append("add_button")
step.append("sweep_button")
step.append("ok_button")
step.append("sec_blank_button")
step.append("sec_blank_button")
step.append("change_button")

step.append("add_button")
step.append("add_button")
step.append("sweep_button")
step.append("ok_button")
step.append("sec_blank_button")
step.append("sec_blank_button")
step.append("change_button")

step.append("add_button")
step.append("add_button")
step.append("sweep_button")
step.append("ok_button")
step.append("sec_blank_button")
step.append("sec_blank_button")
step.append("cancel_button")

step.append("boss_button")
step.append("challenge_button")
step.append("attack_button")
step.append("next_button")
step.append("next_button")
step.append("blank_button")
step.append("blank_button")
step.append("blank_button")
step.append("blank_button")
step.append("blank_button")
step.append("quest_mission_button")
step.append("complete_button")

total_step["mission_quest"] = step

# [Mission_Complete]
step = []
step.append("main_button")
step.append("mission_button")
step.append("receive_button")
step.append("blank_button")

total_step["mission_complete"] = step

# [Step] Finish
profile["setting"] = setting
profile["coordinate"] = total_coordinate
profile["step"] = total_step


with open(os.path.join(os.getcwd(), "profile.json"), mode='wt', encoding='utf-8') as file_obj:
    json_str = json.dumps(profile, indent=4)
    file_obj.write(json_str)
