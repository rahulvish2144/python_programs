"""
3. Function takes an Array as an argument find out if there is any number in the Array which is greater than sum of other elements.
   Don't use any built-in functions: Done

Examples:
----------

func([10,20,30,45,90,200,2000])
Output 2000

func([10,20,30,40,90,200,20])
Output None
Note: Code must be Optimized and all Scenarios handled.
"""


def problem_3(number):
    """
    This program takes a list as an argument and checks whether there
    is any number in the list which is greater than sum of other elements.

    :param number: List containing numbers
    :return: Maximum number in the list or None
    """
    max_num = find_max_num(number)
    sum = 0
    for each_num in number:
        if type(each_num) == int or type(each_num) == float:
            if each_num != max_num:
                sum += each_num
        else:
            raise ValueError('Expected numerical value')

    if max_num > sum:
        return max_num
    else:
        return None


def find_max_num(num_list):
    max_num = num_list[0]
    for x in num_list:
        if x > max_num:
            max_num = x

    return max_num


result = problem_3([10, 20, 30, 40, 90, 200, 20])

print(result)