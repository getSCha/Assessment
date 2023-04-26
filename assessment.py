import json

def twoSum(nums, target): 
    indices = {}
    for i, num in enumerate(nums):
        key = target - num 
        if key in indices:
            return indices[key]+i
        indices[num] = i
    return -1
    
#O(n)
#[1,2,3,4] target = 5
i=0
num = 1
key = 5-1 = 4
{1:0}
i=1
num = 2
key = 3
{1:0,2:1}
i=2
num = 3
key = 2
return 1 + 2
 

lst_str = input("Enter List : ")
lst = [float(x) for x in json.loads(lst_str)]
tar = float(input("Enter Target : "))
ans = twoSum(lst, tar)
if ans == -1:
    print("No element in the list")
else:
    print("answer is " + str(ans))