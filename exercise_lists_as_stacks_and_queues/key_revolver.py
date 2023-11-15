from collections import deque
bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(y) for y in input().split())
value_intelligence = int(input())
trial_no = 0
while locks:
    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    trial_no +=1
    if current_bullet <= current_lock:
        print('Bang!')
    else:
        print('Ping!')
        locks.appendleft(current_lock)
    if trial_no %gun_barrel_size == 0 and bullets:
        print('Reloading!')
    if not bullets:
        break

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    total_price_bullets = trial_no *bullet_price
    earnings = value_intelligence - total_price_bullets
    print(f'{len(bullets)} bullets left. Earned ${earnings}')