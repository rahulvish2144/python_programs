"""
5. Python function takes an Array as an argument find out if there is any number in the Array which is greater than sum of other elements.
   If there is no number in the Array which is greater than sum of other elements then find the max possible number and difference in value
   that it takes to be the max possible number.: Done

   Don't use any built-in functions

Examples:
----------

func([10,20,30,45,90,200,2000])
Output 2000

func([10,20,30,40,90,200,20])
Output 200,10

Here sum of all other numbers other than 200 is 210(10 + 20 + 30 + 40 + 90 + 20)
210 - 200 = 10

Note: Code must be Optimized and all Scenarios handled.
"""


def problem_5(number):
    """
    This program takes a list as an argument and checks whether there
    is any number in the list which is greater than sum of other elements.

    :param number: List containing numbers
    :return: Maximum number in the list or difference in value
    that it takes to be the max possible number
    """
    max_num = find_max_num(number)
    sum = 0
    for each_num in number:
        if each_num != max_num:
            sum += each_num

    if max_num > sum:
        return max_num
    else:
        return max_num, (sum - max_num)


def find_max_num(num_list):
    max_num = num_list[0]
    for x in num_list:
        if x > max_num:
            max_num = x

    return max_num


result = problem_5([10,20,30,40,90,150,20])
print(result)