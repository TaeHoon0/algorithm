import sys

N = int(sys.stdin.readline().strip())
words = []

for _ in range(N):
    word = sys.stdin.readline().strip()
    words.append(word)

# set은 중복이 없기 때문에 set으로 변환하여 중복 제거 후 list로 다시 변환
words = list(set(words))
def merge(arr1, arr2):
    result = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if len(arr1[i]) < len(arr2[j]):   #문자열 길이비교
            result.append(arr1[i])
            i += 1
        # 길이가 같을 때 사전순으로 비교
        elif len(arr1[i]) == len(arr2[j]):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result

def mergeSort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    return merge(mergeSort(left), mergeSort(right))

words = mergeSort(words)

for w in words:
    print(w)