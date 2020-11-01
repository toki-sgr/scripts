data = [[1, 5], [5, 2], [4.3, 6.4], [7, 1], [8, 6.6]]
data_with_result = []
for d in data:
    res = round(d[0] * 7.3 + d[1] * 4.4)
    data_with_result.append([d[0], d[1], int(res)])
print(data_with_result)