"""
4. Function takes 2 Arrays, an integer X as Arguments. Find out pairs of numbers from both lists divisible by X. When
Collecting Pairs the element in the first list index(n) and the element in the second list index(n) must both be divisible by X,
Only then it forms a pair. : Done

Example:

 func([10,20,30,40,50],[12,24,40,90,200],10)
 while index is 0 : 10,12 (12 not divisible by 10)
 while index is 1 : 20,24 (24 not divisible by 10)
 while index is 2 : 30,40 (30 & 40 both divisible by 10)
 Similarly parse all indexes and return final array

 STEP 1 Output :
        [(30,40),(40,90),(50,200)]
 STEP 2 Output :
    From the List returned above return only the pair that has max value
    [50,200] .. since 200 is the max number among all from STEP 1 Output
"""


def problem_4(*args, dividend):
    """
    This program takes 2 Arrays, an integer X as Arguments.
    Find out pairs of numbers from both lists divisible by X.
    When Collecting Pairs the element in the first list index(n)
    and the element in the second list index(n) must both be
    divisible by X, Only then it forms a pair.

    :param args: Lists containing number
    :param dividend: Integer value
    :return: Pair of numbers which are divisible by the passed dividend
    """
    final_list = []
    length = len(args)
    if length % 2 == 0:
        for i in range(0, len(args[0])):
            if len(args[0]) == len(args[1]):
                if (args[0][i] % dividend == 0) and (args[1][i] % dividend == 0):
                    final_list.append((args[0][i], args[1][i]))
            else:
                raise AssertionError('Length of lists must be equal')
    else:
        raise AssertionError('Even number of lists should be passed in order to form pair')
    return final_list


result = problem_4([10, 20, 30, 40, 50], [12, 24, 40, 90, 200], dividend = 10)
print(result)