def sort_alphabetically(words):
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if words[i] > words[j]:
                words[i], words[j] = words[j], words[i]
    return words

user_input = input("Enter words separated by spaces: ")
words_list = user_input.split()
sorted_words = sort_alphabetically(words_list)
print("Words in alphabetical order:", ' '.join(sorted_words))
