code = '???'
check = 0
z = code.find('0')
o = code.find('1')
initial = init_e = init_b = min(int(z), int(o))
if z == o == -1:
    code = '1' + code[initial + 2:]
    init_b = init_e = 0
while init_b > -1:
    if code[init_b] == '?':
        code = code[:init_b] + str(abs(int(code[init_b + 1]) - 1)) + code[init_b + 1:]
        init_b -= 1
    else:
        init_b -= 1

while init_e < (len(code)):
    if code[init_e] == '?':
        code = code[:init_e] + str(abs(int(code[init_e - 1]) - 1)) + code[init_e + 1:]
        init_e += 1
    else:
        init_e += 1

for i in range(len(code) - 1):
    if code[i] == code[i + 1]:
        check = 1
if check == 1:
    print('is not a well defined function')
if check == 0:
    print('well defined function')
print(code)
