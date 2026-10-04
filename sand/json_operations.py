import json

with open('new_json1.json', 'r') as new_f:
    objs = json.load(new_f)
for sec, com in objs.items():
    print(f'sec = {sec}')
    print(f'com = {com}')
    print()
print(f'1-------')


with open('new_json1.json', 'r') as new_f:
    new_f_content = new_f.read()
    objs = json.loads(new_f_content)

for sec, com in objs.items():
    print(f'sec = {sec}')
    print(f'com = {com}')
    print()

print(f'2-------')





data = {
  "action": "msg",
  "time": 11111111,
  "to": "account_name",
  "from": "account_name",
  "encoding": "ascii",
  "message": "message"
}


with open('new_json2.json', 'w') as new_f:
    new_f.write(json.dumps(data))

with open('new_json2.json', 'r') as new_f:
    print(new_f.read())


data3 = {
  "action3": "msg",
  "time3": 11111111,
  "to3": "account_name",
  "from3": "account_name",
  "encoding3": "ascii",
  "message3": "message"
}

with open('new_json3.json', 'w') as new_f:
    json.dump(data3, new_f)

with open('new_json3.json') as new_f:
    print(new_f.read())

number = 4
data4 = {
  "action": "msg",
  "time": 11111111,
  "to": "account_name",
  "from": "account_name",
  "encoding": "ascii",
  "message": "message"
}

data4 = {k+str(number):v for k,v in data4.items()}

print(data4)


with open('new_json4.json', 'w') as new_f:
    json.dump(data4, new_f, sort_keys=True, indent=2)

with open('new_json4.json', 'r') as new_f:
    print(new_f.read())
