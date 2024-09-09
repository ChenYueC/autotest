import yaml
import json


class Yaml_Method:
    @classmethod
    def yaml_read(cls, path, key):  # 读取yaml文件
        with open(path, 'r', encoding='utf-8') as data:
            value = yaml.load(stream=data, Loader=yaml.FullLoader)
            return value.get(key)

    @classmethod
    def yaml_write(cls, path, data_w):  # 写入yaml文件
        with open(path, 'a', encoding='utf-8') as data:
            yaml.dump(data_w, stream=data, allow_unicode=True)

    @classmethod
    def yaml_clear_all(cls, path):  # 清理yaml文件
        with open(path, 'w', encoding='utf-8') as data:
            data.truncate()

    @classmethod
    def yaml_del_key_value(cls, path, re_data):  # 清理yaml文件
        with open(path, 'r', encoding='utf-8') as data:
            value = yaml.load(stream=data, Loader=yaml.FullLoader)
            new_value = value.pop(re_data)
        with open(path, 'w', encoding='utf-8') as data:
            yaml.dump(value, stream=data, allow_unicode=True)


class Json_Method:
    @classmethod
    def json_read(cls, json_path):
        with open(json_path, mode='r', encoding='utf-8') as file:
            login_read_data = json.load(file)
            login_list_data = []
            for i in login_read_data:
                login_data = tuple(i.values())
                login_list_data.append(login_data)
        return login_list_data
