a = int(input())
b = int(input())
def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)
print(sum(a, b))