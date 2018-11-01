import random
letters = ['А','Е','Н','О','С','Т']
random.shuffle(letters)
word = ''.join(letters)
word = word[:4]

i = 0
place = 0
place_1 = 0
answer_1 = 'да + yes'
answer_2 = 'no нет -'
answer = 'да'
print('БУКВЫ: А,Е,Н,О,С,Т')
print('Угадайте четырехбуквенное слово из данных букв.')
while answer.lower() in answer_1:
    while i != 10:
        word_1 = input('Введите слово: ')
        i += 1
        if len(word_1) < 4:
            print('Недостаточно букв! Слово состоит из 4 букв!')
        elif len(word_1) > 4:
            print('Слишком много букв! Слово состоит из 4 букв!')
        else:
            word_1 = word_1.upper()
            place = 0
            place_1 = 0

            for j in range(0,4):
                if word_1[j] == word[j]:
                    place += 1
                elif word_1[j] in word and word_1[j] != word[j]:
                    place_1 += 1
                else:
                    place += 0
                    place_1 += 0
            if place == 3:
                print('Вы почти угадали!')
            print('На "своем месте": ', place)
            print('На "чужом месте": ', place_1)

            if i == 10:
                print('Вы проиграли!')
                print('Загаданное слово:', word)
                break

            if place == 4:
                print('Вы выиграли!')
                print('Вы готовы сыграть еще раз?')
                answer = input('Ваш ответ: ')
                if answer.lower() in answer_2:
                    print('Спасибо, что поучаствовали! Приходите еще!')
                    break