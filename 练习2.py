Exercise 2: Write another program that prompts for a list of numbers as above and at tbeend prints out both the maximum and minimum of the numbers instead of the venage.

imax = 0
imin = 0
nums = []

while True:
    num = input("please input a number:")
    if num == 'done':
        break;
    else:
        try:
            num = float(num)
            nums.append(num)
        except:
            print("Invalid input!")

for i in nums:
    imax = int(max(nums))
    imin = int(min(nums))
print(imax)
print(imin)