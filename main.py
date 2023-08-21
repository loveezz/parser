from Bot.TgBot import TgBot
from Data import API_KEY

if __name__ == "__main__":
    Bot = TgBot(API_KEY)
    Bot.start()
