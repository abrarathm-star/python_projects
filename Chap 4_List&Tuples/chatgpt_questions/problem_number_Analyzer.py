numbers=[]

for i in range(6):
    # input(f"Number{i+1}: ")
    numbers.append(int(input(f"Number{i+1}: ")))
print()
numbers.sort()
print()
print(numbers)
print()
print(sum(numbers))
print()
print(max(numbers))
print()
print(min(numbers))
print()
print(round(sum(numbers)/len(numbers),4))
print()