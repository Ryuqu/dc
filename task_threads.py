import csv
import threading

completed = 0
lock = threading.Lock()

def process_task(row):
    global completed
    print(threading.current_thread().name, "processing", row["task_id"], "burst: ", row["burst_ms"], " ms")
    with lock:
        completed += 1

with open("threading.csv", "r" ,newline="") as file:
    tasks = list(csv.DictReader(file))

threads = []
for task in tasks:
    t = threading.Thread(target=process_task, args=(task, ), name=task["thread_name"])

    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Total Completed tasks: ", completed)
