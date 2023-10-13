'''
Created on 2023/10/13

@author: t21cs029
'''

import random

def janken(player_a, player_b, player_c):
    HANDS = ['グー', 'チョキ', 'パー']

    win_count = {player_a: 0, player_b: 0, player_c: 0}

    def judge(hand_a, hand_b, hand_c):
        # 全員異なる手の場合
        if len(set([hand_a, hand_b, hand_c])) == 3:
            return "引き分け"

        # どれか2人が同じ手で、もう1人が異なる手の場合
        if hand_a == hand_b and hand_a != hand_c:
            return player_c
        elif hand_a == hand_c and hand_a != hand_b:
            return player_b
        elif hand_b == hand_c and hand_b != hand_a:
            return player_a
        else:
            # 3人とも同じ手の場合
            return "引き分け"
    
    results = []
    for _ in range(3):
        hand_a = random.randint(0, 2)
        hand_b = random.randint(0, 2)
        hand_c = random.randint(0, 2)
        winner = judge(hand_a, hand_b, hand_c)
        if winner != "引き分け":
            win_count[winner] += 1
        results.append(f"{player_a}の手︓{HANDS[hand_a]} v.s. {player_b}の手︓{HANDS[hand_b]}"
               f" v.s. {player_c}の手︓{HANDS[hand_c]} → {winner if winner == '引き分け' else '引き分け'}")

    # 勝者を決定する
    max_wins = max(win_count.values())
    winners = [player for player, wins in win_count.items() if wins == max_wins]
    if len(winners) > 1:
        final_result = "総合結果: 引き分け"
    else:
        final_result = f"総合結果: {winners[0]}の勝ち"

    return "\n".join(results + [final_result])

print(janken("A", "B", "C"))