sum_squares = 0
square_sum = 0
for i in range(1,101):
    sum_squares += i**2
    square_sum += i

square_sum = square_sum ** 2

print("Diffrence:", abs(square_sum-sum_squares))
