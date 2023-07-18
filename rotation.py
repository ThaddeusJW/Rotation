import json

path = "C:/Users/Thaddeus/Coding/VS Code/Rotation_Checker/showTVData.json"
f = open(path, 'r')
rotation_json = json.load(f)

rotation_str = json.dumps(rotation_json, indent=2)
print(rotation_str)