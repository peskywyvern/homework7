# Write a function using list comprehensions that takes a list of strings
# and removes those that contain 4 characters or less


def remove_shorts(words_list):
    return [word for word in words_list if len(word) > 4]


assert remove_shorts(['telegram', 'sport', 'call', 'football', 'jet']) \
       == ['telegram', 'sport', 'football']
assert remove_shorts(['zombie', 'vision', 'cat', 'ring', 'telescope']) \
       == ['zombie', 'vision', 'telescope']
