matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# def displayMatrix(mat):
#     for row in mat:
#         for item in row:
#             print(item, end=" ")
#         print()

# displayMatrix(matrix)



lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def printMatrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[j][i], end=" ")
        print()  # New line after each row

printMatrix(lst)


# Flatening

def flatening(matrix,newLst):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            newLst.append(matrix[i][j])
            
    return newLst

newLst=[]

ans=flatening(lst,newLst)
print(ans)



lst=[]
for i in range(1,11):
    lst.append(i)
print(lst)

del lst[2]
del lst[4]
del lst[6]

print(lst)
lst.insert(5,99)
print(lst)


def reversal(lst):
    return lst[::-1]

print(reversal(lst))
# lst1=['a','b','v','c']

# print(list(zip(lst,lst1)))


lst=[1,2,3,4,5]

def rotate(lst,m):
    return lst[m:]+lst[:m]
    
print(rotate(lst,2))


lst=[1,2,3,4,5]
lst1=[2,3,4,8,0]

def intersection(lst,lst1,ans):
    for x in lst:
        if x in lst1:
            ans.append(x)
            
    return ans
    
ans=[]       
print(intersection(lst,lst1,ans))


from package.math import addition,muliplay

print(addition(4,5))
print(muliplay(4,5))