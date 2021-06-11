from builtins import map

nest = [
    [11, 12, 13, [23, 355, 67, 67]],
    [14, 15, 16, [34, 456, 5657, 7]],
    [17, 18, 19, [34545, 45, 23, 78]],
]


# ci = 0
# cj = 0
# ck = 0
# if ci < len(nest):
#     for i in range(0, len(nest)):
#         ci += 1
#     if cj < len(nest[i]):
#         for j in range(0, len(nest[i])):
#             cj += 1
#         if ck < len(nest[i][j]):
#             for k in range(0, len(nest[i][j])):
#                 ck += 1
#                 print(nest[i][j])
#                 data.append(nest[i][j][k])

# for i, val_outer in enumerate(nest):
#   for j, val_inner in enumerate(nest[val_outer]):
#     for k, val_innermost in enumerate(nest[val_outer][val_inner]):
#       print(k)

# data = []
# for i,val in enumerate(nest):
#   data.append(val[len(nest)])
#   # print(val[len(nest)])

# print(data)

# finalData = [ element for subMatrix in data for element in subMatrix ]
# print(finalData)


# def getFinalMatrix(matrix):
#   data = []
#   for i,val in enumerate(nest):
#     data.append(val[len(nest)]


# for k in range(0, len(nest[i][j])):
# data.append(nest[i][j][k])
# for i in range(0,10):
#   for j in range(0, i):
#     print('x', end="")
#   print('')

def get_final_matrix(matrix):
    data = []
    for i, val in enumerate(matrix):
        data.append(val[len(matrix)])
    return [el for subMat in data for el in subMat]


print(get_final_matrix(nest))
