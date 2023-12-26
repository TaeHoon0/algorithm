import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    nums = []
    ans = "YES"

    for _ in range(n):
        num = sys.stdin.readline().strip()
        nums.append(num)

    nums.sort()
    print(nums)
    for i in range(len(nums) - 1):
        # 사전순으로 정렬 후, 다음 값을 현재 문자로 길이로 슬라이싱해서 접두어로 포함하고 있는지 확인
        if nums[i] in nums[i+1][:len(nums[i])]:
            ans = "NO"
            break

    print(ans)