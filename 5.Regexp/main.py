from pprint import pprint
import re
import csv


class WriteRead:
    def read_(self, file_="phonebook_raw.csv", delimeter=',', encoding='utf-8'):
        with open(file_, 'r', encoding=encoding) as f:
            rows = csv.reader(f, delimiter=delimeter)
            contacts_list = list(rows)
            return contacts_list

    def write_(self, list_, file_="phonebook.csv", delimeter=',', encoding='utf-8'):
        with open(file_, "w", encoding=encoding) as f:
            datawriter = csv.writer(f, delimiter=delimeter)
            datawriter.writerows(list_)


class Data:

    def chenge_phone(self, regex):
        phone_new = f'{regex[1] if regex[1] == "+7" else "+7"}({regex[2]}){regex[3]}-{regex[4]}-{regex[5]}'
        phone_ext = f' доб.{regex[6]}'
        return phone_new + phone_ext if str(regex[6]).isdigit() else phone_new

    def get_contact_list(self, contacts_list):
        contacts = {}
        for i in range(1, len(contacts_list)):
            fio = contacts_list[i][0] + contacts_list[i][1] + contacts_list[i][2]
            fio = re.findall(r'([А-ЯЁ][а-яё]*) ?([А-ЯЁ][а-яё]*) *([А-ЯЁ][а-яё]*)*', fio)
            organisation = contacts_list[i][3]
            position = contacts_list[i][4]
            phone = contacts_list[i][5]
            phone = re.sub(r'([+]?[7]|[8])[( ]*(\d{3})[) -]*(\d{3})[ -]?(\d{2})[ -]?(\d{2}) *\S* *(\d{4})?.*',
                           self.chenge_phone, phone)
            mail = contacts_list[i][6]

            if fio[0][0] not in contacts:
                contacts[fio[0][0]] = [fio[0][0], fio[0][1], fio[0][2], organisation, position, phone, mail]
            else:
                contacts[fio[0][0]] += [fio[0][0], fio[0][1]]
                contacts[fio[0][0]] += [fio[0][2] if contacts[fio[0][0]][2] == '' else contacts[fio[0][0]][2]]
                contacts[fio[0][0]] += [organisation if contacts[fio[0][0]][3] == '' else contacts[fio[0][0]][3]]
                contacts[fio[0][0]] += [position if contacts[fio[0][0]][4] == '' else contacts[fio[0][0]][4]]
                contacts[fio[0][0]] += [phone if contacts[fio[0][0]][5] == '' else contacts[fio[0][0]][5]]
                contacts[fio[0][0]] += [mail if contacts[fio[0][0]][6] == '' else contacts[fio[0][0]][6]]

            headings = [['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']]
            data = [i[-7:] for k, i in contacts.items()]
            result_list = [*headings, *data]
        return result_list


if __name__ == '__main__':
    file = WriteRead()
    data = Data()

    file.write_(data.get_contact_list(file.read_()))

