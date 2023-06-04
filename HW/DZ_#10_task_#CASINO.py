import random


class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bet_amount = 0
        self.bet_number = 0
        self.bet_color = ''

    def place_bet(self, amount, number, color):
        self.bet_amount = amount
        self.bet_number = number
        self.bet_color = color

    def win(self, amount):
        self.balance += amount

    def lose(self, amount):
        self.balance -= amount


class RouletteGame:
    def __init__(self):
        self.players = []
        self.winning_number = 0
        self.winning_color = ''

    def add_player(self, player):
        self.players.append(player)

    def spin_wheel(self):
        self.winning_number = random.randint(0, 36)
        self.winning_color = 'red' if self.winning_number % 2 == 0 else 'black'

    def play_round(self):
        for player in self.players:
            print(f"Игрок: {player.name}")
            print(f"Баланс: {player.balance}")
            amount = int(input("Сделайте свою сумму ставки: "))
            number = int(input("Выберите число для ставки (0-36): "))

            if number != 0:
                color = input("Выберите цвет для ставки (red/black): ")
            else:
                color = ''

            if amount > player.balance:
                print("Недостаточный баланс. Сумма ставки не может превышать баланс.")
                break

            player.place_bet(amount, number, color)

        self.spin_wheel()
        print(f"Выигрышный номер: {self.winning_number}")
        print(f"Выигрышный цвет: {self.winning_color}")

        for player in self.players:
            if player.bet_number == self.winning_number and player.bet_color == self.winning_color:
                winnings = player.bet_amount * 36 * 2
                player.win(winnings)
                print(f"{player.name} выиграл {winnings}!")
            elif player.bet_number == self.winning_number or player.bet_color == self.winning_color:
                winnings = player.bet_amount * 36
                player.win(winnings)
                print(f"{player.name} выиграл {winnings}!")
            else:
                player.lose(player.bet_amount)
                print(f"{player.name} проиграл {player.bet_amount}!")

            if player.balance < 0:
                print(f"{player.name} имеет отрицательный баланс. Игра завершена.")
                return

            print(f"{player.name} баланс: {player.balance}")
            print()

    def play_game(self):
        while True:
            choice = input("Введите 'p', чтобы сыграть раунд, или 'q', чтобы выйти: ")

            if choice == 'p':
                self.play_round()
            elif choice == 'q':
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
                continue


# Создаем игроков
player1 = Player("Игрок 1", 1000)
player2 = Player("Игрок 2", 1500)

# Создаем игру в рулетку
game = RouletteGame()

# Добавляем игроков в игру
game.add_player(player1)
game.add_player(player2)

# Запускаем игру
game.play_game()