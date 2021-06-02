import json
import os
import re

# The property name responsible for saving average number of steps between random encounters
es = 'encounterStep'

directory = './data/'
files = []

for filename in os.listdir(directory):
    pattern = r'Map[0-9]{3}.json$'
    if re.match(pattern, filename):
        files.append(os.path.join(directory, filename))

# https://stackoverflow.com/questions/21035762/python-read-json-file-and-modify
for path in files:
    f = open(path, 'r+', encoding="utf-8")
    data = json.load(f)
    data[es] = 999
    f.seek(0)
    json.dump(data, f, ensure_ascii=False)
    f.close()