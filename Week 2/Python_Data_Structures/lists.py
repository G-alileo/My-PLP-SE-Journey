# Lists are ordered, mutable collections that can store different data types.
my_list = ["Audi", "BMW", "Mercedes", "Honda"]

#  Display the list
print("Original list:", my_list)

#  List operations
# Accessing elements (indexing, slicing)
print("First car:", my_list[0])
print("Last car:", my_list[-1])
print("Middle cars:", my_list[1:3])     

# Adding elements (append, insert, extend)
my_list.append("Toyota")
print("After appending Toyota:", my_list)

my_list.insert(1, "Lexus")
print("After inserting Lexus at index 1:", my_list)

my_list.extend(["Nissan", "Mazda"])
print("After extending with Nissan and Mazda:", my_list)

# Removing elements (remove, pop, clear)
my_list.remove("Honda")
print("After removing Honda:", my_list)

#  Searching (index, in)
print(my_list.index("BMW"))  # 2
print("Lexus" in my_list) # True

#  Sorting and reversing
my_numbers = [5,4,9,23,45,3]

print("Original List : ", my_numbers)
my_numbers.sort()
print("Sorted List : ", my_numbers)

reversed =  my_numbers.reverse()
print("Reversed List : ", my_numbers)