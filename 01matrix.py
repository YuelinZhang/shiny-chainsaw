def bfs(matrix,nums):
    if not nums:
        return
    temp = []
    for k in range(len(nums)):
        [i,j] = nums[k]
        print([i,j])
        if i-1>=0 and matrix[i-1][j] =="*":
            matrix[i-1][j] = matrix[i][j]+1
            temp.append([i-1,j])
        if i+1<=len(matrix)-1 and matrix[i+1][j]=="*":
            matrix[i+1][j] = matrix[i][j]+1
            temp.append([i+1,j])
        if j-1>=0 and matrix[i][j-1]=="*":
            matrix[i][j-1] = matrix[i][j]+1
            temp.append([i,j-1])
        if j+1<=len(matrix[0])-1 and matrix[i][j+1] == "*":
            matrix[i][j+1] = matrix[i][j]+1
            temp.append([i,j+1])
    nums = temp
    bfs(matrix,nums)

matrix = [[0],[0],[0],[0],[0]]
nums = []
copy = [["*"]*len(matrix[0]) for i in range(len(matrix))]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
       if matrix[i][j] == 0:
            copy[i][j] = 0
            nums.append([i,j])

bfs(copy,nums)
print(copy)
