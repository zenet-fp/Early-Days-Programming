nums = [9,34, 45, 1, 98, 67, 54, 92, 476, 35, 67]
#accednig order

def main():
        for x in range(len(nums) - 1):
            for i in range(len(nums) - 1 - x):
                while True:
                    if nums[i] > nums[i + 1]:
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    break

if __name__ == '__main__':
    main()
    print(nums)
