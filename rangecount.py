def assign(numbers):
    numbers.sort()
    a=(list(set(numbers)))
    # print(a)
    cnt=1
    value=[]
    range_count=[]
    output=[]
    for i in range(len(a)):
        if i == 0:
            continue
        if(a[i]-a[i-1]==1):
            cnt=cnt+1
   #         print(cnt)
            if cnt==2:
                first = a[i-1]
                # print(first)
        else:
            if cnt >= 2:
                value.append(first)
                range_count.append(cnt)
            cnt=1
            start=''
    
    if cnt >= 2:
        value.append(first)
        range_count.append(cnt)

    # print(value)
    # print(range_count)

    output_value = max(range_count)
    output_index = range_count.index(output_value)

    # print(output_value)
    # print(output_index) 

    output_endvalue = output_value+output_index-1
    # print(output_endvalue)   

    output.append(value[output_index])
    output.append(output_endvalue)

    print(output)
            

    
    
    
# numbers=[1, 11, 3, 0, 15, 5, 5, 2, 4, 10, 7, 12, 6]  
numbers=[11, 7, 3, 4, 2, 1,5, 0]
print(assign(numbers))
