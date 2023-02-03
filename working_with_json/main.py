import json

computers = [
    {
        "id": 1,
        "name": "Asus",
        "color": "black"
    },
{
        "id": 2,
        "name": "Victus",
        "color": "black"
    },
    {
        "id": 3,
        "name": "HP",
        "color": "white"
    },
    {
        "id": 4,
        "name": "Lenovo",
        "color": "red"
    }
]

json_arr = json.dumps(computers)

with open("computers.json", "w") as f:
    json.dump(computers, f, indent=4)

# print(json.loads(json_arr)[0])

with open("computers.json") as f:
    computers = json.load(f)

print(computers)





