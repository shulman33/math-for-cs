import sys

set_one = set()

with open(sys.argv[1], 'r') as f:
    contents = f.readlines()

left_side = contents[0]
right_side = contents[1]

for content in left_side:
    if content.isupper():
        set_one.add(content)

for content in right_side:
    if content.isupper():
        set_one.add(content)

list_var = list(set_one)
left_to_right = 0
right_to_left = 0
equal = 0
length = len(set_one)
counter = 2 ** length
dict = {}

for n in range(counter):
    for i in list_var:
        if i == 'T':
            dict[i] = 1
        elif i == 'F':
            dict[i] = 0
        else:
            dict[i] = (n // 2**list_var.index(i)) % 2
    l_val = eval(left_side,dict)
    r_val = eval(right_side,dict)
    if l_val == r_val:
        left_to_right += 1
        right_to_left += 1
        equal += 1
    if l_val and not r_val:
        right_to_left +=1
    if not l_val and r_val:
        left_to_right += 1
if equal == counter:
    print("EQUIVALENT")
elif left_to_right == counter:
    print("LEFT implies RIGHT")
elif right_to_left == counter:
    print("RIGHT implies LEFT")
else:
    print("NO IMPLICATION")