https://cs61a.org/disc/disc04/#q1-map-filter-reduce

我后来知道其实不一定得是单变量函数。比如 list(map(lambda x, y: y - x, ls1, ls2)) 其实也是可用的。

本质上是 function(func, iterable)

这三个函数很有用，主要要记住他们起什么作用：

map 是将 func 作用于 iterable 的每一项；

filter 是将 iterable 中符合 func 的每一项筛选出来；

reduce 是将 iterable 的每一项按照 func 计算出一个值。
