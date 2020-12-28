# 算法2.1 选择排序


A = [1, 3, 4, 5, 4, 5]


def selection(A):
    """
    docstring
    """
    pass


for i in range(len(A)):
    min_index = i
    # 第一次循环 把最小项放到第一个item
    for j in range(i + 1, len(A)):
        # range(start, stop[, step])
        if A[min_index] > A[j]:
            min_index = j

    A[i], A[min_index] = A[min_index], A[i]

if __name__ == "__main__":
    selection(A)
    print("排序后的数组：")
    # python 传引用类型
    for i in range(len(A)):
        print(A[i])
