from collections import Counter

# NOTE: very well explained in pepcoding, the solutions written in leetcode(best) 

def minWindow(self, s: str, t: str) -> str:
    
    if not s or not t:
        return ""
    
    dict_t = Counter(t)

    # all unique characters required
    required = len(dict_t)
    l, r = 0, 0

    # all unique characters with same frequency found, ll increast count by 1 each time
    formed = 0

    # curr window frequency count
    window_counts = {}

    # stores size, left and right index 
    ans = float('inf'), None, None
    
    while r < len(s):
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1
        
        # if curr char is our requrired char and at the time its frequency equals the required frequency we ll increase the count
        # not when the frequency found is either less or greater
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1
        
        # we ll start decreasing l index when we have found all characters with required frequency till all the character with 
        # required frequency are there in current window 
        while l <= r and formed == required:
            character = s[l]
            
            # store the desired output
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
                
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1
                
            l += 1
            
        r += 1
        
    return "" if ans[0] == float('inf') else s[ans[1] : ans[2] + 1]
