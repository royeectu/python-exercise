# Write a function that takes a list of words and returns the length of the longest one


def return_longest_word(words_lst):
    longest_word = ""
    for word in words_lst:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


words = ['royee', 'may', 'yael', 'aharon']
print(return_longest_word(words))
