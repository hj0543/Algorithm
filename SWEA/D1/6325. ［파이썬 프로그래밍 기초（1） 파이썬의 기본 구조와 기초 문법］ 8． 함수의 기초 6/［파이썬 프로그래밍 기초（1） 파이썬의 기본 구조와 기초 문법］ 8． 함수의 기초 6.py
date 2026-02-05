nums = [2, 4, 6, 8, 10]
print(nums)
def search(x):
    if x in nums:
        return True
    else:
        return False

for i in (5, 10):
    search(i)
    print(f'{i} => {search(i)}')