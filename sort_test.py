import unittest
import sort

class CustomTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_merge_sort(self):
        in_list = [9, 5, 8, 6, 7, 1, 4, 3, 2]
        rtn_list = sort.merge_sort(in_list)

        self.assertEqual(rtn_list, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_merge_sort(self):
        in_list = [9, 5, 8, 6, 7, 1, 4, 3, 2]
        rtn_list = sort.merge_sort(in_list)

        self.assertEqual(rtn_list, [1, 2, 3, 4, 5, 6, 7, 8, 9])



# unittest를 실행
if __name__ == '__main__':
    unittest.main()