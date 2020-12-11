def sum_all(num: int) -> int :

    str_num = str(num)
    len_str_num = len(str_num)

    #iがlen_str_num内に入れられる+の場所, sentenceが+と数値を含む文字列 
    def dfs(idx: int , sentence: str) -> int: 
        # 再起が最後まで終了した時
        if idx == len_str_num - 1:
            #＋で挟んでいる文字の合計値を出す
            return sum(list(map(int, sentence.split("+"))))
        #間に+を入れるか入れないかで分岐させ、全通り検索できるようにする
        return dfs(idx + 1, sentence + "+" + str_num[idx + 1]) + dfs(idx + 1, sentence + str_num[idx + 1])

    return dfs(0, str_num[0])


print(sum_all(1234))


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
