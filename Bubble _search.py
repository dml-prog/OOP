pos = -1

def search(list,n):
    l =0
    u =len(list)-1
    while l<=u:
        mid = l+u //2
        if list[mid] ==n:
            globals()['pos']=mid
            return True
        elif list[mid]>n:
            u = mid-1
        else:
            l= mid+1


    return False

list= [1,2,3,5,6,7]
n=7
if search(list,n):
    print("Found",pos+1)
else:
    print("Not found")