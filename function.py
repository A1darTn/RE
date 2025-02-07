import re

def merge_records(records):
    merged = {}
    
    for record in records:
        # Формируем ключ из ФИО
        full_name = (record[0], record[1], record[2])
        
        # Если ключ уже существует, объединяем записи
        if full_name in merged:
            # Объединяем информацию, игнорируя пустые значения
            for i in range(len(record)):
                if record[i] and record[i] not in merged[full_name][i]:
                    merged[full_name][i] += f"; {record[i]}"
        else:
            # Если ключа нет, добавляем запись
            merged[full_name] = record.copy()
    
    # Преобразуем словарь обратно в список списков
    return list(merged.values())

def correction_of_info(contacts_list_csv: list)-> list:
    phone_pattern = re.compile(r'(?:(?:\+7|8)\s*)?\(?(\d{3})\)?\s*[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})(?:\s*доб\.\s*(\d+))?', re.VERBOSE)
    phonebook_csv = []
    # Добаляем название столбцов
    phonebook_csv.append(contacts_list_csv[0])
    for idx in range(1, len(contacts_list_csv)):
        # Форматируем ФИО
        result = " ".join(contacts_list_csv[idx][:3]).split()
        # Добавляем пустые строки, если не хватает чего-то из ФИО
        while len(result) < 3:
          result.append('')
        # Форматируем номер телефона
        match = phone_pattern.search(" ".join(contacts_list_csv[idx]))
        if match:
            area_code = match.group(1)
            first_part = match.group(2)
            second_part = match.group(3)
            third_part = match.group(4)
            extension = match.group(5)
            formatted_number = f"+7({area_code}){first_part}-{second_part}-{third_part}"
            # Если есть доб., то он добавляется
            if extension:
                formatted_number += f" доб.{extension}"
            # Добавляем информацию о организации, позиции, отформатированный номер, а также почту
            result.extend([contacts_list_csv[idx][3], contacts_list_csv[idx][4], formatted_number, contacts_list_csv[idx][-1]])
        else:
           result.extend([contacts_list_csv[idx][3], contacts_list_csv[idx][4], '', contacts_list_csv[idx][-1]])
        phonebook_csv.append(result)

    return phonebook_csv