#
# def main():
#     list=[]
#     str = input("请输入字符串：")
#     N = int(input("请输入位移量："))
#     for i in str:
#         n = ord(i)
#         new_str= chr(n+N)
#         list.append(new_str)
#     S = "".join(list)
#     print(S)
# if __name__ =="__main__":
#     main()

import queue
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
def treeWidth(tree):
    curwidth = 1
    maxwidth = 0
    q = queue.Queue()
    q.put(tree)
    while not q.empty():
        n = curwidth
        for i in range(n):
            tmp = q.get()
            curwidth -= 1
            if tmp.left:
                q.put(tmp.left)
                curwidth += 1
            if tmp.right:
                q.put(tmp.right)
                curwidth += 1
        if curwidth > maxwidth:
            maxwidth = curwidth
    return maxwidth
if __name__ == '__main__':
    root = Node('A', Node('B', Node('C')), Node('D'))
    width = treeWidth(root)
    print('宽度', width)