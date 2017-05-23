# def f(n):
#     i = 1
#     total = 0
#     while i <= len(n):
#         start = 0
#         while start + i <= len(n):
#             num = int(n[start:start+i])
#             total += num
#             start += 1
#         i += 1
#     return total % (pow(10, 9) + 7)


def better_f(n):
    dp_table = [0]*len(n)
    dp_table[0] = int(n[0])
    i = 1
    while i < len(n):
        dp_table[i] = ((i+1)*int(n[i]) + 10*dp_table[i-1]) % (pow(10, 9) + 7)
        i += 1
    return sum(dp_table) % (pow(10, 9) + 7)
n = raw_input()
print(better_f(n))
