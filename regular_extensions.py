import re
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    phone_book = list(rows)


for person in phone_book:
    fio_list = []
    fio = " ".join(person[:3])
    fio_list = fio.split()

    for i in range(len(fio_list)):
        person[i] = fio_list[i]
for i in range(len(phone_book)):
    for j in range(len(phone_book)):
        if phone_book[i][0] == phone_book[j][0] and phone_book[i][1] == phone_book[j][1] \
                and phone_book[i] is not phone_book[j]:
            if phone_book[i][2] == '':
                phone_book[i][2] = phone_book[j][2]
            if phone_book[i][3] == '':
                phone_book[i][3] = phone_book[j][3]
            if phone_book[i][4] == '':
                phone_book[i][4] = phone_book[j][4]
            if phone_book[i][5] == '':
                phone_book[i][5] = phone_book[j][5]
            if phone_book[i][6] == '':
                phone_book[i][6] = phone_book[j][6]

contacts_result = []
for contact in phone_book:
    if contact not in contacts_result:
        contacts_result.append(contact)

for person in contacts_result:
    for i in range(1, len(contacts_result)):
        if 'доб.' in person[5]:
            pattern = r'(\+7|8)\s*\(*(\d+)\)*\s*(\d+)-*(\d+)-*(\d+)\s*\(*[доб.]*\s*(\d+)\)*'
            result = re.sub(pattern, r"+7(\2)\3-\4-\5 доб.\6", person[5])
            person[5] = result
        elif '(' in person[5]:
            pattern = r"(\+7|8)\s*\(*(\d+)\)*\s*(\d+)-*(\d+)-*(\d+)\s*"
            result = re.sub(pattern, r"+7(\2)\3-\4-\5", person[5])
            person[5] = result
        else:
            pattern = r"(\+7|8)\s*(\d\d\d)-*(\d)(\d)(\d)-*(\d)(\d)(\d)(\d)"
            result = re.sub(pattern, r"+7(\2)\3\4\5-\6\7-\8\9", person[5])
            person[5] = result

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_result)
