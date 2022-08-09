https://cs61a.org/proj/cats/

## Problem 5

分了三种情况：1）如果包含，则 return 本身；2）如果不包含，则 return 差别最小的词；3）如果超出 limit，return 本身。

用了 min 来确定差别最小词。

## Problem 6

我用的方法（recursion）很繁琐，计算量也很大。后来参考了别人的答案，直接用 map(lambda x, y: x != y, str1, str2) 就能输出一个包含 ‘True’ 的集合，
再用 sum 来计算数量。这种 map 的用法我之前不知道。

## Problem 7

我最头疼的一题。tree recursion 对我来说还是有点抽象。俺一开始的做法是找每个字母对应的 index，分别搞成集合，然后去一个个判定这个词存不存在，
比如 cats 的 c 在第3位的话，第4位以后的 a 才算进去。 写出来洋洋洒洒，特别麻烦，而且其实不是tree recursion。

而且这道题 ok 系统里面 ban iteration，题目里没写。(￣◇￣;)

第二天我又回来用 tree recursion 的方法做，分成 helper(typed[1:], reference[1:], limit) + helper(typed[1:], reference, limit），也就是
一位一位数判定，再写了一大堆条件，终于整对了，但很不简洁优雅。

## Problem 8

目的：1) call upload func, and 2) return player i's progress

我新定义了一个 func 来计算正确率，在发现错误时停止 for loop。可能不是最简单的做法。

## Problem 9

目的：return match function， match 是一个 dictionary 包含 ‘words’ 和 ‘times‘。

因为数据为时间节点，所以我用 map func 来计算时间间隔，即 (lambda x,y: y - x, ls, ls[1:])。

## Problem 10

目的：return 的是一个 list of lists， list[0] 应该是 player 0 打得最快的词。（ + 特殊规则）

因为输出值表现为 [[], [], ...], 每个子集合的 index 就是 player 的 index 嘛。所以我先定义一个 list 变量 output 包含 x 个 []，用 list comp。
之后只要用 .append() 把词加进去就可以了！

所以，对于每个词而言，我得知道它进哪个 []，我想到用 min，变量为 palyer_indices，key 为 time。这样 min 输出的值就是打字最快的 player 的 index。 
