import csv 

nodes = []

with open("berkley.csv", "r", newline="") as file:
    for row in csv.DictReader(file):
        faulty = row["is_faulty"].strip().lower() == "true"
        if not faulty:
            nodes.append((row["node_id"], float(row["clock_time_sec"])))

if nodes:
    average = sum(node[1] for node in nodes) / len(nodes)
    print("Average Clock Time: ", round(average, 2))
    for node_id, current in nodes:
        print(node_id, "Adjustment: " , round(average - current, 2), " seconds")
else:
    print("Non-Faulty Clocks not found")