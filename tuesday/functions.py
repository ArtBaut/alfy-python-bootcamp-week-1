def input_list_helper():
    flag = True
    nums = []
    while flag:
        user_in = input("\t")
        if user_in == "":
            flag = False
            continue
        nums.append(int(user_in))
    print("Temp print", nums)
    return nums


def input_list(nums):
    total = 0
    for i in range(len(nums)):
        total = total + nums[i]
    nums.append(total)
    print("list plus total", nums)


def check_monotonic_sequence(seq):
    up = False
    up_s = False
    down = False
    down_s = False
    column = len(seq) - 1
    row = 4
    # initialize list with 4 lists inside that have custom cell size
    rows, cols = (row, column)
    ls = [[False for j in range(cols)] for i in range(rows)]
    # check monotonocity of each number in sequence
    for i in range(len(seq) - 1):
        # print(seq[i],seq[i+1])
        if seq[i] <= seq[i + 1]:
            ls[0][i] = True
        if seq[i] < seq[i + 1]:
            ls[1][i] = True
        if seq[i] >= seq[i + 1]:
            ls[2][i] = True
        if seq[i] > seq[i + 1]:
            ls[3][i] = True
    # combine all results
    mon = [up, up_s, down, down_s]
    for row in range(len(ls)):
        if False in ls[row]:
            mon[row] = False
        else:
            mon[row] = True
    
    return mon


def check_monotonic_sequence_inverse(def_bool):
    match def_bool:
        case [True, False, False, False]:
            return [1, 2, 2, 3]
        case [True, True, False, False]:
            return [1, 2, 3, 4]
        case [False, False, True, False]:
            return [3, 2, 1, 1]
        case [False, False, True, True]:
            return [7.5, 4, 3.14, 0.11]
        case [False, False, False, False]:
            return [1, 0, -1, 1]
        case [True, True, True, True]:
            return [100]
        case [True, False, True, False]:
            return [1, 1, 1, 1]
        case _:
            return None


def primes_generator(end):
    count = 0
    pp = 2  # possible prime
    nonprimes = []
    primes = []
    while count < end:
        for i in range(2, int(pp / 2) + 1):
            if (pp % i) == 0:
                nonprimes.append(pp)
                break
        else:
            primes.append(pp)
            count = count + 1
        pp = pp + 1
    return primes


def is_empty_vector(vec_list):
    for i in range(len(vec_list)):
        if vec_list[i] == None:
            return True
        else:
            return False


def vectors_list_sum(vec_list):
    if is_empty_vector(vec_list):
        print("empty vector! use another vector list")
        return 0
    elif all(len(vec_list[0]) == len(l) for l in vec_list[1:]):
        #
        sum = []
        for j in range(len(vec_list[0])):
            x = 0
            for i in range(len(vec_list)):
                x = x + vec_list[i][j]
            sum.append(x)
    return sum


def calc_the_inner_product(vec_1, vec_2):
    sum = 0
    if len(vec_1) == len(vec_2):
        for i in range(len(vec_1)):
            sum = sum + vec_1[i] * vec_2[i]
        return sum
    else:
        return None


def remove_duplicates(alist):
    # removes duplicate pairs in a list
    auxlist = []
    for i in range(len(alist)):
        if alist[i] not in auxlist:
            auxlist.append(alist[i])
    return auxlist



def orthogonal_number(vectors):
    count = 0
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            inner_product = calc_the_inner_product(vectors[i], vectors[j])
            if inner_product == 0:
                count += 1
    
    return count
