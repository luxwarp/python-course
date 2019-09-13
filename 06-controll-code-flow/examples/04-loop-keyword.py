#!/usr/bin/env python3

# When dealing with loops in python
# sometimes you might want to stop the loop
# or skip one loop run if some condition is met.


# break
# By using break you can exit the closest loop.

# Exit a for loop if a the character is "a".

name = "Luxwarp"

for letter in name:
    if letter == 'a':
        break

    print(letter)

# note that "arp" is not printed out.

# continue
# By using continue you can jump over the rest of the loop and
# start from top with the next item.

# Don't print number 2

numbers = [1, 1, 2, 3, 4, 2, 5, 6]

for number in numbers:
    if number == 2:
        continue

    print(number)

# pass
# By using pass you can create a loop without
# any content, which normally would create an indentation error.

for number in numbers:
    # Let's fill this up later, or never.
    pass
