# 算法2.1 选择排序


def selection(A: list):
    """
    选择排序
    (N-1)+(N-2)+...+2+1=N(N-1)/2 ~N^2/2 次比较
    N 次交换

    数据移动是最少的。每次交换都会改变两个数组元素的值，因此选择排序用了 N 次交换——交
    换次数和数组的大小是线性关系。我们将研究的其他任何算法都不具备这个特征(大部分的增长数
    量级都是线性对数（NlogN）或是平方级别)。

    线性对数成长的比线性函数 N 快，但比平方函数 n^2 慢。
    """

    for i in range(len(A)):
        min_index = i
        # 第一次循环 把最小项放到第一个item
        for j in range(i + 1, len(A)):
            # range(start, stop[, step])
            if A[min_index] > A[j]:
                min_index = j

        A[i], A[min_index] = A[min_index], A[i]


if __name__ == "__main__":
    A = [1, 3, 4, 5, 4, 5]
    selection(A)
    print("排序后的数组：")
    # python 传引用类型
    for i in range(len(A)):
        print(A[i])
