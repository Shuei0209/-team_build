import random
import time

symbols = ["🍒", "🍋", "🔔", "⭐", "🍇", "💎"]


def spin():
    return [random.choice(symbols) for _ in range(3)]


def check_win(slots):
    if slots[0] == slots[1] == slots[2]:
        return True
    return False


def payout(symbol):
    # シンボルごとの配当倍率
    payout_table = {"🍒": 5, "🍋": 4, "🔔": 8, "⭐": 10, "🍇": 6, "💎": 20}
    return payout_table.get(symbol, 0)


def main():
    money = 100  # 初期所持金

    print("=== 🎰 スロットゲームへようこそ！ ===")
    print("シンボルを3つ揃えると勝ち！\n")

    while money > 0:
        print(f"\n💰 現在の所持金: {money}円")
        try:
            bet = int(input("ベット額を入力（0で終了）："))
            if bet == 0:
                break
            if bet > money:
                print("所持金が足りません！")
                continue
            if bet < 1:
                print("ベット額は1円以上にしてください。")
                continue
        except ValueError:
            print("数字を入力してください。")
            continue

        money -= bet
        print("スロットを回しています...")
        time.sleep(1)

        result = spin()
        print("｜ " + " ｜ ".join(result) + " ｜")

        if check_win(result):
            multiplier = payout(result[0])
            win_amount = bet * multiplier
            print(f"🎉 当たり！{result[0]} ×3で{win_amount}円獲得！")
            money += win_amount
        else:
            print("😢 残念、ハズレです。")

    print(f"\n🎮 ゲーム終了！最終所持金：{money}円")


if __name__ == "__main__":
    main()
