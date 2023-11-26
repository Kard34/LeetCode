nums = sorted(list(map(int, input("Enter nums : ").split())))
k = int(input("Enter k : "))
mostFrequent = 0
for i in range(0, len(nums) - 1):
    x = nums[i]
    count = 1
    tempK = k
    for j in range(i + 1, len(nums)):
        diff = nums[j] - x
        if diff <= tempK:
            tempK -= diff
            count += 1
        else:
            break
    if count > mostFrequent:
        mostFrequent = count
print(mostFrequent)
        