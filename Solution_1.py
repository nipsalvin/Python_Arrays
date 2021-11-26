
def solution(A, N):
    for i in range(1, N+1):  # search for 1 to n+1 elements
        flag = False

        for j in range(N-1):  # iterating through the array
            if A[j] == i:
                flag = True
                break
        if flag == False:
            return i


A = [-2, 2, -3, 2, 10, 0]
length = len(A)
res = solution(A, length)
print(res)

#Author N¡PS

