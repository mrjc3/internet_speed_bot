from internetspeed import InternetSpeedBot


PROVIDER = input("Who is your current internet provider?  ")
PROMISED_DOWN = float(input("What is the promised download speed?  "))
PROMISED_UP = float(input("What is the promised upload speed?  "))

# # Create bot
bot = InternetSpeedBot()

# # Start the speed test
bot.get_internet_speed()

# tweets at provider if current speeds are below promised speeds
if float(bot.down) < PROMISED_DOWN:
    bot.tweet_at_provider(PROVIDER)
