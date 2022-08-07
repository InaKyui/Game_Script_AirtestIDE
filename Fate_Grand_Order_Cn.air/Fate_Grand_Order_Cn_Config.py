# Encoding utf8
# Python 3.7.7
# Update in 2022/8/7
# Author by Yui_Roma

import os
import json

config = {}

# Recoding resolution
config["resolution"] = [1920, 1080]

# Coordinate information
# First: [1](110,870);[2](245,870);[3](375,870)
# Second:[1](890,870);[2](720,870);[3](850,870)
# Third: [1](1065,870);[2](1195,870);[3](1330,870)
# Hero:  [Main](1790,480)
#        [1](1360,470);[2](1495,470);[3](1630,870)
# Skill: [1](475,690);[2](960,690);[3](1420,690)
# Coordinate Initial
coordinate = {}
coordinate["first"] = {}
coordinate["first"]["skill1"] = [110,870]
coordinate["first"]["skill2"] = [245,870]
coordinate["first"]["skill3"] = [375,870]
coordinate["second"] = {}
coordinate["second"]["skill1"] = [590,870]
coordinate["second"]["skill2"] = [720,870]
coordinate["second"]["skill3"] = [850,870]
coordinate["third"] = {}
coordinate["third"]["skill1"] = [1065,870]
coordinate["third"]["skill2"] = [1195,870]
coordinate["third"]["skill3"] = [1330,870]
coordinate["hero"] = {}
coordinate["hero"]["main"] = [1790,480]
coordinate["hero"]["skill1"] = [1360,470]
coordinate["hero"]["skill2"] = [1495,470]
coordinate["hero"]["skill3"] = [1630,470]
coordinate["skill"] = {}
coordinate["skill"]["target1"] = [475,690]
coordinate["skill"]["target2"] = [960,690]
coordinate["skill"]["target3"] = [1420,690]
coordinate["attack"] = {}
coordinate["attack"]["main"] = [1700,910]
coordinate["attack"]["master1"] = [620,250]
coordinate["attack"]["master2"] = [960,250]
coordinate["attack"]["master3"] = [1290,250]
coordinate["attack"]["card1"] = [195,750]
coordinate["attack"]["card2"] = [580,750]
coordinate["scroll"] = {}
coordinate["scroll"]["start"] = [1885,495]
coordinate["scroll"]["interval"] = [0,85]
config["coordinate"] = coordinate

# Save config
with open("Fate_Grand_Order_Cn_Config.json", mode='wt', encoding='utf-8') as file_obj:
    json_str = json.dumps(config, indent=4)
    file_obj.write(json_str)
