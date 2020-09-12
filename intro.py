# greeting = 'Hello'
# name = 'Michael'

# message = greeting + ", " + name
# print(message)

# multi_line = '''This
# is
# how
# you
# make
# a
# multiline
# string'''

# print(multi_line)
# print(len(multi_line))  # This is the length property of the
# print(message[2])  # Index of 0 based
# print(message[0:5])  # the first number is inclusive while the second
# # You can leave off the final index and it will assume you want to go to the end of the string
# print(message[6:])

# # Some string methods
# print(message.lower())
# print(message.upper())
# # Count
# print(message.count('l'))  # count how many time a char occurs
# # Find
# print(message.find('World'))

# new_message = message.replace('World', 'Universe')

# message = message.replace('World', 'Universe')
# print(new_message)
# print(message)

greeting = 'Hello'
name = 'Michael'

# message = greeting + ', ' + name + '. Welcome!'

# message = '{}, {}. Welcome!'.format(greeting, name)
# f strings

message = f'{greeting}, {name}. Welcome!'
print(message)

message = f'{greeting.upper()} {name}'

# shows what functions are available
print(dir(name))

print(help(str))
