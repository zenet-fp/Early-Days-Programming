nums = [1, 4, 7, 34, 54, 100, 64, 23]
target = 14

for x in range(len(nums)):
        if target == nums[x]:
            print(f"We have found {target}")
            print("At index:",x)
            break
        elif target not in nums:
            print(f"{target} not in list")
            break
