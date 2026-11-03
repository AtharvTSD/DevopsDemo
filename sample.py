 # Python program to demonstrate list operations

numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# Add an element
numbers.append(60)
print("After adding:", numbers)

# Remove an element
numbers.remove(20)
print("After removing:", numbers)

# Find maximum and minimum
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# Calculate sum
print("Sum:", sum(numbers))

# Sort list in descending order
numbers.sort(reverse=True)
print("Descending Order:", numbers)

# Additional list operations
fruits = ["Apple", "Banana", "Mango"]

fruits.append("Orange")
print("Updated fruits:", fruits)

print("Total fruits:", len(fruits))