"""
2. Function takes any n.o. lists as Arguments (*args), an integer X . Find all the elements in the lists that has numbers divisible by X.
Create a final dictionary and return. The final dictionary must contain the count of occurrences of each element in the lists that are divisible by X. : Done

Don't use any built-in functions

Examples:
----------

func( [10,12,14,40,60,65,80,90],[3,4,65,40,40,30,20],[120,400,80,90,20,60],5 )
func must return:
{10:1, 40:3, 60:2, 65:2, 80:2,90:2, 30:1, 20:2, 120:1,400:1}

The numbers that are divisible by X i.e. 5 in this case are the keys, the number of times that a key occurs across all lists
is the value

Note: Code must be Optimized and all Scenarios handled.
"""


def problem_2(*args, dividend):
    """
    This program takes number of lists and check whether all the elements
    are divisible by the dividend passed.

    :param args: Number of lists
    :param dividend: Integer number with which each elements of a list gets divided
    :return: Dictionary containing all the number divisible with the dividend and it's count
    """
    final_dict = {}
    for each_list in args:
        for each_num in each_list:
            last_occurrence = 0
            if type(each_num) == int or type(each_num) == float:
                if each_num % dividend == 0:
                    last_occurrence += count_x(each_list, each_num)
                    final_dict[each_num] = last_occurrence
            else:
                raise ValueError('Expected numerical value')

    for each_key in final_dict.keys():
        total_occurrence = 0
        for each_list in args:
            total_occurrence += count_x(each_list, each_key)

        final_dict[each_key] = total_occurrence

    return final_dict


def count_x(lst, x):
    count = 0
    for each_element in lst:
        if each_element == x:
            count = count + 1

    return count


result = problem_2([10, 12, 14, 40, 60, 65, 80, 90, 120, 400], [3, 4, 65, 40, True, 30, 20], [120, 400, 80, 90, 20, 60, -400], dividend = 2)
print(result)