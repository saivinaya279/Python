accounts = [[1,2,3],[3,2,1]]
max_sum=0
for num in accounts:
    sum_1=0
    for i in num:
        sum_1+=i
        if sum_1>max_sum:
            max_sum=sum_1
print(max_sum)