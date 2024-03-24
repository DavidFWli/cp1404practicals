numbers = [3, 1, 4, 1, 5, 9, 2]
print("The value of numbers[0] is:", numbers[0])
print("The value of numbers[-1] is:", numbers[-1])
print("The value of numbers[3] is:", numbers[3])
print("The value of numbers[:-1] is:", numbers[:-1])
print("The value of numbers[3:4] is:", numbers[3:4])
print("Is 5 in numbers?", 5 in numbers)
print("Is 7 in numbers?", 7 in numbers)
print("Is '3' in numbers?", "3" in numbers)
print("The value of numbers + [6, 5, 3] is:", numbers + [6, 5, 3])
#①
numbers[0] = "ten"
print("The updated list is:", numbers)
#②
numbers[-1] = 1
print("The updated list is:", numbers)
#③
print("All elements from numbers except the first two:", numbers[2:])
#④
print("Is 9 an element of numbers?", 9 in numbers)
