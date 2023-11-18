IN = input("matrix = ").strip("[]").split("],[")
for i in range(0, len(IN)):
    IN[i] = [int(x) for x in IN[i].split(',')]
    
print(IN)