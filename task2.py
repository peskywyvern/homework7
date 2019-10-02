# Write a function using list comprehensions that takes a string and changes
# letter's case from upper to lower and vice versa


def change_case(string1):
    return ''.join(letter.upper()if letter.islower() else letter.lower()
                   for letter in string1)


assert change_case("HELLO") == "hello"
assert change_case("Hi! I'm Jim :)") == "hI! i'M jIM :)"
assert change_case("welcome y'all") == "WELCOME Y'ALL"
