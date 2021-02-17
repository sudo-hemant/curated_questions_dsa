
def search( pat, txt):

    if len(txt) < len(pat):
        return []
    
    pattern = [0] * 26
    text = [0] * 26
    curr = len(pat)
    count = 0
        
    for i in range(len(pat)):
        pattern[ord(pat[i]) - ord('a')] += 1
        text[ord(txt[i]) - ord('a')] += 1
        
    while curr < len(txt):
        if is_anagram(text, pattern):
            count += 1
        
        text[ord(txt[curr - len(pat)]) - ord('a')] -= 1
        text[ord(txt[curr]) - ord('a')] += 1
        
        curr += 1
    
    if is_anagram(text, pattern):
        count += 1
    
    return count
    
    
def is_anagram( text, pattern):
    for i in range(26):
        if text[i] != pattern[i]:
            return False
    return True


print(search( "for", "forxxorfxdofr"))