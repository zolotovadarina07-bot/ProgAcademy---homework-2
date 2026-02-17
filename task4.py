side_a = int(input('Input side A: '))
side_b = int(input('Input side B: '))
side_c = int(input('Input side C: '))
if side_a + side_b > side_c and side_b + side_c > side_a and side_c + side_a > side_b:
    print('Yes')
else:
    print('No')