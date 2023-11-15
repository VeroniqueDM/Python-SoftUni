from collections import deque

kids_queue = deque(input().split())
n_toss = int(input())

while len(kids_queue) > 1 :
    kids_queue.rotate(-n_toss)
    print(f"Removed {kids_queue.pop()}")

print(f"Last is {kids_queue.popleft()}")