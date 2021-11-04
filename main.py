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
# myFinalMarks = {'CSF': 75,
#                 'FunPro': 80,
#                 'WT': 85}
#
#
# def calculate(key):
#     sum1 = 0
#
#     for i in key:
#         sum1 = sum1 + key[i]
#
#     _final_result = sum1 / myFinalMarks.__len__()
#     print(_final_result)
#
#
# calculate(myFinalMarks)

# h = {'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2, 'u': 2, 't': 1}

# def histogram(s):
#     d = dict()
#     for c in s:
#         if c not in d:
#             d[c] = 1
#         else:
#             d[c] += 1
#         return d
#
# h = histogram('brontosaurus')
# print(histogram(h))


csf = {
'cw1-weight': 0.4,
'cw1-mark': 79,
'exam-weight': 0.6,
'exam-mark': 65
}

first = csf.get('cw1-weight') * csf.get('cw1-mark')
exam = csf.get('exam-weight') * csf.get('exam-mark')
final = first + exam
print(final)