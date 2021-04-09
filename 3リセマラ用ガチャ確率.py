import random
cnt = 0
while True:
    r = random.randint(1, 1000)
    print(r)
    cnt = cnt+1
    if 1 <= r <= 6:
        break
print('\033[96m', str(cnt), '\033[0m', "回目で☆5キャラゲット！")
