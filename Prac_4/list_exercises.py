# # this function will ask the user to input 5 numbers and will then add them to a variable called numbers.
#
# numbers = []
# count = 5
# print("Input 5 numbers:")
# for count in range(1, 5 + 1):
#     users_input = input()
#     numbers.append(int(users_input))
#
# print(
#     "Number: {}\nNumber: {}\nNumber: {}\nNumber: {}\nNumber: {} ".format(numbers[0], numbers[1], numbers[2], numbers[3],
#                                                                          numbers[4]))
#
# print("The first number is {}".format(numbers[0]))
#
# print("The last number is {}".format(numbers[4]))
#
#
# small_number = min(numbers[0:5])
# print('The smallest number is: {}'.format(small_number) )
#
# large_number = max(numbers[0:5])
# print('The largest number is: {}'.format(large_number))
#
# average = sum(numbers[0:5]) / 5
# print('The average of the numbers is {}'.format(average))

# TODO: Intermediate exercise 2
count = 0
while count < 3:
 usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
 compare_name = []
 compare_name = input("Enter your username: ").lower()

 if compare_name in usernames:
    print("Access granted")
    print("Logout when done!")
 else:
    print("Access denied")
    count +=1

print("Try again after 10 minutes.")




