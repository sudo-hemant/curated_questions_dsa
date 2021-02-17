
from collections import Counter, defaultdict


def group_words(strings):

    dict = defaultdict(list)

    for word in strings:

        word_dict = Counter(word)
        key = word_dict.keys()

        key = ''.join(sorted(key))
        
        dict[key].append(word)

    for key, value in dict.items():
        print(', '.join(value))


print(group_words(
    [
        "may", "student", "students", "dog",
        "studentssess", "god", "cat", "act",
        "tab", "bat", "flow", "wolf", "lambs",
        "amy", "yam", "balms", "looped", 
        "poodle"
    ]
))