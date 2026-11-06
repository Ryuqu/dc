import csv

vectors = {"P1": [0, 0], "P2": [0, 0]}
messages = {}

with open("vector.csv", "r", newline="") as file:
    for row in csv.DictReader(file):
        process = row["process_id"]
        action = row["event_action"]
        target = row["target_process"]
        index = int(process[1:]) - 1

        if action == "receive":
            message = messages.get(process, [0, 0])
            for i in range (2):
                vectors[process][i] = max(vectors[process][i], message[i])
            vectors[process][index] += 1
        else:
            vectors[process][index] += 1

        print(row["event_id"], process, action, ":", vectors[process])
        
        if action == "send" and target:
            messages[target] = vectors[process].copy()