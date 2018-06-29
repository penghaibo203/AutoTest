"""
有用的通用功能代码
"""

def get_testdata(file_path):
    data4ddt = []
    with open(file_path, encoding='utf-8') as f:
        dataset = f.readlines()
        for data in dataset:
            data4ddt.append(data.strip().split("|"))

    return data4ddt

