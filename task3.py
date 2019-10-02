# Write a function using dict comprehensions that takes a list of strings
# and outputs a dictionary where keys are strings and values are booleans
# that say whether the word is a palindrome or not


def detect_palindromes(strings_list):
    return {word: word == word[::-1] for word in strings_list}


assert detect_palindromes(['madam', 'joy', 'fish']) == {
    'madam': True,
    'joy': False,
    'fish': False
}

assert detect_palindromes(['print', 'mom', 'dad']) == {
    'print': False,
    'mom': True,
    'dad': True
}