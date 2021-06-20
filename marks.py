input = [1,8,6,2,5,4,8,3,7]

maks1=0
maks2=0
water=0
maks_water=0
count1=0

for i in input: # First loop for the first point
    maks1=i
    count1+=1
    count2=0  # To begin the second loop, count2 must be reset
    for j in input:  # Second loop for the second point
        maks2=j
        count2+=1
        if maks1 <= maks2:  # For not to slant, we must find the lowest point
            water=(count2-count1)*maks1
        else:
            water=(count2-count1)*maks2
        
        if water > maks_water:  # Assigning bigger area to the result
            maks_water=water

print(maks_water)