
# Given an array X of positive integers, its elements are to be transformed by running the following operation on them as many times as required:
# if X[i] > X[j] then X[i] = X[i] - X[j]
# When no more transformations are possible, return its sum ("smallest possible sum").
# For instance, the successive transformation of the elements of input X = [6, 9, 21] is detailed below:
# X_1 = [6, 9, 12] # -> X_1[2] = X[2] - X[1] = 21 - 9
# X_2 = [6, 9, 6]  # -> X_2[2] = X_1[2] - X_1[0] = 12 - 6
# X_3 = [6, 3, 6]  # -> X_3[1] = X_2[1] - X_2[0] = 9 - 6
# X_4 = [6, 3, 3]  # -> X_4[2] = X_3[2] - X_3[1] = 6 - 3
# X_5 = [3, 3, 3]  # -> X_5[1] = X_4[0] - X_4[1] = 6 - 3

def solution(x):
    
    def get_largest_val( my_list ):
        largest_value = None
        largest_index = None
        for i in range( len( my_list ) ):
            current_value = my_list[i]
            if not largest_value or current_value > largest_value:
                largest_value = current_value
                largest_index = i

        return largest_value, largest_index

    largest_value, largest_index = get_largest_val( x )
    new_list = [ x[i] for i in range( len( x ) ) if i !=  largest_index ]
    largest_difference, _ = get_largest_val( new_list )
    print( new_list )
    if x[largest_index] - largest_difference <= 0:
        return sum( x )
    x[largest_index] -= largest_difference
    print( x )
    return solution( x )

test_solution = solution([6, 9, 21])
assert test_solution == 9