# importing the yfinance package
import sys
import yfinance as yf
from redmail import gmail
from datetime import datetime, date, time, timedelta
import time as other_time
from itertools import chain, repeat
import os


#inputting user email address
amt_recipients = int(input("how many recipients for updates: "))

recipient_list = []
for i in range(amt_recipients):
    each_recipient = input("type email address for update(no school email): ")
    recipient_list.append(each_recipient)
print("recipient list:", recipient_list)

# giving the start and end dates
startDate = '2015-03-01'
endDate = '2100-01-01'


#printing date
today = date.today()
date_today = today.strftime("%B %d, %Y")

#printing time
now = datetime.now()
hr = ("{0:0=2d}".format(now.hour))
min = ("{0:0=2d}".format(now.minute))
sec = ("{0:0=2d}".format(now.second))
day_of_week = now.weekday()
current_time = f"{hr}:{min}:{sec}"
print(current_time)


#start time
start = time(6, 30, 0)
#end time
end = time(13, 0, 0)
#current time
current = now.time()



all_ticks_file = open("all_tickers.txt", "r")
data = all_ticks_file.read()
list_of_tickers = data.split("\n")
#print(list_of_tickers)
all_ticks_file.close()


# setting the ticker value using input(repeats input prompt until string is inputted)
print('----------------------------------------------------------------------------------------------------')
prompts = chain(['Enter the company ticker you want updates for: '], repeat("Typo? Try again: "))
replies = map(input, prompts)
ticker = next(filter(str.isalpha, replies))
ticker = ticker.upper()

for i in range(1):
    if ticker not in list_of_tickers:
        print('**TYPE A VALID TICKER SYMBOL**')
        python = sys.executable
        os.execl(python, python, *sys.argv)
    else:
        break

gmail.username = 'periodicstockpriceupdatebot@gmail.com' # the gmail address that sends the email
gmail.password = 'devnrmalzichyjwk'#gmail app password


# gets the professional name of the company
long_name = yf.Ticker(ticker).info['longName']





stock = yf.Ticker(ticker)
current_price = (round((stock.history(period='1d').iloc[-1]['Close']), 2))
'''print(current_price)'''
previous_close = (round(stock.history(period='2d').iloc[-2]['Close'], 2))
'''print(previous_close)'''



print("*Price is inclusive for the range*")
range_inp_low = float(input(f"Type low range price for updates({current_price}): "))
range_inp_high = float(input(f"Type high range price for updates({current_price}): "))




def in_range_email():
    if start <= current <= end:



        if range_inp_low <= current_price <= range_inp_high and '''((prices_list.count(target_price)) == occur_input)''':
            gmail.send(
                subject=f"({ticker})MARKET OPEN on {date_today} at {current_time}",
                receivers=recipient_list,
                text=f"UPDATE:\n{long_name} stock price: \n\nPrice in range of ({range_inp_low} to {range_inp_high}): ${current_price}"
            )
            print('----------------------------')
            print('**EMAIL SENT (check spam)**')
            print('----------------------------')
            sys.exit()


def close_email():
    if now.time().hour >= 13 or 6 >= now.time().hour:
        gmail.send(
            subject=f"({ticker})MARKET Closed on {date_today} at {current_time}",
            receivers=recipient_list,
            text=f"{long_name} stock price\nOn {date_today} at {current_time}: \n\nCLOSED price:  ${current_price} \nPREVIOUS DAY'S CLOSED PRICE: {previous_close} \nCLOSE PRICE TOMORROW(PREDICTION): |placeholder|"
        )
        print('----------------------------')
        print('**EMAIL SENT (check spam)**')
        print('----------------------------')
        sys.exit()

    if day_of_week == 5 or day_of_week == 6:
        print('''
    ___________________________________________________________________________
             ||
             ||
            _||
           /__)
          / /||
         / / // .--.
         \ \// / (OO)
          \//  |( O )    ***stock market closed go away
          // \__/`-'\__
         // \__      _ |
     _.-'/    | ._._.|\ |
    (_.-'     |      \ \ |
       .-._   /      / / /
      /_ \ \ /   \__/ / /
        \ \_/   / /  (_/
         \     / /
          `-._/-' 
        ''')

        gmail.send(
            subject=f"({ticker})MARKET Closed on {date_today} at {current_time}",
            receivers=recipient_list,
            text=f"{long_name} stock price\nOn {date_today} at {current_time}: \n\nCLOSED price:  ${current_price} \nPREVIOUS DAY'S CLOSED PRICE: {previous_close} \nCLOSE PRICE TOMORROW(PREDICTION): |placeholder|"
        )
        print('----------------------------')
        print('**EMAIL SENT (check spam)**')
        print('----------------------------')

        sys.exit()


close_email()


while True:
    try:
        target_price = float(input(f"Type the target price for {date_today} (current price is {current_price}): "))
    except ValueError:
        print("Typo? Try again... ")
        print(' ')
        continue
    else:
        break


prices_list = []


occur_input = int(input('after how many occurrences would you like to receive your updates: '))
sleep_time = float(input('how long would you like to wait before receiving your emails(min): '))

for i in range(100000):

    now = datetime.now()
    hr = ("{0:0=2d}".format(now.hour))
    min = ("{0:0=2d}".format(now.minute))
    sec = ("{0:0=2d}".format(now.second))
    current_time = f"{hr}:{min}:{sec}"

    other_time.sleep(1)
    current_price = (round((stock.history(period='1d').iloc[-1]['Close']), 2))
    prices_list.append(current_price)
    prices_set = set(prices_list)
    print(prices_set)

    if len(prices_set) == 20:
        prices_set = {}

    print(f'price added: {(current_price)}')
    print(f'{(prices_list.count((current_price)))} times')
    print()

    in_range_email()

    if target_price in prices_set and ((prices_list.count(target_price)) == occur_input):
        print('-------------------------------')
        print(prices_set)
        print('-------------------------------')

        if start <= current <= end:
            gmail.send(
                subject=f"({ticker})MARKET OPEN on {date_today} at {current_time}",
                receivers=recipient_list,
                text=f"UPDATE:\n{long_name} stock price: \n\nTARGET PRICE REACHED: ${current_price}"
            )
            print('----------------------------')
            print('**EMAIL SENT (check spam)**')
            print('----------------------------')
            sys.exit()

            other_time.sleep((sleep_time * 60))

        prices_set.remove(target_price)
        prices_list = list(prices_set)
        print(prices_list)

    close_email()


'''
#checking if current time is between start and end time
if start <= current <= end:
    gmail.send(
        subject=f"({ticker})MARKET OPEN",
        receivers=recipient_list,
        text=f"UPDATE:\n{long_name} stock price\n{date_today}\n{current_time}: \n\n${current_price}"
    )

else:
    gmail.send(
        subject=f"({ticker})MARKET CLOSED",
        receivers=recipient_list,
        text=f"{ticker} stock CLOSED PRICE on {date_today} at {current_time}: \n\nCLOSED price:  ${current_price} \n"
'''





























'''if ((int(hour_check) >= 13)) or (6 <= int(hour_check) and int(minute_check) == 30):'''

"""# And then you can send emails
    gmail.send(
        subject=f"APPLE stock Periodic Update",
        receivers=recipient_list,
        text=f"AAPL stock on {date_today} at {current_time}: \nCurrent price:  ${current_price}"
    )"""
