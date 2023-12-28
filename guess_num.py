import random

def guess_number_game():
    # 隨機選擇一個1到100之間的數字
    secret_number = random.randint(1, 100)
    attempts = 0
    print("歡迎來到猜數字遊戲! 我已選擇了一個1到100之間的數字。")

    while True:
        # 讓玩家輸入他們的猜測
        guess = input("請輸入你的猜測(1-100): ")

        # 檢查玩家是否輸入了一個數字
        if not guess.isdigit():
            print("請輸入一個有效的數字!")
            continue

        # 轉換猜測為整數
        guess = int(guess)
        attempts += 1

        # 檢查猜測
        if guess < secret_number:
            print("太小了!")
        elif guess > secret_number:
            print("太大了!")
        else:
            print(f"恭喜你! 你在{attempts}次嘗試後猜對了!")
            break

if __name__ == "__main__":
    guess_number_game()
