import gspread


gp = gspread.service_account(filename='resources/aquarel.json')
# Open Google spreadsheet
gsheet = gp.open("AquarelArt")
# Select worksheet
wsheet = gsheet.worksheet("Нейрокартины")
masterClass = gsheet.worksheet("Мастер-класс")
start = gsheet.worksheet("/start")


# добавить значения
def append_name(i, name):
    wsheet.append_row([i, name])


def append_name_start(i):
    start.append_row([i])


def append_name_master(i, name):
    masterClass.append_row([i, name])


# поиск строки и столбца положения значения
def values_row_col(value):
    values = wsheet.get_all_values()
    res = []
    for i, r in enumerate(values):
        for j, c in enumerate(r):
            if str(value) in c:
                res.append({'row': i, 'col': j})
    return res


def values_row_col_master(value):
    print("values_row_col_master")
    values = masterClass.get_all_values()
    res = []
    for i, r in enumerate(values):
        for j, c in enumerate(r):
            if str(value) in c:
                res.append({'row': i, 'col': j})
    return res


# добавления значения
def update_phone(message):
    print("update_phone")
    i = message.chat.id
    print(f"ID: {i}")
    res = values_row_col(i)
    print(res)
    row = res[-1]["row"]+1
    print(f"row: {row}")
    if message.contact is not None:
        print("contact")
        phone = message.contact.phone_number
    else:
        print("text")
        phone = message.text
    wsheet.update(f'C{row}', phone)


def update_phone_master(message):
    print("update_phone_master")
    i = message.chat.id
    res = values_row_col_master(i)
    row = res[-1]["row"]+1
    if message.contact is not None:
        phone = message.contact.phone_number
    else:
        phone = message.text
    masterClass.update(f'C{row}', phone)


def get_all_user():
    values = start.get_all_values()
    users = set()
    for user in values:
        users.add(user[0])
    print(users)
    return list(users)


if __name__ == '__main__':
    values_row_col(value='anna')
