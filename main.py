import csv
from function import correction_of_info, merge_records



def main():
    # Чтение файла в формате csv
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    general_csv_list = correction_of_info(contacts_list)
    phonebool = merge_records(general_csv_list)
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(phonebool)


if __name__ == '__main__':
   main()