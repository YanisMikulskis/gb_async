import csv
import datetime


def example_1():
    def tables():
        data = [
                [['hostname1', 'vendor1', 'model1', 'location1'],
                 ['kp1', 'Cisco1', '2960', "Moscow str1"]],

                [['hostname2', 'vendor2', 'model2', 'location2'],
                 ['kp2', 'Cisco2', '2960', "Moscow str2"]],

                [['hostname3', 'vendor3', 'model3', 'location3'],
                 ['kp3', 'Cisco3', '2960', "Moscow str3"]
                 ]]

        files_csv = ['info_txt1.txt','info_csv2.csv', 'info_csv3.csv']

        print(list(zip(files_csv, data)))
        for file in list(zip(files_csv, data)):

            with open(file[0], 'w') as new_f:
                file_writer = csv.writer(new_f)
                for row in file[1]:
                    file_writer.writerow(row)

    import re
    def get_data():
        paths = ['lesson_2_files/info_1.txt',
                 'lesson_2_files/info_2.txt',
                 'lesson_2_files/info_3.txt']
        os_prod_list = []
        os_name_list = []
        os_code_list = []
        os_type_list = []
        main_data = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']

        def search_patterns(pattern, text):
            return re.search(rf'{pattern}:\s*(.+)', text).group(1)

        for file in paths:
            with open(file, 'r') as f:
                text = f.read()
                os_prod_list.append(search_patterns('Изготовитель системы', text))
                os_name_list.append(search_patterns('Название ОС', text))
                os_code_list.append(search_patterns('Код продукта', text))
                os_type_list.append(search_patterns('Тип системы', text))
        data = [main_data]
        for i in zip(os_prod_list, os_name_list, os_code_list, os_type_list):
            data.append(list(i))
        return data





    def write_to_csv():
        data = get_data()
        info_csv = 'lesson_2_files/info_csv.csv'
        with open(info_csv, 'w') as f:
            file_writer = csv.writer(f)
            for row in data:
                file_writer.writerow(row)
    write_to_csv()

def example_2():
    import json
    from datetime import date
    def write_order_to_json(item, quantity, price, buyer, date):
        dict_to_json = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
        }
        json_file = 'lesson_2_files/orders.json'
        with open(json_file, 'w') as f:
            json.dump(dict_to_json, f,
                      default=lambda obj: obj.isoformat() if isinstance(obj, datetime.date) else obj,
                      indent=4)
    write_order_to_json('iPhone', 10, '1000$', 'John', date.today())
# example_2()
def example_3():
    dict_to_yaml = {
        1: [1,2,3,4],
        2: 101,
        3: {
            'a': '1€',
            'b': '2€',
            'c': '3€'
        }
    }
    import yaml
    yaml_file = 'lesson_2_files/file.yaml'
    with open(yaml_file, 'w') as f:
        yaml.dump(dict_to_yaml, f, default_flow_style = False, allow_unicode = True)


    with open(yaml_file, 'r') as f:
        print(f.read())
example_3()
