import math
from unittest import TestCase, main
def Pascal_tree(number_of_lines):
    if type(number_of_lines) != int or number_of_lines < 0:
        return "ValueError"
    new_list = [[1]]
    for n in range(1,number_of_lines+1):
        origin_list=[]
        for k in range(0,n+1):
            origin_list.append(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))
        new_list.append(origin_list)
    return new_list


b=int(input())
ans = Pascal_tree(b)
for i in range(len(ans)):
    print(ans[i])


class Validator(TestCase):
    def test_correct_values(self):
        if not self.assertEqual(Pascal_tree('abc'), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(Pascal_tree(0), [[1]]):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(Pascal_tree(2), [[1], [1, 1], [1, 2, 1]]):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(Pascal_tree(-3), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(Pascal_tree(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]):
            print("Test passed")
        else:
            print("Test failed")


main()