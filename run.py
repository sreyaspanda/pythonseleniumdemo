from booking.booking import Booking
import time

try:
    with Booking(teardown=True) as bot:
        bot.land_first_page()
        bot.change_currency(currency='INR')
        bot.select_places_to_go('New Delhi')
        bot.select_dates(check_in_date='2022-09-11', check_out_date='2022-09-15')
        bot.select_adults(4)
        bot.click_search()
        bot.apply_filterations()
        bot.refresh()
        time.sleep(5)
        bot.report_results()
    
except Exception as e:
    if 'in PATH' in str(e):
        print('''
            You are trying to run the bot from command line\n
            Please add to PATH your selenium drivers\n
            Windows:\n
            \t set PATH = %PATH%; C:path-to-your-folder\n
            Linux:\n
            \t PATH = $PATH:/path/toyour/folder/\n
        ''')
    else:
        raise
    