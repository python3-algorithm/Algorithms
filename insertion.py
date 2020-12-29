# 算法2.2 插入排序


def insertion(arr: list):
    """
    与选择排序一样，当前索引左边的所有元素都是有序的，但它们的最终位置还不确定，为了给
    更小的元素腾出空间，它们可能会被移动。但是当索引到达数组的右端时，数组排序就完成了。
    """
    # 从1到最右索引，排序完成
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and current < arr[j]:
            # 当前item右移一位
            arr[j + 1] = arr[j]
            # 当前索引往左遍历
            j -= 1
        # 插入
        arr[j + 1] = current


if __name__ == "__main__":
    a = [12, 11, 13, 5, 6]
    insertion(a)
    print("排序后的数组")
    for i in range(len(a)):
        print(a[i])
