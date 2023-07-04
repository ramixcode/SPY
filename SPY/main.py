import random
import time
import math
import os
from tqdm import tqdm
import keyboard
from pyfiglet import Figlet

select_Language_checker = 0
Select_option_checker = 0

words_list = ["Code (کد)","Message (پیام)","Spy (جاسوس)","Mission (ماموریت)","Map (نقشه)","Stealth (پنهانی)","Tracking (ردیابی)","Security (امنیت)","Assassination (ترور)","Intelligence (اطلاعات استخباراتی)","Toolkit (ابزارک)","Agent (عامل)","Cover (پوشش)","Encryption (رمزگذاری)","Equipment (تجهیزات)","Hideout (سرپناه)","Special Forces (نیروهای ویژه)","Undercover (مخفی‌کاری)","Footprint (ردپایی)","File (پرونده)","Traffic (ترافیک)","Communication (ارتباطات)","Dangerous (خطرناک)","Espionage (جاسوسی)","Security (امنیت)","Tracker (ردیاب)","Hidden (پنهان)","Operation (عملیات)","Target Sequence (توالی هدف)","Protection (محافظت)","Identification (شناسایی)","Adventure (ماجراجویی)","Sneaky (پنهانی)","Confidential (محرمانه)","Mask (ماسک)","Authentication (احراز هویت)","Transfer (انتقال)","Security Reinforcement (تقویت امنیت)","Mapping (نقشه‌برداری)","Rescue (نجات)","Threat (تهدید)","Embassy (سفارتخانه)","Classified Documents (اسناد رده‌بندی شده)","Black Box (جعبه سیاه)","Communication (ارتباطات)","Agent (عامل)","Telecommunications (مخابرات)","Security Service (خدمات امنیتی)","Encrypted Message (پیام رمزگذاری شده)","Rope Climbing (طناب کشیدن)","Strategy (استراتژی)","Control (کنترل)","Information System (سیستم اطلاعات)","Explorer (کاوشگر)","Sensitive Information (اطلاعات حساس)","Pursuit (تعقیب)","Communication Network (شبکه‌ی ارتباطی)","Spy-like (مانند جاسوس)","Covert Exercises (تمرینات مخفی)","Encrypted Communication (ارتباط رمزگذاری شده)","Secret Operation (عملیات مخفی)","Prevention (جلوگیری)","Care (مراقبت)","Measurement (اندازه‌گیری)","Location Map (نقشه مکان)","Underground (زیرزمینی)","Decoder (رمزگشایی کننده)","Planning (برنامه‌ریزی)","Secret Mission (ماموریت مخفی)","Secret Coding (کدنویسی محرمانه)","Network Security (امنیت شبکه)","Information Operation (عملیات اطلاعاتی)","Secret (مخفی)","Hidden Agenda (اهداف پنهان)","Decryption (رمزگشایی)","Covert Mapping (نقشه‌برداری مخفی)","Investigation (تحقیق)","Confidential Communication (ارتباطات محرمانه)","Military Espionage (جاسوسی نظامی)","Effort (تلاش)","Military Intelligence (اطلاعات نظامی)","Coded Communication (ارتباط رمزگذاری شده)","Assault (حمله)","Concealment (پنهان کاری)","Secret Documents (اسناد محرمانه)","Spy Tracking (ردیابی جاسوس)","Risk-taking (پذیرفتن خطر)","Encoder (رمزگذار)","Expert (کارشناس)","Armaments (تجهیزات نظامی)","Spy Equipment (تجهیزات جاسوسی)","Search (جستجو)","Terrorism (تروریسم)","Covert Communication (ارتباط مخفی)","Industrial Espionage (جاسوسی صنعتی)","Guide (راهنما)","Terrorist (تروریست)","Politics (سیاست)","Investigation (تحقیق)"]

players = []

roles = ['spy', 'location']

spy_checker = 0

location_removed_checker = 0

first_person_checker = 0

location_checker = 0

removed = []

removed_int = []

spy_removed_checker = 0

random_location = random.choice(words_list)

