def even_odd(num):
    if 1 <= num <= 50:
        if num % 2 == 0:
            return "Even on West side"
        else:
            return "Odd on East side"
    elif 51 <= num <= 100:
        if num % 2 == 0:
            return "Even on North side"
        else:
            return "Odd on South side"

results = []

for i in range (3):
    try:
        nums = int(input("Enter 3 house numbers: "))
        answer = even_odd(nums)
        results.append(answer)
    except ValueError:
        print("Not a valid number")
        
print("\n".join(results))
        

