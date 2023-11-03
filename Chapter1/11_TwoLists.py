def combine_lists(first_list, second_list):
    combined_list = []
    for number in first_list:
        combined_list.append(number)
    for number in second_list:
        combined_list.append(number)
    combined_list.sort()
    return combined_list
