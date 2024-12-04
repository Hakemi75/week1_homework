row = int(input("行数を入力してください:"))
col = int(input("列数を入力してください:"))

for i in range(1, col + 1):
    for j in range(1, row + 1):
        result = i * j
        print(f" {j} * {i} = {result: >2} |", end="")
    print("")
