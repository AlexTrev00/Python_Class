lista=[1,2,3,4,5]
M = [[2,4,6,8],[3,6,9,12],[4,8,12,16]]

i=0
for i in range(len(lista)):
    print(lista[i])

print("-----------------------")

for i in range(len(M)):
    print(M[i])
print("------------------------")

for i in range(len(M)):
    for j in range(len(M)):
        print(f"{M[i][j]} = {M[j]} ")