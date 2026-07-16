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
    elif digit_input != "":
        print("数値ではなかったため、3桁で開始します。")

    # 決まった桁数で正解を作る
    secret = make_secret(digits)
    print(f"\nHit & Blow（{digits} 桁・重複なし）を開始します！")

    tries = 0
    while True:
        guess = input("予想 > ").strip()

        # ===== ② 入力コマンドに足す（ヒント など）: ここに書く（import もここに） =====
        # 例:  from .hint import hint
        #      if guess == "h":
        #          print(hint(secret)); continue

        if len(guess) != digits or not guess.isdigit():
            print(f"{digits} 桁の数字で入力してね")
            continue
        tries += 1
        hit, blow = judge(secret, guess)
        print(f"  Hit={hit}  Blow={blow}")
        if hit == digits:

            # ===== ③ 勝利時に足す（スコア・履歴 など）: ここに書く =====

            print(f"正解！ {tries} 回で当たり（答え {secret}）")
            break
