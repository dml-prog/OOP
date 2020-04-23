pos = 0

def lin(nums,n):
    i=0
    while i<len(nums):
        if nums[i]==n:
            globals()['pos'] =i
            return True
        i+=1
    return False

nums =[11,5,2,6,8,9,7]
n=8
if lin(nums,n):
    print("found",pos+1)
else:
    print("not found")
