import os

import yaml


def analyze_data(file_name, key):
    """
    根据文件解析数据
    :param file_name: 数据文件名
    :param key: 数据的key
    :return:
    """

    with open(r".%sdata%s%s.yaml" % (os.sep, os.sep, file_name), "r",encoding="utf-8") as f:
        data_list = list()
        data_list.extend(yaml.load(f)[key].values())
        return data_list
