from collections import Counter

def most_common_value(number_list):
    """ returns the most common element of the list
    """
    most_common = []
    item_counts = Counter(number_list)
    most_common = item_counts.most_common(1)[0][0]

    return most_common


if __name__ == "__main__":
    nums = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
    print(f"Most common value = {most_common_value(nums)}")


