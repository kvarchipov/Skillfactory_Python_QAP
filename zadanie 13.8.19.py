print("""Здравствуйте! Программа принимает только цифры. Пожалуйста не пытайтесь вводить значения прописью.
Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
От 18 до 25 лет — 990 руб.
От 25 лет — полная стоимость 1390 руб.
При регистрации более чем 3 участников, скидка 10%!""")
number_of_tickets = int(input("Сколько билетов Вы желаете приобрести: "))
receipt = 0
registered_person = 0
for i in range(number_of_tickets):
    print("Пожалуйста, введите возраст", i+1, "участника: ")
    age_person = int(input())
    if 0 > age_person or age_person > 150:
        print("Проверте корректность вводимых данных.")
    elif age_person < 18:
        registered_person += 1
    elif age_person < 25:
        receipt += 990
        registered_person += 1
    else:
        receipt += 1390
        registered_person += 1
if registered_person > 2:
    print("Зарегестрированно", registered_person, "участников. Вам полагается скидка 10%! К оплате -", receipt / 10 * 9, "руб.")
elif registered_person == 1:
    print("Зарегестрирован", registered_person, "участник. К оплате -", receipt, "руб.")
else:
    print("Зарегестрированно", registered_person, "участников. К оплате -", receipt, "руб.")
