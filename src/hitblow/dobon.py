# dobon.py
import random


def init_dobons(secret, digits, count=5):
    """正解（secret）とは異なり、お互いにも重複しないドボン数字を指定個数（デフォルト5個）生成する。"""
    dobons = set()
    
    # 桁数に対して生成可能な総パターン数を計算（重複なし数字の場合、最大 10Pdigits 通り）
    # 例: 3桁なら 10 * 9 * 8 = 720通り。
    # ドボンを5個作るのに十分なパターンがあるか一応チェック（1桁だと足りなくなるため）
    import math
    max_patterns = math.perm(10, digits)
    
    # 安全のため、作れる最大数か指定個数の小さい方をターゲットにする
    target_count = min(count, max_patterns - 1) 

    while len(dobons) < target_count:
        dobon_num = "".join(random.sample("0123456789", digits))
        # 正解（secret）とは被らないようにする
        if dobon_num != secret:
            dobons.add(dobon_num)
            
    return list(dobons)


def is_dobon(guess, dobons_list):
    """プレイヤーの入力が、5つのドボン数字のいずれかと一致しているか判定する。"""
    return guess in dobons_list