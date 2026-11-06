import csv

def server(method, value):
    print("[Server] Request recieved: ", method, value)
    if method == "double":
        return value * 2
    elif method == "square":
        return value * value
    else:
        return value * -1



with open("rpc.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        method = row["method_name"]
        value = row["param_value"]
        print("\n[Client]", row["client_name"], "sends call ", row["call_id"])
        result = server(method, int(value))
        print("[Client] Result: " ,result)