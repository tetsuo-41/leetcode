# LeetCode 128. Longest Consecutive Sequence

## ① Clarify the problem (約1分)
Okay, so I’m given an unsorted array of integers, possibly with duplicates, and I need to find the length of the longest sequence of consecutive numbers. Is that correct?

## ② Constraintsの確認 (約30秒)
- Are negative numbers allowed?
- Can the array be empty?
- What’s the expected size of the array?

## ③ Naive approach を軽く言う (約30秒〜1分)
A straightforward way would be to sort the array and then iterate through it, counting consecutive numbers.  
That would be O(n log n) due to sorting, but since we want O(n), we need a better approach.

## ④ Optimal solution を言ってから書き始める (ここが大事)
So instead, I’ll use a HashSet to store all numbers for O(1) lookups.  
For each number, I’ll check only if it’s the start of a sequence by seeing if `num - 1` is not in the set.  
Then I’ll iterate forward to count the length of the sequence.  
That way, each number is visited at most twice, giving us O(n) time.

## ⑤ Live talk (コード書きながらの補足トーク)
- I'm creating a set to enable O(1) lookups.  
- Now I'm looping through each number in the set.  
- If `num - 1` is not in the set, this might be the start of a sequence.  
- Then I extend the sequence as far as possible.  
- Finally, I update the maximum length.





# LeetCode 128. 最長の連続数列

## ① 問題の明確化 (約1分)  
はい、整数の並べ替えられていない配列が与えられ、重複を含む可能性があり、その配列内で最も長い連続する数の列の長さを求める必要があります。これで合っていますか？  

## ② 制約の確認 (約30秒)
- 負の数は許可されていますか？
- 配列は空でもよいですか？
- 配列の期待されるサイズはどれくらいですか？

## ③ 単純なアプローチを簡単に説明する (約30秒～1分)
単純な方法は、配列をソートしてから順に巡回し、連続する数を数えることです。  
ソートのためO(n log n)になりますが、O(n)を求めたいので、より良いアプローチが必要です。

## ④ 最適解を説明してから書き始める (ここが重要)
代わりに、HashSetを使用してすべての数を格納し、O(1)で検索できるようにします。 
各数値について、`num - 1`がセットに存在しないかどうかを確認し、それがシーケンスの開始点かどうかを判断します。  
その後、シーケンスの長さを数えるために前方へ反復処理を行います。  
これにより、各数値は最大で2回しか訪問されず、O(n)の時間複雑度を実現できます。

## ⑤ ライブ解説（コードを書きながらの補足説明）
- O(1) での検索を可能にするためにセットを作成しています。  
- 次に、セット内の各数値をループで巡回しています。  
- `num - 1` がセットに含まれていない場合、これがシーケンスの始まりである可能性があります。  
- その後、シーケンスを可能な限り延長します。  
- 最後に、最大長を更新します。