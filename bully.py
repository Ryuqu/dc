import csv

alive = []

with open("bully.csv", "r" , newline="") as file :
    for row in csv.DictReader(file):
        if row["is_alive"].strip().lower() == "true":
            alive.append(int(row["node_id"]))

initiator = 2
print("Process", initiator, "Starts Election")
for node_id in alive:
    if node_id > initiator:
        print("Election message sent to process ", node_id)
        
if alive:
    leader = max(alive)
    print("New Co-ordinator", leader)
    print("co-ordination announcement sent")
else :
    print("No active process is available")