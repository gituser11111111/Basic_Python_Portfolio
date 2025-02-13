import requests

# yesterday = "http://sandipbgt.com/theastrologer/api/horoscope/{sunsign}/yesterday"
# tomorrow = "http://sandipbgt.com/theastrologer/api/horoscope/{sunsign}/tomorrow"
# today = "http://sandipbgt.com/theastrologer/api/horoscope/{sunsign}/today"
# sunsign_list = "http://sandipbgt.com/theastrologer/api/horoscope/{sunsign}/sunsigns"

signs = requests.get("http://sandipbgt.com/theastrologer/api/sunsigns").json()

sign_dates = {'Aries:': 'March 21 - April 19', 'Taurus:': 'April 20 – May 20', 'Gemini:': 'May 21 – June 20',
              'Cancer:': 'June 21 – July 22', 'Leo:': 'July 23 – August 22',
              'Virgo:': 'August 23 – September 22', 'Libra:': 'September 23 – October 22',
              'Scorpio:': 'October 23 – November 21', 'Sagittarius:': 'November 22 – December 21',
              'Capricorn:': 'December 22 – January 19', 'Aquarius:': 'January 20 – February 18',
              'Pisces:': 'February 19 – March 20'}

i = 1

while i == 1:
    start_input = input("Are you ready to check out your horoscope? \n\n"
                        "Please enter 'yes' or 'no'. ")

    if start_input in {str('yes'), str('Yes'), str('YES')}:
        print('Okay cool! check out the list of zodiac signs and their corresponding dates below! ')
        print('Zodiac sign list below: ')
        print('')

        for key, value in sign_dates.items():
            print(key, value)

        '''another method to print the key, value pairs of sign_date dictionary.
    result = '\n'.join(f'{key}: {value}' for key, value in sign_dates.items())
    print(result)'''

        selectedSign = input('\nWhat sign are you?:\n')

        timeframe = input("Do you want your horoscope for 'today', 'tomorrow', or 'yesterday'? ")

        horoscope = requests.get(f"http://sandipbgt.com/theastrologer/api/horoscope/{selectedSign}/{timeframe}").json()
        print(str(horoscope))

        second_input = input('Pretty cool huh?\n\n'
                             'Would you like to check another timeframe or check another zodiac sign? ')

        if second_input in {str('yes'), str('Yes'), str('YES')}:
            print('Okay cool! Sending you to main menu:')
            i = 1

        elif second_input not in {str('yes'), str('Yes'), str('YES')}:
            print('Okay! Have a good one!')
            break

    elif start_input in {str('no'), str('No'), str('NO')}:
        print('Okay! Have a good one!')
        break

    else:
        print('Oops! Something went wrong. Please try again!')
        i = 1
