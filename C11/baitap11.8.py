nums = [2,6,7,9]
def has_lucky_number(nums):
    flag = False
    for i in range(len(nums)):
        if nums[i]%7==0:
            flag = True
    return flag
print(has_lucky_number(nums))