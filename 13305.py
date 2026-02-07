# 13305. 주유소

import sys

input = sys.stdin.readline
n = int(input())

road = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = 0
min_cost = price[0]  # 첫 번째 도시 가격

for i in range(n - 1):
    min_cost = min(min_cost, price[i])  # 현재까지 중 가장 싼 주유소 가격 유지 => 이게 킥! 가장 싼 가격으로 계속 주유하면 됨 (그전에 넣고 간다라고 생각하고)
    min_price += min_cost * road[i] 

print(min_price)