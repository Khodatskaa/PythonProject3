try:
    my_list = []

    x = int(input("Enter the number of elements in the list: "))

    for _ in range(x):
        element = int(input("Enter an integer: "))
        my_list.append(element)

    number_to_find = int(input("Enter the number to find: "))

    count = 0

    for num in my_list:
        if num == number_to_find:
            count += 1

    print(f"The number {number_to_find} appears {count} times")

except Exception as e:
    print(e)
