# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Generate the square pattern using a while loop for rows
while row < size:
    # Use a for loop to print '*' in the row
    for _ in range(size):
        print("*", end="")  # Print '*' without moving to a new line
    print()  # Move to the next line after completing one row
    row += 1
