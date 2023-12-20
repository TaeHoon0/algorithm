import sys

L, C = map(int, sys.stdin.readline().split())           # L개의 소문자, C개의 문자
letters = sorted(sys.stdin.readline().strip().split()) # 사전순

vowel = ['a', 'e', 'i', 'o', 'u']
pwds = []

def check(pwd):
    vowel_cnt = 0       #모음 개수
    consonant_cnt = 0  #자음 개수

    for char in pwd:
        if char in vowel:
            vowel_cnt += 1
        else:
            consonant_cnt += 1

    return vowel_cnt >= 1 and consonant_cnt >= 2

def dfs(cur_str, start):
    if len(cur_str) == L:
        if check(cur_str):
            pwds.append(cur_str)
        return

    for i in range(start, len(letters)):
        dfs(cur_str + letters[i], i + 1)

dfs('', 0)
pwds.sort()

for pwd in pwds:
    print(pwd)