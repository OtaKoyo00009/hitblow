"""ゲームの進行（入力・表示・ループ）。

★ チームで足す機能は **自分の担当の場所**に書く（1機能=1ファイル）。
   下の「ここに足す」場所は3か所（① 開始時 ② 入力コマンド ③ 勝利時）。
   ペアごとに**別の場所**を直すので、並行作業でも衝突しない。
   import も自分の場所の近くに書くこと（ファイル先頭にまとめない＝衝突回避）。
"""

from .core import judge, make_secret


def play(digits=3):
    secret = make_secret(digits)
    print(f"Hit & Blow（{digits} 桁・重複なし）")

    # ===== ① 開始時に足す（難易度・あいさつ など）: ここに書く =====
    print("★ Hit & Blow カスタム桁数モード ★")


    # 好きな桁数を入力してもらう（デフォルトは3桁）
    digit_input = input("何桁でプレイしますか？ (1〜10) [未入力なら3桁] > ").strip()
    
    if digit_input.isdigit():
        chosen_digits = int(digit_input)
        # 1〜10桁の範囲内ならその桁数にし、それ以外なら3桁にする安全装置

        
        if 1 <= chosen_digits <= 10:
            digits = chosen_digits
        else:
            print("範囲外のため、3桁で開始します。")
            
            digits = 3
    elif digit_input != "":
        print("数値ではなかったため、3桁で開始します。")

    # 決まった桁数で正解を作る
    secret = make_secret(digits)

    from .dobon import init_dobons
    dobon_numbers = init_dobons(secret, digits, count=5)

    print(f"\nHit & Blow（{digits} 桁・重複なし）を開始します！")
    print("⚠️ 注意: 5つの『ドボン数字』が仕掛けられています。踏むと一発ゲームアウト！")

    # 回数制限機能を読み込んで設定する
    from .seigen import set_limit
    max_tries = set_limit(digits, secret)
    
    tries = 0
    while True:
        guess = input("予想 > ").strip()

        # ===== ② 入力コマンドに足す（ヒント など）: ここに書く（import もここに） =====
        # 例:  from .hint import hint
        #      if guess == "h":
        #          print(hint(secret)); continue
        from .dobon import is_dobon
        if is_dobon(guess, dobon_numbers):
            print("\n💥 ドカーン！！！ 💥")
            print(f"ドボン数字【 {guess} 】を踏んでしまいました！ゲームオーバー！")
            print(f"（正解は {secret} でした）")
            # せっかくなので他のドボン数字も教えてあげる親切設計
            other_dobons = [d for d in dobon_numbers if d != guess]
            print(f"（他のドボン数字は {', '.join(other_dobons)} でした）")
            # ドボンの場合はスコア0
            score = 0
            print(f"スコア：{score} 点")
            break

        if len(guess) != digits or not guess.isdigit():
            print(f"{digits} 桁の数字で入力してね")
            continue

        tries += 1
        hit, blow = judge(secret, guess)
        print(f"  Hit={hit}  Blow={blow}")

        if hit == digits:

            # ===== ③ 勝利時に足す（スコア・履歴 など）: ここに書く =====
            # 指定されたスコア計算式
            score = (
                digits * (max_tries-tries)
                / max_tries
                * 10000
            )

            print(f"正解！ {tries} 回で当たり（答え {secret}）")
            print(f"スコア：{score:.0f} 点")
            break