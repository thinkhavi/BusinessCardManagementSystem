import time

cards_list = []

"""
    新建菜单
"""


def show_menu():
    print('**************************************************\n'
          '欢迎使用【名片管理系统】V1.0\n\n'
          '1. 新建名片\n'
          '2. 显示全部\n'
          '3. 查询名片\n\n'
          '0. 退出系统\n'
          '**************************************************')


"""
    新建名片
 """


def new_card():
    name = input('请输入姓名：')
    phone = input('请输入电话：')
    qq = input('请输入QQ：')
    email = input('请输入邮箱：')
    cards_dict = {'name': name, 'phone': phone, 'qq': qq, 'email': email}
    cards_dict.values()
    cards_list.append(cards_dict)
    print('              添加成功！！！')
    time.sleep(2)


"""
    显示全部名片
    :return: 
"""


def show_all():
    if len(cards_list) == 0:
        print('暂时没有名片，请添加名片！')
        time.sleep(2)
        return

    print("----------------------全部名片----------------------")
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")

    print("\n----------------------------------------------------")
    for cards in cards_list:
        for val in cards.values():
            print(val, end="\t\t")
        print()
    meau_data = input('0.返回上一级菜单：')
    print("----------------------------------------------------")
    return


"""
 搜索名片
 :return: 查询到的list中dist数据
 """


def search_card():
    print('功能：搜索名片')
    name = input('请输入要搜索的姓名：')
    for cards in cards_list:
        if name == cards['name']:
            print("姓名", "      电话", "      QQ", "           邮箱")
            print(name + '      ', cards['phone'] + '      ', cards['qq'] + '    ', cards['email'])
            print("----------------------------------------------------")
            return cards
    else:
        print('没有查询到' + name)


"""
     删除/修改/返回函数
    :param find_dict: 查询到的list中dist数据
"""


def deal_card(find_dict):
    while True:
        meau_data = input('请输入对名片的操作  1.修改  2.删除  0.返回上一级菜单：')
        if meau_data in ('1', '2', '0'):
            # 删除
            if meau_data == '2':
                cards_list.remove(find_dict)
                print('     删除成功！')
                time.sleep(2)
                break
            # 修改
            elif meau_data == '1':
                name = input("请输入姓名[回车不修改]：")
                phone = input("请输入电话[回车不修改]：")
                qq = input("请输入QQ[回车不修改]：")
                email = input("请输入邮件[回车不修改]：")
                # 将接受到的数据进行处理
                find_dict["name"] = find_dict['name'] if name == '' else name
                find_dict["phone"] = find_dict['phone'] if phone == '' else phone
                find_dict["qq"] = find_dict['qq'] if qq == '' else qq
                find_dict["email"] = find_dict['email'] if email == '' else email

                print('      修改成功！')
                time.sleep(2)
                break
        else:
            print('您输入的数字无效,请重新输入 ！')
