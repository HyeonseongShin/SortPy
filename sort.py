
def merge_sort(input_list):
    if(len(input_list) <= 1):
        return input_list

    mid_idx = int(len(input_list)/2)

    left_list = merge_sort(input_list[:mid_idx])
    right_list = merge_sort(input_list[mid_idx:])

    rtn_list = []

    while len(left_list) > 0 or len(right_list) > 0:
        if len(left_list) <= 0:
            rtn_list.extend(right_list)
            break
        elif len(right_list) <= 0:
            rtn_list.extend(left_list)
            break

        left_value = left_list[0]
        right_value = right_list[0]
        if left_value < right_value:
            rtn_list.append(left_value)
            left_list = left_list[1:]
        else:
            rtn_list.append(right_value)
            right_list = right_list[1:]

    return rtn_list

def quick_sort(input_list):
    pass

def bubble_sort(input_list):
    pass

def selection_sort(input_list):
    pass

def insertion_sort(input_list):
    pass

if __name__ == '__main__':
    input_list = [9, 5, 8, 6, 7, 1, 4, 3, 2]
    print("Input List : {0}".format(input_list))
    print("Merge Sort : {0}".format(merge_sort(input_list)))
