"""
11. 给定3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

给定4输出：
------d------
----d-c-d----
--d-c-b-c-d--
d-c-b-a-b-c-d
--d-c-b-c-d--
----d-c-d----
------d------

"""
english = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n = int(input('输入整数：'))
row = 2*n - 1
for i in range(1, 2*n):
    print('-'*((4*n-3)//2), end='')
    print(english[i-1], end='')
    print('-'*((4*n-3)//2))





