import json
import os
import re

# https://forums.rpgmakerweb.com/index.php?threads/how-to-turn-off-random-encounters.31071/
# The property name responsible for saving average number of steps between random encounters
es = 'encounterStep'
# Responsible for saving the list of enemies to encounter
el = 'encounterList'

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

    # Empty the encounter list
    data[el] = []

    # Bigger == Rarer random encounter
    data[es] = 999
    
    f.seek(0)
    json.dump(data, f, ensure_ascii=False)
    f.close()