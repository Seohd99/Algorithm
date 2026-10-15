def solution(nums):
    half = len(nums) // 2
    answer = len(set(nums))
    answer = answer if half > answer else half

    return answer