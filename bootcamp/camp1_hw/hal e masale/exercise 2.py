def exercise_two(num):
    a = str(num)
    result = []
    for i in range(len(a)-1):
        add_num = str(int(a[i]) + int(a[i+1]))
        res = int(a.replace(a[i:i+2], add_num))
        result.append(res)
    return max(result)


print(exercise_two(10038))