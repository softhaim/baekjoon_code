'''
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

그냥 오더의 순서에 맞추어서 재귀로 들어가면 됨.
'''
import sys

input = sys.stdin.readline

def pre_order(node, result):
    for left_node, right_node in graph[node]:
        if left_node == "." and right_node == ".": # 리프 노드라는 뜻
            result.append(chr(node+64))
            return
        result.append(chr(node+64))
        if left_node != ".":
            pre_order(left_node, result)
        if right_node != ".":
            pre_order(right_node, result)
    
    return

def mid_order(node, result):
    for left_node, right_node in graph[node]:
        if left_node == "." and right_node == ".": # 리프 노드라는 뜻
            result.append(chr(node+64))
            return
        if left_node != ".":
            mid_order(left_node, result)
        result.append(chr(node+64))
        if right_node != ".":
            mid_order(right_node, result)
    
    return

def post_order(node, result):
    for left_node, right_node in graph[node]:
        if left_node == "." and right_node == ".": # 리프 노드라는 뜻
            result.append(chr(node+64))
            return
        if left_node != ".":
            post_order(left_node, result)
        if right_node != ".":
            post_order(right_node, result)
        result.append(chr(node+64))
    
    return

if __name__ == "__main__":
    N = int(input())

    graph = [[] for _ in range(N+1)]
    for _ in range(N):
        node, left_node, right_node = input().split()
        if left_node != ".":
            left_node = ord(left_node) - 64
        if right_node != ".":
            right_node = ord(right_node) - 64
            
        graph[ord(node)-64].append((left_node, right_node))
    
    pre_order_result = []
    mid_order_result = []
    post_order_result = []

    pre_order(1,pre_order_result)
    mid_order(1,mid_order_result)
    post_order(1,post_order_result)

    print("".join(pre_order_result))
    print("".join(mid_order_result))
    print("".join(post_order_result))