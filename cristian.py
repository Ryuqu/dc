import csv

with open("cristian.csv", "r" ,newline="") as file:
    for row in csv.DictReader(file):
        t0 = int(row["t0_send_ms"])
        server_time = int(row["t_server_ms"])
        t1 = int(row["t1_recv_ms"])
        rtt = t1 - t0
        delay = rtt / 2
        estimated_time = server_time - delay
        print("Client:", row["client_id"])
        print("RTT:", rtt, "ms")
        print("Estimated delay:", delay, "ms")
        print("Synchronized time:", estimated_time, "ms")
        print()


