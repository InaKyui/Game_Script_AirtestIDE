import os
import json
import time
import random
import datetime
import subprocess

profile_dic = {}

def click(task, button):
    # Get coordinate infomation
    x = round(profile_dic["coordinate"][task][button]["x"] * profile_dic["setting"]["resolution"]["x"], 0)
    y = round(profile_dic["coordinate"][task][button]["y"] * profile_dic["setting"]["resolution"]["y"], 0)
    error_x = profile_dic["coordinate"][task][button]["error_x"]
    error_y = profile_dic["coordinate"][task][button]["error_y"]
    idle_time = profile_dic["coordinate"][task][button]["idle_time"]
    # Calculate actual coordinate and idle time
    actual_x = x + random.randint(-error_x, error_x)
    if actual_x < 0:
        actual_x = 0
    actual_y = y + random.randint(-error_y, error_y)
    if actual_y < 0:
        actual_y = 0
    actual_time = random.randint(idle_time * 100, idle_time * 100 + 300)
    
    # Click
    custom_print("[" + task + "]" + "[" + button + "][click] (" + str(actual_x) + ", " + str(actual_y) + ")")
    click_cmd = profile_dic["setting"]["adb_path"] + " shell input tap " + str(actual_x) + " " + str(actual_y)
    #print(click_cmd)
    obj = subprocess.Popen(click_cmd,
                      shell=True,
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE)

    # Idle
    custom_print("[" + task + "]" + "[" + button + "][idle] " + str(actual_time / 100) + " seconds")
    time.sleep(actual_time / 100)

def double_click(task, button):
    # Get coordinate infomation
    x = profile_dic["coordinate"][task][button]["x"] * profile_dic["setting"]["resolution"]["x"]
    y = profile_dic["coordinate"][task][button]["y"] * profile_dic["setting"]["resolution"]["y"]
    error_x = profile_dic["coordinate"][task][button]["error_x"]
    error_y = profile_dic["coordinate"][task][button]["error_y"]
    idle_time = profile_dic["coordinate"][task][button]["idle_time"]
    # Calculate actual coordinate and idle time
    actual_x = x + random.randint(-error_x, error_x)
    actual_y = y + random.randint(-error_y, error_y)
    actual_x2 = actual_x + random.randint(-3, 3)
    actual_y2 = actual_y + random.randint(-3, 3)
    interval_time = random.randint(5, 10)
    actual_time = random.randint(idle_time * 100, idle_time * 100 + 300)

    # Double click - 1
    custom_print("[" + task + "]" + "[" + button + "][double_click] (" + str(actual_x) + ", " + str(actual_y) + ")")
    click_cmd = profile_dic["setting"]["adb_path"] + " shell input tap " + str(actual_x) + " " + str(actual_y)    
    click_cmd2 = profile_dic["setting"]["adb_path"] + " shell input tap " + str(actual_x2) + " " + str(actual_y2)    
    subprocess.Popen(click_cmd,
                      shell=True,
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE)
    # Idle
    time.sleep(interval_time / 100)
    # Double click - 2
    subprocess.Popen(click_cmd2,
                      shell=True,
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE)

    # Idle
    custom_print("[" + task + "]" + "[" + button + "][idle] " + str(actual_time / 100) + " seconds")
    time.sleep(actual_time / 100)


def long_press_normal(task, button):
    # Get coordinate infomation
    x = profile_dic["coordinate"][task][button]["x"] * profile_dic["setting"]["resolution"]["x"]
    y = profile_dic["coordinate"][task][button]["y"] * profile_dic["setting"]["resolution"]["y"]
    error_x = profile_dic["coordinate"][task][button]["error_x"]
    error_y = profile_dic["coordinate"][task][button]["error_y"]
    idle_time = profile_dic["coordinate"][task][button]["idle_time"]
    # Calculate actual coordinate and idle time
    actual_x = x + random.randint(-error_x, error_x)
    actual_y = y + random.randint(-error_y, error_y)
    actual_time = random.randint(idle_time * 100, idle_time * 100 + 300)
    
    # Long press - normal quest
    custom_print("[" + task + "]" + "[" + button + "][long_press_normal] (" + str(actual_x) + ", " + str(actual_y) + ")")
    press_cmd = profile_dic["setting"]["adb_path"] + " shell input swipe " + str(actual_x) + " " + str(actual_y) + " " + str(actual_x) + " " + str(actual_y) + " 20000"
    subprocess.Popen(press_cmd,
                      shell=True,
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE)
    
    # Idle
    custom_print("[" + task + "]" + "[" + button + "][idle] " + str(actual_time / 100) + " seconds")
    time.sleep(actual_time / 100)


