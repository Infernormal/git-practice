# Taken From
# Iterating Over Data
# Problem-Set While Loops #11
def silly_sum():
    """ reads numbers from the user (use input_int) 
        summing as we go until either
        the user enters 0, or
        the sum reaches or exceeds 1000
    """
    total = 0
    while True:
        valid_input = input_int()
        if valid_input == 0:
            break
        elif total < 1000:
            total += valid_input
        else:
            break
    return total

   

if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")
