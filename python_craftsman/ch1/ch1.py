from typing import List


def remove_invalid(items: List[int]):
    """剔除 items 中的无效值"""
    return [item for item in items if item > 0]


# 用户输入可能会有空格，使用strip()函数去除空格
def extract_username(s):
    print(s)
    if len(s) == 0:
        return True
    else:
        return False


# input_string = input("Enter a string: ")
# value = extract_username(input_string.strip())
# print(value)

author = "piglei"
print("hello, {}".format(author))

author, reader = "piglei", "raymond"
print("change before -> author: {}, reader: {}".format(author, reader))
author, reader = reader, author
print("change after -> author: {}, reader: {}".format(author, reader))

usernames = ["piglei", "raymond"]
author, reader = usernames
print("author: {}, reader: {}".format(author, reader))

attrs = [1, ["piglei", 100]]
user_id, (username, score) = attrs
print("user_id: {}, username: {}, score: {}".format(user_id, username, score))

data = ["piglei", "apple", "orange", "balnana", 100]
# *fruits表示剩下的元素都是fruits, 动态unpacking
username, *fruits, score = data
print("username: {}, fruits: {}, score: {}".format(username, fruits, score))

for username, score in [("piglei", 100), ("raymond", 60)]:
    print("username: {}, score: {}".format(username, score))

author, _ = usernames
print("author: {}".format(author))
username, *_, score = data
print("username: {}, score: {}".format(username, score))

items = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
print(remove_invalid(items))
