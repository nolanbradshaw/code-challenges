
n = [1,3,5,6,7,9,11,15,16,18]
sum_to_find = 20

def pair_with_sum(n, sum_to_find):
    min_index = 0
    max_index = len(n) - 1
    # Iterate until the indexes touch.
    while min_index < max_index:
        current_sum = n[min_index] + n[max_index]
        if current_sum == sum_to_find:
            return True
        elif current_sum < sum_to_find:
            # Move min_index (pair to small)
            min_index += 1
        else:
            # Move max_index (pair to large).
            max_index -= 1
    
    return False

if __name__ == '__main__':
    print(pair_with_sum(n, sum_to_find))
