# print("Пример 1")
count = 0
for A in [0,1]:
    for B in [0,1]:
        for C in [0,1]:
            F = (not (A or B)) and C
            if F:
                print(A, B, C, F)
                count += 1
print("F=1 встречается", count, "раз")
print("Пример 2")
count = 0
for X in [0,1]:
    for Y in [0,1]:
        for Z in [0,1]:
            F = (not (not X or not Y)) <= Z  # ¬X ∨ ¬Y → Z = ¬(¬X ∨ ¬Y) ∨ Z
            # F = (X and Y) or Z
            if F:
                print(X, Y, Z, F)
                count += 1
print("F=1 встречается", count, "раз")
print("Пример 3")
count = 0
for S1 in [0,1]:
    for S2 in [0,1]:
        for S3 in [0,1]:
            F = (S1 and (not S2)) or S3
            if F:
                print(S1, S2, S3, F)
                count += 1
print("F=1 встречается", count, "раз")
print("Пример 4")
count = 0
for X in [0,1]:
    for Y in [0,1]:
        for Z in [0,1]:
            equiv = ((not X) and Y) == (X and (not Y)) == False  # ¬X ↔ Y
            # либо написать просто: equiv = ((not X) == Y)
            equiv = ((not X) == Y)
            F = equiv or Z
            if F:
                print(X, Y, Z, F)
                count += 1
print("F=1 встречается", count, "раз")
print("Пример 5")
count = 0
for A in [0,1]:
    for B in [0,1]:
        for C in [0,1]:
            F = ((not A) or B) <= (not C)
            if F:
                print(A, B, C, F)
                count += 1
print("F=1 встречается", count, "раз")
print("Пример 6")
count = 0
for A in [0,1]:
    for B in [0,1]:
        for C in [0,1]:
            F = (not (A and B)) or C
            if F:
                print(A, B, C, F)
                count += 1
print("F=1 встречается", count, "раз")
print("Пример 7")
count = 0
for X1 in [0,1]:
    for X2 in [0,1]:
        for X3 in [0,1]:
            F = (not X1 and not X2) or (X1 and X3)
            if F:
                print(X1, X2, X3, F)
                count += 1
print("F=1 встречается", count, "раз")
print("Пример 8")
count = 0
for A in [0,1]:
    for B in [0,1]:
        for C in [0,1]:
            left = A and (not C)
            right = not (A and B)
            F = (left == right)
            if F:
                print(A, B, C, F)
                count += 1
print("F=1 встречается", count, "раз")
