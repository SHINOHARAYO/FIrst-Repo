# First-Repo
***
## OK LA  

记得Python文件前添加这段:  

    #!/usr/bin/python
    # -*- coding: UTF-8 -*-

***

## Hello, World!

OG Hello, World!

    #!/usr/bin/python
    # -*- coding: UTF-8 -*-

    #输出字符串 Hello, World!
    print("Hello, World!")

## 简单例子: 使用Python求解斐波那契数列

使用矩阵法求解

$$
\begin{bmatrix}
Fib(n+1) \\
Fib(n)
\end{bmatrix}
=
\begin{bmatrix}
1 & 1 \\
1 & 0
\end{bmatrix}
\begin{bmatrix}
Fib(n) \\
Fib(n-1)
\end{bmatrix}
$$

代码如下:

    # 两个n阶矩阵相乘
    def matrix_multiplication(n, A, B):
    C = []
    for line in range(n):
        line_arr = []
        for column in range(n):
            item = 0
            for i in range(n):
                item += A[line][i] * B[][i]
            line_arr.append(item)
        C.append(line_arr)
    return C

    # 矩阵求解，所求元素为A^{n-1} 中的 A[0][0], 或 A^n 中的 A[0][1]
    def Fib_matrix(n):
    if check_input(n):
        # 检查输入
        if n < 2: return n
        A = [[1, 1], [1, 0]]
        result = [[1, 0], [0, 1]]
        matrix_n = 2
        while n > 0:
            result = matrix_multiplication(matrix_n, result, A)
            n -= 1
        return result[0][1]
    else:
        # 默认返回值
        return -1


