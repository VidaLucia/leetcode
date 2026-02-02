nums = [1,2,6,7,8]
nums.sort()
print(nums)

largest =0 
count = 0
prev = "" 
nums.sort() 
if len(nums) > 1: # Empty or one value arrays 
    
    for i in nums: # If we are at start prev = "" we want to start counting 
        if prev=="": 
            count+=1 
            prev = i # We also want to then check if prev == i-1 (1, (2-1)) would suggest consecutive 
        elif prev==(i-1): 
            count +=1 
            prev = i 
        elif prev == i: 
            continue # If not equal that means we are going from 1 to something like 3 
        else: 
            if largest < count: # 123 67 so need to check 
                largest=count 
            count = 1 
            prev = i 
    if largest < count: 
        print(count) 
print (largest)