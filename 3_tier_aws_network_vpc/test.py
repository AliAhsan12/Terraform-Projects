# def bin_search(arr, n):
#     s = 0
#     e = len(arr)-1
#     while(s<=e):
#         mid = (s+e)//2
#         if(arr[mid] < n):
#             s = mid+1
#         elif(arr[mid] > n):
#             e = mid -1
#         elif(arr[mid] == n):
#             print("found at :",mid+1)
#             break
#         else:
#             print("not found")


# bin_search([1,2,3,45,60], 45)

def sec_largest(arr):
    max1 = arr[0]
    max2 = arr[1]
    for i in range(0, len(arr)):
        if(arr[i] >= max2):
            max2 = arr[i]
            if(max2 > max1):
                temp = max1
                max1 = max2
                max2 = temp
               
            
    print(max2," ",max1)

sec_largest([2,3,16,9,2])
            
        

