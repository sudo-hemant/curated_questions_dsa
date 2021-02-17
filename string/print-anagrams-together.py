
from collections import defaultdict

# NOTE: let size of words is N and each word is max k 
# so tc ll be O(N*K*LOG(K))

def anagrams(words):

    dict = defaultdict(list)
    ans = []

    for word in words:
        dict[tuple(sorted(word))].append(word)
    
    for values in dict.values():
        ans.append(values)
    
    return ans


print(anagrams(
    ["cat", "dog", "tac", "god", "act"]
))
    

# -------------------------------------------------------------------


# NOTE: tc : O( N * K )

def anagrams_2(words):

    dict = defaultdict(list)

    for word in words:
        count = [0] * 26

        for char in word:
            count[ord(char) - ord('a')] += 1
        
        dict[tuple(count)].append(word)

    return dict.values()


print(anagrams_2(
    ["cat", "dog", "tac", "god", "act"]
))