n=int(input())  # n 시 59분 59초까지.. (n<=23)

count =0

for hour in range(n+1):
    for minute in range(60):
        for second in range(60):
            if "3" in str(hour)+str(minute)+str(second):
                count+=1
print(count)