def long_press_hard(task, button):
    # Get coordinate infomation
    x = profile_dic["coordinate"][task][button]["x"] * profile_dic["setting"]["resolution"]["x"]
    y = profile_dic["coordinate"][task][button]["y"] * profile_dic["setting"]["resolution"]["y"]
    error_x = profile_dic["coordinate"][task][button]["error_x"]
    error_y = profile_dic["coordinate"][task][button]["error_y"]
    idle_time = profile_dic["coordinate"][task][button]["idle_time"]
    # Calculate actual coordinate and idle time
    actual_x = x + random.randint(-error_x, error_x)
    actual_y = y + random.randint(-error_y, error_y)
    actual_time = random.randint(idle_time * 100, idle_time * 100 + 300)
    
    # Long press - hard quest
    custom_print("[" + task + "]" + "[" + button + "][long_press_hard] (" + str(actual_x) + ", " + str(actual_y) + ")")
    press_cmd =  profile_dic["setting"]["adb_path"] + " shell input swipe " + str(actual_x) + " " + str(actual_y) + " " + str(actual_x) + " " + str(actual_y) + " 3000"
    subprocess.Popen(press_cmd,
                      shell=True,
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE)

    # Idle
    custom_print("[" + task + "]" + "[" + button + "][idle] " + str(actual_time / 100) + " seconds")
    time.sleep(actual_time / 100)

def custom_print(message):
    # Print time
    time_now = datetime.datetime.now()
    print_str = "[" + str(time_now) + "]" + message
    print(print_str)
    # Write to debug file
    with open(os.path.join(os.getcwd(), "debug_for_develop.txt"), "a") as file_obj:
        file_obj.write(print_str + "\n")

def start_server():
    # Start adb server
    while True:
        start_cmd = profile_dic["setting"]["adb_path"] + " connect 127.0.0.1:5555"
        custom_print("[Connect] " + start_cmd)
        obj = subprocess.Popen(start_cmd,
                          shell=True,   
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
        stdout = obj.stdout.read()
        stderr = obj.stderr.read()
        # Print return data (chinese -> gbk)
        try:
            return_data = stdout.decode('utf-8').splitlines()
        except:
            return_data = stdout.decode('gbk').splitlines()
        custom_print(str(return_data))
        if return_data != []:
            break
        else:
            custom_print("[Error] Please check adb")
            time.sleep(3)

def stop_server():
    # Start adb server
    while True:
        stop_cmd = "taskkill /f /im adb.exe"
        custom_print("[Connect] " + stop_cmd)
        obj = subprocess.Popen(stop_cmd,
                          shell=True,   
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
        stdout = obj.stdout.read()
        stderr = obj.stderr.read()
        stop_cmd = profile_dic["setting"]["adb_path"] + " kill-server"
        custom_print("[Connect] " + stop_cmd)
        obj = subprocess.Popen(stop_cmd,
                          shell=True,   
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
        # Print return data (chinese -> gbk)
        try:
            return_data = stdout.decode('utf-8').splitlines()
        except:
            return_data = stdout.decode('gbk').splitlines()
        custom_print(str(return_data))
        if return_data != []:
            break
        else:
            custom_print("[Error] Please check adb")
            time.sleep(3)

def start_game():
    # adb shell am start -n [package]/[activity]
    package_str = profile_dic["setting"]["package_name"] + r"/" + profile_dic["setting"]["activity_name"]
    game_cmd = profile_dic["setting"]["adb_path"] + " shell am start -n " + package_str
    custom_print("[Connect] " + game_cmd)
    obj = subprocess.Popen(game_cmd,
                      shell=True,   
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE)
    time.sleep(15)

def main():
    # Get task
    task = []
    # Initial task
    initial_task = profile_dic["setting"]["task"]["initial_task"][0]
    # Start tasks
    start_tasks = profile_dic["setting"]["task"]["start_task"]
    # Random tasks
    random_tasks = profile_dic["setting"]["task"]["random_task"]
    random.shuffle(random_tasks)
    # End tasks
    end_tasks = profile_dic["setting"]["task"]["end_task"]

    task.extend(start_tasks)
    task.extend(random_tasks)
    task.extend(end_tasks)

    # Print task
    custom_print("[Task_List] " + str(task))

    # Start adb server
    #stop_server()
    #start_server()

    # Start the game or initialize
    if "game_start" in start_tasks:
        start_game()
    else:
        task.insert(0, initial_task)

    # Perform task
    for t in task:
        # Print current task
        custom_print("[Task] " + t)
        step = profile_dic["step"][t]
        for button in step:
            # Distinguishing action
            if profile_dic["coordinate"][t][button]["action"] == "click":
                # Print current click
                custom_print("[Task] <" + profile_dic["coordinate"][t][button]["action"] + "> " + button)
                click(t, button)

    stop_server()


if __name__ == '__main__':
    # Load profile
    profile_path = os.path.join(os.getcwd(), "profile.json")
    with open(profile_path, "r") as file_obj:
        profile_dic = json.load(file_obj)
    
    main()


