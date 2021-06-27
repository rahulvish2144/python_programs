"""
1. Function takes any n.o. lists as Arguments(*args), an integer X . Find the list that has most numbers divisible by X.
Don't use any built-in functions: Done

Examples:
----------
func([1,2,3,4,5],[1,3,4,6,9],[10,12,9,7,8],[12,7,9,8,14],3)


So func must return [1,3,4,6,9] since it has got 3 items divisible by 3. Remaning lists have lesser.

Exception: If there's more than 1 list that got same number of items divisible by X then pick the items in the lists
that are divisible by X and return.


func([1,2,3,4,5],[1,3,4,6,9],[3,9,10,11,18],[10,12,9,7,8],[12,7,9,8,14],3)
Here there are 2 lists that's got 3 items divisibly by 3
[1,3,4,6,9],[3,9,10,11,18]
So your function must return [3,6,9,3,9,18]

Note: Code must be Optimized and all Scenarios handled.
"""


def problem_1(*args, dividend):
    count_of_num = []
    for each_list in args:
        count = 0
        for each_num in each_list:
            if each_num % dividend == 0:
                count += 1
        count_of_num.append(count)

    print(count_of_num)

    # for i in count_of_num:
    #     index = 0
    #     for j in count_of_num:
    #         if j > i:
    #             index += 1
    #             break

    # return args[index]
    return count_of_num


result = problem_1([1,2,3,4,5], [1,3,4,6,9], [10,12,9,7,8], [12,7,9,8,14], [3, 6, 9, 12, 15, 18], dividend= 3)

print(result)