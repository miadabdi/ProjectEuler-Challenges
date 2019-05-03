largest_number = []
for a in range(999,99,-1):
    for b in range(a,99,-1):
        # Generating 2 3-digit numbers
        num = str(a * b)
        if num == num[::-1]:
            largest_number.append(int(num))

print("The largest number is:",max(largest_number))
