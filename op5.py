start=''
from datetime import datetime
time_encrypt = datetime.now().strftime('%c')          # переменная времени
time_encrypt = time_encrypt[-4:] + time_encrypt[3:-4] # нужный мне формат
while True:
    if start=='':
        start=input('''
If you need encrypt text write me    (1)
If you need decrypt text write me    (2)
if you want to finsh write me        (0)''')

    if start=='1':
        text=input('\nWrite me your text!')

        t = len(text)       # переменная длинна строки
        tt = t % 2          # переменная четность строки и вычесления половинны от нее
        a = 0               # переменная для строки прохода по каждому символу
        i = 0               # переменная цыклов
        d  = 0              # переменная количества букв в строке
        s  = 0              # переменная количества букв в строке
        ss = 0              # переменная количества спец символов
        text_1 = ''         # переменная для первого уровня шифрования
        text_2 = ''         # переменная второго уровня шифрования

        if tt == 1:
            tt = int((t - 1) / 2)
        else:
            tt = int(t / 2)
        # переменая для 3 уровня шифрования если длина четная делим на 2 если длина не четная отнимаем 1 и делим на 2

        while i < t:
            if text[i].isalpha() == True:  # выявление кол букв в строке
                s += 1
            elif text[i].isdigit() == True:  # выявления кол цыфр в строке
                d += 1
            elif text[i].isalnum() == False:  # выявления кол спец символов
                ss += 1
            i += 1
        i = 0 # Обнуляем переменую цыкла

        print('\nFirst level encryption!')
        while i < t:
            while a < t:
                b = text[a]
                if 'a' <= b <= 'y' or 'A' <= b <= "Y":
                    tex = chr(ord(b) + 1)
                elif b == 'z':
                    tex = 'a'
                elif b == 'Z':
                    tex = 'A'
                elif '0' <= b <= '8':
                    tex = chr(ord(b) + 1)
                elif b == '9':
                    tex = '0'
                else:
                    tex = b

                a += 1
                text_1 += tex
            text = text_1
            text_1 = ''
            a = 0
            i += 1
            print('-'*i)
        i = 0 # Обнуляем переменую цыкла

        print('\nSecond level encryption!')
        while i < t:
            b = ord(text[i])
            if 97 <= b <= 122:
                b1 = chr(b - 64)
            elif 65 <= b <= 71:
                b1 = chr(b - 7)
            elif 72 <= b <= 76:
                b1 = chr(b + 19)
            elif 77 <= b <= 90:
                b1 = chr(b + 23)
            elif 48 <= b <= 57:
                b1 = chr(b + 66)
            elif 33 <= b <= 47:
                b1 = chr(b + 37)
            elif b == 32:
                b1 = chr(85)

            i += 1
            text_2 += b1
            print('-'*i)
        i = 0 # Обнуляем переменую цыкла


        print('\nThird level encryption!')
        text = text_2[::-1]
        print('-')
        if t >1:
            text = text[tt - 1::-1] + text[tt::]
            print('--')
        i = 0 # Обнуляем переменую цыкла

        open('message_encrypt.txt', 'a+', encoding='utf8')
        file_read_1 = open('message_encrypt.txt', encoding='utf8').read()
        file_read_len = len(file_read_1)

        len_read = 1
        while i < file_read_len:
            if file_read_1[i] == '\n':
                len_read += 1
            i += 1
        i = 0 # Обнуляем переменую цыкла

        file = open('message_encrypt.txt', 'a+', encoding='utf8').write('\n'+str(len_read)+'. ' + text)
        # cтрока в документе которая тобой шифруеться так как в докемент идет до запись

        file_read_1 = open('message_encrypt.txt', encoding='utf8').read()
        file_read_len = len(file_read_1)

        len_read = 0
        while i < file_read_len:
            if file_read_1[i] == '\n':
                len_read += 1
            i += 1
        i = 0 # Обнуляем переменую цыкла

        file_2 = open('key_data.txt', 'a+', encoding='utf8').write('\n' + f'''
Number of symbol in your text            :{t} 
Number of digits in your text            :{d} 
Number of litters in your text           :{s} 
Number of S.symbol in your text          :{ss} 
Creation time                            :{time_encrypt} 
Encrypted string number in the document  :{len_read}''')

        print(f'''
Your text is encrypted                  : {text} 
Number of symbol in your text           : {t} 
Number of digits in your text           : {d} 
Number of litters in your text          : {s} 
Number of S.symbol in your text         : {ss} 
Encrypted string number in the document : {len_read}
Creation time                           : {time_encrypt} ''')


        start=input('''
If want new encrypt write me    (1)
If want decrypt write me        (2)
if want finish program write me (0)''')
        if start == '1':
            start = '1'
            continue
        elif start == '2':
            start='2'
            continue
        elif start == '0':
            break
        else:
            start=''
            continue




    elif start=='2':
        while True:
            decryption=input('''
Do You want decrypted your text via input! Write me                         :(1)
Do You want decrypted your text using record number str in file! Write me   :(2)
If do You want decrypt all write me                                         :(3)      
Do You want to go back! Write me                                            :(4)
Do You want finish program! Write me                                        :(0)''')
            if decryption == '1':
                text = input('\nWrite me your text!')

                t=len(text)

                tt = t % 2  # переменная четность строки и вычесления половинны от нее
                a = 0  # переменная для строки прохода по каждому символу
                i = 0  # переменная цыклов
                d = 0  # переменная количества букв в строке
                s = 0  # переменная количества букв в строке
                ss = 0  # переменная количества спец символов
                text_1 = ''  # переменная для первого уровня дешифрования
                text_2 = ''  # переменная второго уровня дешифрования

                if tt==1:
                    tt=int((t-1)/2)
                else:
                    tt=int(t/2)

                if t > 1:
                    text=text[tt-1::-1]+text[tt::]
                    print('--')

                text = text[::-1]
                print(text)


                while i < t:
                    b = ord(text[i])
                    if 33 <= b <= 57:
                        b1 = chr(b + 64)

                    elif 58 <= b <= 64:
                        b1 = chr(b + 7)

                    elif 91 <= b <= 96:
                        b1 = chr(b - 19)

                    elif 100 <= b <= 113:
                        b1 = chr(b - 23)

                    elif 114 <= b <= 123:
                        b1 = chr(b - 66)

                    elif 70 <= b <= 84:
                        b1 = chr(b - 37)

                    elif b == 85:
                        b1 = chr(32)

                    i += 1
                    text_2 += b1
                    print('-' * i)
                i = 0  # Обнуляем переменую цыкла
                text=text_2


                while i < t:
                    while a < t:
                        b = text[a]
                        if 'b' <= b <= 'z' or 'B' <= b <= "Z":
                            tex = chr(ord(b) - 1)
                        elif b == 'a':
                            tex = 'z'
                        elif b == 'A':
                            tex = 'Z'
                        elif '1' <= b <= '9':
                            tex = chr(ord(b) - 1)
                        elif b == '0':
                            tex = '9'
                        else:
                            tex = b

                        a += 1
                        text_1 += tex
                    text = text_1
                    text_1 = ''
                    a = 0
                    i += 1
                    print('-' * i)
                i = 0  # Обнуляем переменую цыкла

                while i < t:
                    if text[i].isalpha() == True:  # выявление кол букв в строке
                        s += 1
                    elif text[i].isdigit() == True:  # выявления кол цыфр в строке
                        d += 1
                    elif text[i].isalnum() == False:  # выявления кол спец символов
                        ss += 1
                    i += 1
                i = 0  # Обнуляем переменую цыкла
                print(f'''
Compare the date of the text encryption with the date of the key!!!

Your text is decrypted                  : {text}
Number of symbol in your text           : {t} 
Number of digits in your text           : {d} 
Number of litters in your text          : {s} 
Number of S.symbol in your text         : {ss} ''')


            elif decryption == '2':
                text = input('\nWrite me your line number!')
                tpt=len(text)
                file=open('message_encrypt.txt', encoding='utf8')
                file=file.read()

                f_find=file.find('\n'+text)
                f_find2 = file.find('\n' + str(int(text)+1))

                f_find=f_find+tpt+3


                if f_find2==-1:
                    text = (file[f_find:])
                else:
                    text = (file[f_find:f_find2])

                t = len(text)

                tt = t % 2  # переменная четность строки и вычесления половинны от нее
                a = 0  # переменная для строки прохода по каждому символу
                i = 0  # переменная цыклов
                d = 0  # переменная количества букв в строке
                s = 0  # переменная количества букв в строке
                ss = 0  # переменная количества спец символов
                text_1 = ''  # переменная для первого уровня дешифрования
                text_2 = ''  # переменная второго уровня дешифрования

                if tt == 1:
                    tt = int((t - 1) / 2)
                else:
                    tt = int(t / 2)

                if t > 1:
                    text = text[tt - 1::-1] + text[tt::]
                    print('--')

                text = text[::-1]
                print(text)

                while i < t:
                    b = ord(text[i])
                    if 33 <= b <= 57:
                        b1 = chr(b + 64)

                    elif 58 <= b <= 64:
                        b1 = chr(b + 7)

                    elif 91 <= b <= 96:
                        b1 = chr(b - 19)

                    elif 100 <= b <= 113:
                        b1 = chr(b - 23)

                    elif 114 <= b <= 123:
                        b1 = chr(b - 66)

                    elif 70 <= b <= 84:
                        b1 = chr(b - 37)

                    elif b == 85:
                        b1 = chr(32)

                    i += 1
                    text_2 += b1
                    print('-' * i)
                i = 0  # Обнуляем переменую цыкла
                text = text_2

                while i < t:
                    while a < t:
                        b = text[a]
                        if 'b' <= b <= 'z' or 'B' <= b <= "Z":
                            tex = chr(ord(b) - 1)
                        elif b == 'a':
                            tex = 'z'
                        elif b == 'A':
                            tex = 'Z'
                        elif '1' <= b <= '9':
                            tex = chr(ord(b) - 1)
                        elif b == '0':
                            tex = '9'
                        else:
                            tex = b

                        a += 1
                        text_1 += tex
                    text = text_1
                    text_1 = ''
                    a = 0
                    i += 1
                    print('-' * i)
                i = 0  # Обнуляем переменую цыкла

                while i < t:
                    if text[i].isalpha() == True:  # выявление кол букв в строке
                        s += 1
                    elif text[i].isdigit() == True:  # выявления кол цыфр в строке
                        d += 1
                    elif text[i].isalnum() == False:  # выявления кол спец символов
                        ss += 1
                    i += 1
                i = 0  # Обнуляем переменую цыкла
                print(f'''
Compare the date of the text encryption with the date of the key!!!

Your text is decrypted                  : {text}
Number of symbol in your text           : {t} 
Number of digits in your text           : {d} 
Number of litters in your text          : {s} 
Number of S.symbol in your text         : {ss} ''')





            elif decryption == '3':
                txt = '1'
                tpt = len(txt)
                f_find2=0

                while f_find2>=0:
                    file = open('message_encrypt.txt', encoding='utf8')
                    file = file.read()

                    f_find = file.find('\n' + str(txt))
                    f_find2 = file.find('\n' + str(int(txt) + 1))

                    f_find = f_find + tpt + 3

                    if f_find2 == -1:
                        text = (file[f_find:])
                    else:
                        text = (file[f_find:f_find2])

                    t = len(text)
                    tt = t % 2  # переменная четность строки и вычесления половинны от нее
                    a = 0  # переменная для строки прохода по каждому символу
                    i = 0  # переменная цыклов
                    d = 0  # переменная количества букв в строке
                    s = 0  # переменная количества букв в строке
                    ss = 0  # переменная количества спец символов
                    text_1 = ''  # переменная для первого уровня дешифрования
                    text_2 = ''  # переменная второго уровня дешифрования
                    print(txt, '1.',text)

                    if tt == 1:
                        tt = int((t - 1) / 2)
                    else:
                        tt = int(t / 2)

                    if t > 1:
                        text = text[tt - 1::-1] + text[tt::]

                    text = text[::-1]

                    while i < t:
                        b = ord(text[i])
                        if 33 <= b <= 57:
                            b1 = chr(b + 64)

                        elif 58 <= b <= 64:
                            b1 = chr(b + 7)

                        elif 91 <= b <= 96:
                            b1 = chr(b - 19)

                        elif 100 <= b <= 113:
                            b1 = chr(b - 23)

                        elif 114 <= b <= 123:
                            b1 = chr(b - 66)

                        elif 70 <= b <= 84:
                            b1 = chr(b - 37)

                        elif b == 85:
                            b1 = chr(32)

                        i += 1
                        text_2 += b1

                    i = 0  # Обнуляем переменую цыкла
                    text = text_2

                    while i < t:
                        while a < t:
                            b = text[a]
                            if 'b' <= b <= 'z' or 'B' <= b <= "Z":
                                tex = chr(ord(b) - 1)
                            elif b == 'a':
                                tex = 'z'
                            elif b == 'A':
                                tex = 'Z'
                            elif '1' <= b <= '9':
                                tex = chr(ord(b) - 1)
                            elif b == '0':
                                tex = '9'
                            else:
                                tex = b

                            a += 1
                            text_1 += tex
                        text = text_1
                        text_1 = ''
                        a = 0
                        i += 1

                    i = 0  # Обнуляем переменую цыкла

                    while i < t:
                        if text[i].isalpha() == True:  # выявление кол букв в строке
                            s += 1
                        elif text[i].isdigit() == True:  # выявления кол цыфр в строке
                            d += 1
                        elif text[i].isalnum() == False:  # выявления кол спец символов
                            ss += 1
                        i += 1
                    i = 0  # Обнуляем переменую цыкла
                    print(txt,'1.',text, '\n')
                    txt= int(txt)+1
                    f5=open('Decrypt_all.txt', 'a+', encoding='utf8').write('\n'+text)
                print('''
Your text all decryption!!! 
I saved it in the file: Decrypt_all.txt''')


            elif decryption == '4':
                start=''
                break
            elif  decryption =='0':
                start='0'
                break
            else:
                continue


    elif start=='0':
        break
    else:
        start=''
        continue
