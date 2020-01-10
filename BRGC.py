def gray_code(n):
    if n <= 0:
        return []
    if n == 1:
        return ['0', '1']
    res = gray_code(n-1)
    return ['0'+s for s in res] + ['1'+s for s in res[::-1]]

print(gray_code(5))