n = int(input("dimension: "))

print("first matrix:")
matrix1 = [list(map(int, input().split())) for _ in range(n)]

print("second matrix:")
matrix2 = [list(map(int, input().split())) for _ in range(n)]

result = [[0 for _ in range(n)] for _ in range(n)]


for i in range(n):
  for j in range(n):
    for k in range(n):
      result[i][j] += matrix1[i][k] * matrix2[k][j]

print("Resultant Matrix:")
for row in result:
  print(*(row))
