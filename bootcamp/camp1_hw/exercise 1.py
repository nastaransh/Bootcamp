def first_exercise(L):
    L_copy = L[:]
    ind = []
    for i in range(len(L) - 2):
        if L_copy[i + 1] > L_copy[i] and L_copy[i + 1] > L_copy[i + 2] and L_copy[i] != L[i]:
            L_copy[i] = L_copy[i + 1]
            ind.append(i)
        if L_copy[i + 1] > L_copy[i] and L_copy[i + 1] > L_copy[i + 2] and L_copy[i] == L[i]:
            L_copy[i + 2] = L_copy[i + 1]
            ind.append(i + 2)
    for i in range(len(ind) - 2):
        if ind[i] == ind[i + 1]:
            ind.remove(ind[i])
    return len(ind), L_copy


L = [1, 2, 1, 3, 2, 3, 1, 2, 1]
print(first_exercise(L))
