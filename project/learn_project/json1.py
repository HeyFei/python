import json

data = '''
{
    "name": "Jiaming",
    "phone": {
        "type": "intel",
        "number": "as"
    },
    "email": {
        "hide": "yes"
    }
}'''

input = '''
[
    {
        "id": "001",
        "x": "2",
        "name": "jiaming"
    },
    {
        "id": "002",
        "x": "3",
        "name": "xuan"
    }
]
'''

info = json.loads(data)
print('Name:', info['name'])
print('Email:', info['email']['hide'])

info = json.loads(input)
print('User count:', len(info))

for item in info:
    print('Name:', item['name'])
    print('Id:', item['id'])
    print('Attribute:', item['x'])
