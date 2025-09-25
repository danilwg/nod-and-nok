def s(a, b):
    while b:
        a, b = b, a % b
    return a

def o(a, b):
    return a * b // s(a, b)
    
numbers = list(map(int, input("enter numbers pls: ").split()))

s_result = numbers[0]
o_result = numbers[0]

for num in numbers[1:]:
    s_result = s(s_result, num)
    o_result = o(o_result, num)

print(f"nod: {s_result}")
print(f"nok: {o_result}")
input()