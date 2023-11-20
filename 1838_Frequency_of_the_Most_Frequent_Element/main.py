IN = list(map(int, input("Enter list : ").split()))
k = int(input("Enter k : "))
diff = [], count = 1
for i in range(0, len(IN) - 1):
    diff.append(abs(IN[i + 1] - IN[i]))
diff = sorted(diff, reverse = True) # sort list diff max to min
# print(diff)
while(True):
    x = diff.pop()
    if k > x:
        count += 1
        k -= x
    if k == 0 or len(diff) == 0 or k < x:
        break
print(count)