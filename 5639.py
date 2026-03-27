'''
전위순회는:

첫 값 = 루트
그 다음부터 루트보다 작은 구간 = 왼쪽 서브트리
그 다음 루트보다 큰 구간 = 오른쪽 서브트리
'''

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

preorder = []
while True:
    try:
        line = input().strip()
        if not line:
            break
        preorder.append(int(line))
    except:
        break

def postorder(start, end):
    if start > end:
        return
    
    root = preorder[start]
    
    split = end + 1
    for i in range(start + 1, end + 1):
        if preorder[i] > root:
            split = i
            break
    
    postorder(start + 1, split - 1)  # 왼쪽
    postorder(split, end)            # 오른쪽
    print(root)

postorder(0, len(preorder) - 1)