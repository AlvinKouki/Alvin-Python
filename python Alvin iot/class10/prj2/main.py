import json

d = {}
t = int(input("please enter the amount you want:"))
for i in range(t):
    print(f'number{i}')
    k = input("please enter the name")
    v = input("please enter the number")
    d[k] = v

print(d)
r = input("please enter the number you want to remove:")
d.pop(r, 'fuck you')
print(d)
json_str = json.dumps(d)
d = json.load(json_str)
print(d)