import json
import sys

if len(sys.argv) != 4:
    print("Необходимо указать 3 аргумента коммандной строки\nВ качестве аргументов принимаются пути к файлам"
          "\nExample: python task2.py path_to_values_file path_to_tests_file path_to_result_file")
    exit(1)

with open(sys.argv[1], "r") as read_file:
    valueData = json.load(read_file)

with open(sys.argv[2], 'r') as read_file:
    testsData = json.load(read_file)

replacements_dict = {item["id"]: item["value"] for item in valueData['values']}


def set_values(data):
    if isinstance(data, dict):
        if 'id' in data and 'value' in data:
            if data['id'] in replacements_dict:
                data['value'] = replacements_dict[data['id']]
        for k, v in data.items():
            set_values(v)
    elif isinstance(data, list):
        for item in data:
            set_values(item)


set_values(testsData['tests'])
with open(sys.argv[3], 'w') as write_file:
    json.dump(testsData, write_file, indent=4)
