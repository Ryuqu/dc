import csv

with open("load.csv", "r", newline="") as file:
    jobs = list(csv.DictReader(file))

servers = ["Server1", "Server2", "Server3"]

for i , job in enumerate(jobs):
    print(job["job_id"], "assigned to ", servers[i % len(servers)])

print("\n Least-Connected Scheduling")
connections = [0,0,0]
for job in jobs:
    min_index = 0
    for i in range (1, len(servers)):
        if connections[i] < connections[min_index]:
            min_index = i
    print(job["job_id"], "assigned to", servers[min_index])
    connections[min_index] += 1
print("Final connections: ",connections)