from pyfiglet import Figlet
name = '''
r a m i x c o d e
         S P Y
'''
f = Figlet(font='slant')
ascii_art = f.renderText(name)
print(ascii_art)
print('''
You can find me on social media
Instagram : ramixcode
Telegram : ramixcode
Github : ramixcode
''')
print
print('----------------------------------------------')
print("WLC TO SPY GAME")
while True:
    try:
        if select_Language_checker == 0:
            select_Language = int(input("Please Select the language.\n1)english\n2)Persian(finglish)\n==>"))
            select_Language_checker =+ 1

        if select_Language == 2:
            print("not available yet")
            continue

        if select_Language == 1:
            if Select_option_checker == 0:
                Select_option = int(input("Select an option to continue.\n1)New Game\nabout us\n==>"))
                Select_option_checker =+ 1

            if Select_option == 1:
                number_of_player = int(input("Enter the number of players:"))
                if number_of_player < 3:
                    print(f"The number of players you have entered is {number_of_player} and this value is less than 3. Please enter a number greater than 3.")
                    continue
                
                A_quarter_of_the_players = number_of_player / 3

                result_number_of_player = math.floor(A_quarter_of_the_players)

                number_of_spies = int(input("Enter the number of spies:"))

                if number_of_spies > result_number_of_player:
                    print("The number of spies must be less than or equal to a quarter of the total number of players.")
                    continue
               
                for i in range(0, number_of_player):

                    print("are you ready for see role?(Press Enter)")
                    keyboard.wait('enter')

                    os.system('cls')
                    
                    random_playerforrole = random.choice(roles)

                    
                    if spy_checker < number_of_spies:    
                        if random_playerforrole == 'spy':
                            spy_checker =+ 1
                            print(f"your role is {random_playerforrole}")

                            print("if you see your role press enter")
                            keyboard.wait('enter')
                    
                            os.system('cls')
                            continue
                        
                    if location_checker < (number_of_player - number_of_spies):
                        if random_playerforrole == 'location':
                            print(f"word is {random_location}")
                            location_checker =+ 1
                            print("if you see your role press enter")
                            keyboard.wait('enter')

                            os.system('cls')
                            continue
                    
                    if spy_checker == number_of_spies:
                        print(f"word is {random_location}")
                        print("if you see your role press enter")
                        keyboard.wait('enter')

                        os.system('cls')
                        continue

                    if location_checker == (number_of_player - number_of_spies):
                        print("your role is spy")
                        print("if you see your role press enter")
                        keyboard.wait('enter')

                        os.system('cls')
                        continue
                        


                all_players = number_of_player
                for t in range(0,3):
                    print(f"Game Start in {t + 1}")
                    time.sleep(1)


            while all_players > 2:
                for i in range(0, number_of_player):
                    if i + 1 not in removed_int:
                        print(f"player{i + 1} can ask questions.\nIf he asked the question.")
                        print("press enter")
                        keyboard.wait('enter')

                for i in range(1, number_of_player + 1):
                    if i not in removed_int:
                        print(f"Vote for the player {i}")
                        duration = 5
                        progress_bar = tqdm(total=duration, desc='Voting ends in')

                        start_time = time.time()
                    while time.time() - start_time < duration:

                        progress_bar.update(1)
                        time.sleep(0.1)  

                    
                    progress_bar.close()

                which_kick = int(input("Ask the person who was deleted, was he/she a spy?\n1)yes\n2)no\n3)No one was eliminated\n==>"))
                if which_kick == 1 or which_kick == 2:
                    L = input("who?what is him/her number?")
                    removed.append(L)
                    for string in removed:
                        integer = int(string)
                        removed_int.append(integer)


                if which_kick == 1:
                    spy_removed_checker =+ 1

                if which_kick == 2:
                    location_removed_checker =+ 1

                if spy_removed_checker == number_of_spies:
                    print('game is over spies are lose')
                    break

                if location_removed_checker == (number_of_player - number_of_spies):
                    print('game is over. spies win')
                    break

    except Exception as error:
        print("Insert the correct entry!!!")