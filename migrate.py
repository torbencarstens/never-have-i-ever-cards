import json


with open("tasks_de.json") as f:
    tasks = json.load(f)


new = []
for task in tasks:
    new.append({
        "text": task["text"],
        "id": task["id"]
    })


with open("tasks_de.json", "w+") as output_file:
    json.dump(new, output_file, ensure_ascii=False)
