from typing import LiteralString

def get_formatted_name(first_name: LiteralString, last_name: LiteralString, middle_name: LiteralString = ''):
    """返回整洁的姓名"""
    # if middle_name is not None, it will be True
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    # MUST have return statement if not have return key word, it will return None
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
