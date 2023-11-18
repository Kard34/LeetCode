IN = list(map(int, input("Enter list : ").split()))
k = int(input("Enter k : "))
# print(IN)
# print(k)
diff = []
for i in range(0, len(IN) - 1):
    diff.append(abs(IN[i + 1] - IN[i]))

print(diff)