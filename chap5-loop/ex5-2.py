largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        inum = int(num)
        if largest is None:
            largest = inum
        if smallest is None:
            smallest = inum

        if inum > largest:
            largest = inum
        elif inum < smallest:
            smallest = inum
    except:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
