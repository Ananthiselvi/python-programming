def list(arr):
    n = len(arr)
    print(n)
    list = [1]*n
    print(list)
    for i in range (1 , n):
        for j in range(0 , i):
            if arr[i] > arr[j] and list[i]< list[j] + 1 :
                list[i] = list[j]+1
    maximum = 0
    for i in range(n):
        maximum = max(maximum , list[i])
 
    return maximum
arr = [1,2,2,1,3]
print ("Length of list is=", list(arr))
