
total = 0
average = 0
count  = 0

minimum = 100000000000000000000000000000000000000000000000000000000000000000000000
maximum = -99999999999999999999999999999999999999999999999999999999999999999999999

while True:
    num = int(input("Enter the number or -999 to stop: "))

    if num == -999:
        break
    
    total += num
    count += 1

    if num <= minimum:
        minimum = num

    if num >= maximum:
        maximum = num
    


average = total / count
print(f"The average is: {average:.2f}")
print(f"The maximum number is: {maximum}")
print(f"The minimum number is: {minimum}")
print(f"The Total is: {total}")