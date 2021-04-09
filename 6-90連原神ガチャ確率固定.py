# ☆5キャラ：0.6//☆4キャラ：2.55/☆4武器：2.55//☆3武器：94.3
# 10連毎に9体目まで+10体目が☆4以上排出しなかった場合、10体目を☆4スコアにせっつして1/2で武器かキャラにする
# 90連以内に☆5が排出しなかった場合、90体目を☆5にリプレイス。その際50%の確率でピックアップ☆5キャラ
# ☆5が排出した場合、天井リセット
# nmb:1~10000 /cnt:ガチャ引いた回数(10回カウント) /cnt45:☆4~5でたらカウント /star3~5:☆3~☆5 /star42:☆4を1/2で排出

import random
nmb = 0
cnt = 0
star5 = 0
star4b = 0
star4c = 0
star3 = 0

cnt45 = 0
star42 = 0

cnt5 = 0
cnt90 = 0

while True:
    nmb = random.randint(1, 10000)
    cnt += + 1
    cnt90 += + 1

    if 1 <= nmb <= 315:
        cnt45 += + 1
    if cnt == 10 and cnt45 == 0:
        star42 = random.randint(1, 2)
        if star42 == 1:
            nmb = 61
        if star42 == 2:
            nmb = 316

    if cnt90 == 90 and cnt5 == 0:
        nmb = 1

    if nmb <= 60:
        print(cnt, "回目：", "5キャラ")
        star5 += 1
        cnt5 += 1
    if 61 <= nmb <= 315:
        print(cnt, "回目：", "4キャラ")
        star4c += 1
    if 316 <= nmb <= 570:
        print(cnt, "回目：", "4武器")
        star4b += 1
    if 571 <= nmb <= 10000:
        print(cnt, "回目：", "3武器")
        star3 += 1

    if cnt == 90:
        print("トータル", "5キャラ", '\033[33m', star5, '\033[0m', "4キャラ", '\033[96m', star4c,
              '\033[0m', "4武器", '\033[96m', star4b, '\033[0m', "3武器", '\033[32m', star3, '\033[0m')
        break
