def print_hollow_diamond(n):
    # Upper part of the hollow diamond
    for i in range(1, n + 1, 2):
        spaces_inside = i - 2
        if i == 1:
            print(" " * ((n - i) // 2) + "*")
        else:
            print(" " * ((n - i) // 2) + "*" + " " * spaces_inside + "*")

    # Lower part of the hollow diamond
    for i in range(n - 2, 0, -2):
        spaces_inside = i - 2
        if i == 1:
            print(" " * ((n - i) // 2) + "*")
        else:
            print(" " * ((n - i) // 2) + "*" + " " * spaces_inside + "*")

# Set the size of the diamond (must be an odd number)
n = int(input("Enter an odd number for diamond size: "))
if n % 2 == 0:
    print("Please enter an odd number.")
else:
    print_hollow_diamond(n)