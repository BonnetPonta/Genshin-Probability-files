# ☆5キャラ：0.6//☆4キャラ：2.55/☆4武器：2.55//☆3武器：94.3
# 10連毎に9体目まで+10体目が☆4以上排出しなかった場合、10体目を☆4スコアにせっつして1/2で武器かキャラにする
# 90連以内に☆5が排出しなかった場合、90体目を☆5にリプレイス。その際50%の確率でピックアップ☆5キャラ
# ☆5が排出した場合、天井リセット
# nmb:1~10000 /cnt:ガチャ引いた回数 /cnt数字:数字分カウント /limit45:☆4~5でたらカウント /star3~5:☆3~☆5 /star42:☆4を1/2で排出

import random
nmb = 0
cnt = 0
star5 = 0
star4b = 0
star4c = 0
star3 = 0
star42 = 0

limit45 = 0
limit5 = 0

cnt10 = 0
cnt90 = 0
cnt1000 = 0

character_cnt_zin = 0
character_cnt_nana = 0
character_cnt_kokusei = 0
character_cnt_mona = 0
character_cnt_deil = 0
character_cnt_arubedo = 0

while True:  # 無限ループ
    nmb = random.randint(1, 10000)  # 乱数生成
    cnt = cnt + 1  # カウント
    cnt10 = cnt10 + 1
    cnt90 = cnt90 + 1
    cnt1000 = cnt1000 + 1

    if 1 <= nmb <= 315:  # 1~315 ☆4~5の場合カウント+1
        limit45 = limit45 + 1
    if cnt10 == 10 and limit45 == 0:  # 10連以内に☆4～5が出なかった場合
        star42 = random.randint(1, 2)  # ☆4の武器かキャラ乱数
        if star42 == 1:
            nmb = 61
        if star42 == 2:
            nmb = 316
    if cnt10 == 10:  # 10連毎にリセット
        limit45 = 0
        star42 = 0
        cnt10 = 0

    if 1 <= nmb <= 60:  # 1~60 ☆5の場合
        limit5 = limit5 + 1
    if cnt90 == 90 and limit5 == 0:  # 90連毎にカウント
        nmb = 1
    if cnt90 == 90 or limit5 >= 1:  # 90連か☆5でたらリセット
        limit5 = 0
        cnt90 = 0

    if nmb <= 60:  # キャラカウント
        print(cnt, "回目：", "5キャラ")
        star5 = star5 + 1
        character_name = random.randint(1, 10)
        if character_name == 1:
            character_cnt_zin = character_cnt_zin + 1
        if character_name == 2:
            character_cnt_kokusei = character_cnt_kokusei + 1
        if character_name == 3:
            character_cnt_mona = character_cnt_mona + 1
        if character_name == 4:
            character_cnt_deil = character_cnt_deil + 1
        if character_name == 5:
            character_cnt_nana = character_cnt_nana + 1
        if 6 <= character_name <= 10:
            character_cnt_arubedo = character_cnt_arubedo + 1
    if 61 <= nmb <= 315:
        print(cnt, "回目：", "4キャラ")
        star4c = star4c + 1
    if 316 <= nmb <= 570:
        print(cnt, "回目：", "4武器")
        star4b = star4b + 1
    if 571 <= nmb <= 10000:
        print(cnt, "回目：", "3武器")
        star3 = star3 + 1

    if cnt1000 == 1000:  # 1000回終わったら表示&終了
        print('\033[35m', "トータル", '\033[0m', "5キャラ", '\033[33m', star5, '\033[0m', "4キャラ", '\033[96m',
              star4c, '\033[0m', "4武器", '\033[96m', star4b, '\033[0m', "3武器", '\033[32m', star3, '\033[0m')
        print("ジン", '\033[33m', character_cnt_zin, '\033[0m', "刻晴", '\033[33m', character_cnt_kokusei, '\033[0m', "モナ", '\033[33m', character_cnt_mona, '\033[0m',
              "ディルック", '\033[33m', character_cnt_deil, '\033[0m', "七七", '\033[33m', character_cnt_nana, '\033[0m', "星5PUキャラ", '\033[33m', character_cnt_arubedo, '\033[0m')
        break
