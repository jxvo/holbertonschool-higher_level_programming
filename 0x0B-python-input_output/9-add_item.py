#!/usr/bin/python3
import json, os
from sys import argv

save_json = __import__("7-save_to_json_file").save_to_json_file
load_json = __import__("8-load_from_json_file").load_from_json_file

filename = "add_item.json"
json_obj = []

if os.path.isfile(filename) is True:
    json_obj = load_json(filename)

for arg in argv[1:]:
    json_obj.append(arg)
save_json(json_obj, filename)
