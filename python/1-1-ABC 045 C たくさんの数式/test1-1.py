def sum_all(num: int) -> int :

    str_num = str(num)
    len_str_num = len(str_num)

    #iがlen_str_numの文字列のインデックス, sentenceが+と数値を含む文字列 
    def dfs(i: int , sentence: str) -> int: 
        # 再起が最後まで終了した時
        if i == len_str_num - 1:
            #＋で挟んでいる文字の合計値を出す
            return sum(list(map(int, sentence.split("+"))))
        #間に+を入れるか入れないかで分岐させ、全通り検索できるようにする
        return dfs(i + 1, sentence + "+" + str_num[i + 1]) + dfs(i + 1, sentence + str_num[i + 1])
     
    #初期値として文字列のインデックス, 文字列にした数値の0行目の値を代入
    return dfs(0, str_num[0])


print(sum_all(125))


import unittest
class TestSumAll(unittest.TestCase):

    def test_sum_all(self):
        # Case : normal
        val = 1234
        self.assertEqual(sum_all(val), 1736)

        # Case : 0
        val = 0
        self.assertEqual(sum_all(val), 0)

if __name__ == "__main__":
    unittest.main()

#atcoderテストケースもあるんだね
