data = [1,3,5]
data2 = [2,7,10]
data3 = [1,2,3,4]

result = map(lambda v1,v2:v1 * v2,data,data2)
print(list(result))

result2 = map(lambda v1,v2:v1*v2,data,data3)
print(list(result2))
# listの要素数が異なるときは要素数が少ない方に合わせて動作する