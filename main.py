user_list = []
length = int(input("Enter the length of the list: "))

for i in range(length):
    element = int(input(f"Enter element {i+1}: "))
    user_list.append(element)

total_sum = sum(user_list)
average = total_sum / length

print(f"List: {user_list}")
print(f"Sum of elements: {total_sum}")
print(f"Average: {average}")
