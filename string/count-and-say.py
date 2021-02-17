
def count_and_say(n):
    
    ans = ["1"]

    if n == 1:
        return ''.join(ans)
    
    for _ in range(n - 1):
        ans = helper(ans)

    return ''.join(ans)


def helper(ans):
    
    no, count = ans[0], 1
    new_ans = []

    for i in range(1, len(ans)):
        if ans[i - 1] == ans[i]:
            count += 1
        else:
            new_ans.append(str(count))
            new_ans.append(no)
            no, count = ans[i], 1

    new_ans.append(str(count))
    new_ans.append(no)

    return new_ans



print(count_and_say( 29 ))