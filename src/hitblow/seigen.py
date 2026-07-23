"""Hit & Blowの入力回数を制限する機能。"""

import builtins

from .core import judge


def set_limit(digits, secret):
    """プレイヤーに制限回数を設定してもらい、入力回数を監視する。"""

    original_input = builtins.input

    while True:
        limit_input = original_input(
            "予想できる回数を入力してください > "
        ).strip()

        if limit_input.isdigit() and int(limit_input) >= 1:
            limit = int(limit_input)
            break

        print("1以上の整数を入力してください。")

    count = 0

    def limited_input(message):
        nonlocal count

        guess = original_input(message).strip()

        # 指定された桁数の数字だけを入力回数として数える
        if len(guess) == digits and guess.isdigit():
            count += 1
            print(f"入力回数：{count}/{limit}")

            # 正解した場合は通常のinputに戻す
            if guess == secret:
                builtins.input = original_input
                return guess

            # 最後の入力でも不正解だった場合
            if count >= limit:
                hit, blow = judge(secret, guess)
                print(f"  Hit={hit}  Blow={blow}")
                print(f"回数制限に達しました。答えは {secret} です。")
                print("スコア：0 点")

                builtins.input = original_input
                raise SystemExit

        return guess

    builtins.input = limited_input
    return limit