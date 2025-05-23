def get_choices():
    return {
        "あ": [
            "朝から驚きの連続だ",
            "あっという間に時間が過ぎる",
            "明るい声が響き渡る",
        ],
        "い": [
            "いつもの朝とは様子が違う",
            "意味深な笑みを浮かべて",
            "今こそ冒険の始まり",
        ],
        "う": [
            "嬉しい知らせが飛び込んできた",
            "運命的な出会いを果たした",
            "海の向こうへ思いを馳せる",
        ],
        "え": [
            "駅で急に待ち合わせ。慌てて準備して",
            "笑顔がこぼれる瞬間だった",
            "遠くの空に虹がかかった",
        ],
        "お": [
            "温泉旅行に出発だ！",
            "思い切って声をかけた",
            "大きな夢に向かって走り出す",
        ],
    }


def main():
    print("=== 選んで作る！あいうえお作文 ===")
    choices = get_choices()
    selected_lines = {}

    for syllable in ["あ", "い", "う", "え", "お"]:
        print(f"\n{syllable} の候補：")
        for idx, option in enumerate(choices[syllable], 1):
            print(f"{idx}. {option}")

        while True:
            try:
                selection = int(input(f"{syllable} に選ぶ文の番号（1〜3）: "))
                if 1 <= selection <= 3:
                    selected_lines[syllable] = choices[syllable][selection - 1]
                    break
                else:
                    print("1〜3の番号を選んでください。")
            except ValueError:
                print("数字で入力してください。")

    print("\n--- あなたの あいうえお作文 ---")
    for syl in ["あ", "い", "う", "え", "お"]:
        print(f"{syl}：{selected_lines[syl]}")


if __name__ == "__main__":
    main()
