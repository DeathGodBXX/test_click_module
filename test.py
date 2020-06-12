"""
    json.dumps()将python数据转换成json数据
    json.loads()将json数据转换成python数据
    json.dump(data,f)将python数据写入到json格式下的文件f中
    data=json.load(f)将json格式下的数据传到python数据data中

"""


# import json
#
# # Python 字典类型转换为 JSON 对象
# data = {
#     'no': 1,
#     'name': 'Runoob',
#     'url': 'http://www.runoob.com'
# }
#
# json_str = json.dumps(data)
# print(data)
# print("Python 原始数据：", repr(data))  # repr将data转换成字符串形式，打印的时候自动去掉“ ”
# print("JSON 对象：", json_str)

import json

# Python 字典类型转换为 JSON 对象
data1 = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data1)
print("Python 原始数据：", repr(data1))
print("JSON 对象：", json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print("data2['name']: ", data2['name'])
print("data2['url']: ", data2['url'])

with open('data.json','w') as f:
    json.dump(data1,f)

with open('data.json','r') as f:
    data3 = json.load(f)
print(data3)

