import csv

nodes = {}

with open("ring.csv", "r", newline="") as file:
    for row in csv.DictReader(file):
        node = int(row["node_id"])
        nodes[node] = {
            "next" : int(row["next_node_id"]),
            "active" : row["is_active"].strip().lower() == "true",
            "rank" : int(row["priority_rank"])
        }

initiator = 2
current = initiator
visited = set()
participants = []
print("Election started by node", initiator)

while current not in visited:
    visited.add(current)
    if nodes[current]["active"]:
        participants.append(current)
        print("Active Node Participants: ", current)
    current = nodes[current]["next"]

if participants:
    leader = max(participants, key= lambda n : nodes[n]["rank"])
    print("New leader Elected: ", leader)
else:
    print("No active Node")