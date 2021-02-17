

class Job:
    def __init__(self, start, end, profit):
        self.start = start
        self.end = end
        self.profit = profit
        
# -------------------------------------------------------


# NOTE: SOLUTION - 1 ( RECURSION )

# TC : O( N * 2^N)
# n for finding latest non conflicting job and 2 options for every position(include or exclude)

def latest_non_conflicting_job(arr, end):
    for i in reversed(range(end)):
        if arr[i].end <= arr[end].start:
            return i
    
    return -1


def max_profit_recursive(arr, n):

    if n < 0:
        return 0

    if n == 0:
        return arr[0].profit

    index = latest_non_conflicting_job(arr, n)

    profit_if_included = arr[n].profit + max_profit_recursive(arr, index)
    profit_if_excluded = max_profit_recursive(arr, n - 1)

    return max(profit_if_included, profit_if_excluded)


if __name__ == '__main__':
    jobs = [
        Job(0, 6, 60), Job(1, 4, 30), Job(3, 5, 10),
        Job(5, 7, 30), Job(5, 9, 50), Job(7, 8, 10)
    ]

    jobs.sort(key=lambda x: x.end)

    print(max_profit_recursive(jobs, len(jobs) - 1))



# --------------------------------------------------------------------------



# NOTE: TC : (N ^ 2) 

# N for every index and n for finding non conflicting job

def latest_non_conflicting_job_2(arr, end):
    for i in reversed(range(end)):
        if arr[i].end <= arr[end].start:
            return i
    
    return -1


def max_profit_dp(arr, n):
    
    arr.sort(key = lambda x: x.end)
    max_profit = [0] * len(arr)
    max_profit[0] = arr[0].profit

    for i in range(1, len(arr)):
        index = latest_non_conflicting_job_2(arr, i)

        profit_if_included = arr[i].profit

        if index != -1:
            profit_if_included += max_profit[index]

        max_profit[i] = max( profit_if_included, max_profit[i - 1] )

    return max_profit[-1]


if __name__ == '__main__':
    jobs = [
        Job(0, 6, 60), Job(1, 4, 30), Job(3, 5, 10),
        Job(5, 7, 30), Job(5, 9, 50), Job(7, 8, 10)
    ]

    jobs.sort(key=lambda x: x.end)

    print(max_profit_dp(jobs, len(jobs) - 1))



# ----------------------------------------------------------------------



# NOTE:  TC : O(N LOG(N))

# n for the for loop and log(n) for finding non-conflicting job

def latest_non_conflicting_job_3(arr, end):
    low, high = 0, end - 1
    ans = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid].end <= arr[end].start:
            ans = mid
            low = mid + 1
        
        else:
            high = mid - 1

    return ans


def max_profit_logn(arr, n):

    arr.sort(key=lambda x: x.end)

    max_profit = [0] * len(arr)
    max_profit[0] = arr[0].profit

    for i in range(1, len(arr)):
        index = latest_non_conflicting_job_3(arr, i)

        profit_if_included = arr[i].profit

        if index != -1:
            profit_if_included += max_profit[index]

        max_profit[i] = max( profit_if_included, max_profit[i - 1] )

    return max_profit[-1]


if __name__ == '__main__':
    jobs = [
        Job(0, 6, 60), Job(1, 4, 30), Job(3, 5, 10),
        Job(5, 7, 30), Job(5, 9, 50), Job(7, 8, 10)
    ]

    jobs.sort(key=lambda x: x.end)

    print(max_profit_logn(jobs, len(jobs) - 1))

