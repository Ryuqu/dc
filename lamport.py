import csv

clocks = {}
message = {}

with open("lamport.csv", "r", newline="") as file:
    for row in csv.DictReader(file):
        process = row["process_id"]
        action = row["event_type"].strip().lower()
        target = row["message_to"].strip()
        clocks.setdefault(process, int(row["initial_clock"]))

        if action == "recieve" :
            messsage_time = message.get(process, 0)
            clocks[process] = max(clocks[process], messsage_time) + 1
        else :
            clocks[process] += 1

        print("Event", row["event_id"], process, action)

        if action == "send":
            message[target] = clocks[process]