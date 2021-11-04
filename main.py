# word = {'one': 'bir',
#         'two': 'ikki',
#         'three': 'uch',
#         'four': 'to`rt'
# }
#
# def translator(word):
#     print(word['two'])
#
# translator(word)


#
# result = (myFinalMarks['CSF'] + myFinalMarks['FunPro'] + myFinalMarks['WT']) / myFinalMarks.__len__()
# print(result)
#
#
myFinalMarks = {'CSF': 75,
                'FunPro': 80,
                'WT': 85}


def calculate(key):
    sum1 = 0

    for i in key:
        sum1 = sum1 + key[i]

    _final_result = sum1 / myFinalMarks.__len__()
    print(_final_result)


calculate(myFinalMarks)


# letters = {
#             'a' =
# }
