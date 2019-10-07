# Zhengwei Zhong
# zhz361
# 11234272


def matrix():
    """
    Enter a number of level of matrix
    :return: a list of list which contains a matrix
    """
    number = input('Enter number：')
    empty_list = []
    for i in range(int(number)):
        x = input('Enter number for each row: ')
        x = x.split()
        empty_list.append(x)
    return empty_list


def check_row(matrix):
    """

    :param matrix: the matrix you want to test
    :return: whether each row has an unique number
    """
    sl = []
    for j in range(int(len(matrix))):
        sl.append(str(j+1))
    new_list = []
    for i in matrix:
        q = sorted(i)
        new_list.append(q)
    for x in new_list:
        if x != sl:
            print("no")
            return False

    print("Yes")
    return True


def check_column(matrix):
    """

    :param matrix: the matrix you want to test
    :return: whether each column has an unique number
    """
    sl = []
    for j in range(int(len(matrix))):
        sl.append(str(j + 1))
    for i in range(0, int(len(matrix))):
        a = [x[i] for x in matrix]
        h = sorted(a)
        if h != sl:
            print('no')
            return False
        else:
            print('Yes')
            return True


def latin_square():
    """

    :return: whether this row is a latin square or not
    """
    list_matrix = matrix()
    a = check_column(list_matrix)
    b = check_row(list_matrix)
    if a == True and b == True:
        print('Yes, this is a latin square')
        return True
    else:
        print('No, this is not a latin square')
        return False


print(latin_square())

