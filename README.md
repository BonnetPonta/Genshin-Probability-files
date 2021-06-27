# Genshin-Probability-files  
# Langage  
1.[English](https://github.com/BonnetPonta/Genshin-Probability-files#english)  
2.[日本語](https://github.com/BonnetPonta/Genshin-Probability-files#日本語)
# [English]  
## [About Genshin Gacha]  
There are three types of gacha: a limited-time PU character gacha that includes PU characters, a limited-time weapon gacha, and a regular prayer that is always held.
This time I tried to reproduce PU gacha and normal gacha.  

There are 5 types of 3 star weapons, 4 star weapons, 4 star characters, 5 star weapons, and 5 star characters in this game, with 5 stars being the highest rank and 3 stars being the lowest rank.  
Probability is 5: 0.6% star 4: 2.55% each star 3: 94.3%  
Therefore, if each is expressed as 1 to 10000  
5 star characters: 1..60  
4 star characters: 61..315  
4 Star Weapon: 316..570  
3 star weapon: 571..10000  
It will be.  

There is also a ceiling.  
① If 5 stars are not discharged within 90 stations, 5 stars will be confirmed at the 90th station.  
② If 4 or more stars are not discharged within 10 stations, 4 stars will be confirmed at the 10th station.  

③ In the case of PU gacha, there is a 50% chance that you can get 5 PU star characters. However, if the PU character is not available, it will be confirmed when the next 5 stars are discharged.  


## [File description]  
3 and 5 are iteratively processed until 5 stars appear. 5 which added the display name to 3 is the main.  
4 is fixed 10 times. (No ceiling setting)  
6 is fixed 90 times. (With ceiling setting)  

7 and 9 are extras.  
7 is fixed 1000 times. PU prayer (with ceiling setting)  
9 is fixed 1000 times. Normal prayer (with ceiling setting)  

## [Ingenuity]  
By coloring the last print, I think we were able to emphasize visibility. It's completely free, so you'll want to try it again and again!  

# [日本語]  
## [原神のガチャについて]  
ガチャには、PUキャラが含まれる期間限定のPUキャラガチャと、期間限定の武器ガチャ、常時開催中の通常祈願の3つがあります。  
今回はPUガチャと通常ガチャを再現してみました。  

星3武器、星4武器、星4キャラ、星5武器、星5キャラの5種類がこのゲームに存在し、星5が最高ランク、星3が最低ランクになります。  
確率は星5：0.6％　星4：各2.55％　星3：94.3％  
よってそれぞれ1～10000で表すと  
星5キャラ	：1..60  
星4キャラ	：61..315  
星4武器		：316..570  
星3武器		：571..10000  
となります。  
  
さらに天井があります。  
①さらに90連以内に星5が排出されなかった場合、90連目で星5確定。  
②10連以内に星4以上が排出されなかった場合、10連目で星4確定。  
  
③PUガチャの場合50％の確率でPU星5キャラが入手できます。しかしPUキャラが入手できなかった場合、次の星5排出時確定。  


## [ファイルの説明]  
3と5は星5がでるまで繰り返し処理されます。3に表示名を追加した5がメインです。  
4は10回固定。(天井設定無し)  
6は90回固定。(天井設定有り)  

7と9はおまけです。  
7は1000回固定。PU祈願(天井設定有り)  
9は1000回固定。通常祈願(天井設定有り)  

## [工夫点]  
最後のprintを色を付けることで見やすさ重視にできたと思います。完全無料なので何度もトライしたくなるそんな作品です!  
