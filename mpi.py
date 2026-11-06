import csv

A = []
B = []

with open("mpi.csv", "r" , newline="") as file:
    for row in csv.DictReader(file):
        A.append((int(row["col_0"]), int(row["col_1"])))
        B.append((int(row["col_2"]), int(row["col_3"])))

n = len(A)
result = []

for i in range(n):
    result_row = []
    for j in range(n):
        total = 0
        for k in range(n):
            total += A[i][k] * B[k][j]
        result_row.append(total)
    result.append(result_row)

print("Final Matrix")
for row in result:
    print(row)