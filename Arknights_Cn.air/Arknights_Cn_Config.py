# Encoding utf8
# Python 3.7.7
# Update in 2022/8/7
# Author by Yui_Roma

import os
import json

config = {}

# Recoding resolution
config["resolution"] = [1920, 1080]

# Coordinate Initial
coordinate = {}
coordinate["room"] = {}
coordinate["room"]["center"] = [0, 0]
coordinate["room"]["trade_a"] = [100, 460]
coordinate["room"]["trade_b"] = [415, 460]
coordinate["room"]["manufacture_a"] = [730, 460]
coordinate["room"]["manufacture_b"] = [100, 780]
coordinate["room"]["manufacture_c"] = [415, 780]
coordinate["room"]["manufacture_d"] = [730, 780]
coordinate["room"]["dormitory_a"] = [1075, 460]
coordinate["room"]["dormitory_b"] = [1235, 620]
coordinate["room"]["dormitory_c"] = [1075, 780]
coordinate["room"]["dormitory_d"] = [1235, 940]
coordinate["room"]["meeting"] = [1840, 300]
coordinate["room"]["office"] = [1890, 615]
coordinate["member"] = {}
coordinate["member"]["first"] = [735,295]
coordinate["member"]["second"] = [735,695]
coordinate["member"]["third"] = [945,295]
coordinate["member"]["fourth"] = [945,695]
coordinate["member"]["fifth"] = [1175,295]
config["coordinate"] = coordinate

member_count = {}
member_count["center"] = 5
member_count["trade_a"] = 3
member_count["trade_b"] = 3
member_count["manufacture_a"] = 2
member_count["manufacture_b"] = 2
member_count["manufacture_c"] = 2
member_count["manufacture_d"] = 2
member_count["dormitory_a"] = 5
member_count["dormitory_b"] = 5
member_count["dormitory_c"] = 5
member_count["dormitory_d"] = 5
member_count["meeting"] = 2
member_count["office"] = 1
config["member_count"] = member_count

# Save config
with open("Arknights_Cn_Config.json", mode='wt', encoding='utf-8') as file_obj:
    json_str = json.dumps(config, indent=4)
    file_obj.write(json_str)
