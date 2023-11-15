n, m = (int(x) for x in input().split())

n_set = set()
m_set = set()
for _ in range(n):
    current_num_n = int(input())
    n_set.add(current_num_n)
for _ in range(m):
    current_num_m = int(input())
    m_set.add(current_num_m)

res = n_set & m_set

for a in res:
    print(a)