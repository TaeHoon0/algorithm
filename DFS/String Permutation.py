import sys

N = int(sys.stdin.readline().strip())

def dfs(str, prev_str, result):
    if len(str) == 0:
        result.append(prev_str[:])

    for i, char in enumerate(str):
        next_str = str[:i] + str[i + 1:]
        temp_str = prev_str + [char]
        dfs(next_str, temp_str, result)

for i in range(N):
    print(f"Case # {i+1}:")
    str = sys.stdin.readline().strip()
    result = []
    dfs(str, [], result)

    for r in result:
        print(''.join(r))