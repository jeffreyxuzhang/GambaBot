import tweepy
import random
import keys

client = tweepy.Client(
    consumer_key=keys.api_key,
    consumer_secret=keys.api_key_secret,
    access_token=keys.access_token,
    access_token_secret=keys.access_token_secret
)

def blackjack():
    moves = ["HIT", "STAND", "DOUBLE", "SPLIT"]
    return 'Blackjack move of the day is to: ' + random.choice(moves)

def luckynum():
    lucknum = "Todays lucky numbers are: "
    for x in range(4):
        lucknum += str(random.randrange(1, 50)) + ", "
    
    lucknum += str(random.randrange(1,50))
    return lucknum

def roulette():
    options = ["RED", "BLACK", "EVEN", "ODD", "FIRST 12", "SECOND 12", "THIRD 12", "COL 1", "COL 2", "COL 3", "FIRST HALF", "SECOND HALF"]
    return "Your roulette option of the day is to bet on: " + random.choice(options) + ". However if you are feeling lucky, you can bet on number: " + str(random.randrange(36))

def poker():
    choices = ["check/fold", "limp", "raise"]
    preflop = random.choice(choices)
    if preflop == "raise":
        preflop += " " + str(random.randrange(1,4)) + "x"
    return "Your preflop poker move of the day is: " + preflop

if __name__ == '__main__':
    try:
        str = "Gamba." + '\n' + blackjack() + '\n' + luckynum() + '\n' + roulette() + '\n' + poker()
        client.create_tweet(text=str)
    except Exception as e:
        print(f"An error occurred: {e}")