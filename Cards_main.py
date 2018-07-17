import Cards_tools

'''
    名片管理系统入口
'''
while True:
    # 显示菜单
    Cards_tools.show_menu()
    action_str = input("请选择希望执行的操作：")
    # 判断接受到的参数
    if action_str in ('0', '1', '2', '3'):

        print('你选择的操作是【%s】' % action_str)
        print("----------------------------------------------------")

        if action_str == '0':
            print('\n欢迎再次使用【名片管理系统】')
            break
        # 新增名片
        elif action_str == '1':
            Cards_tools.new_card()
        # 显示全部2
        elif action_str == '2':
            Cards_tools.show_all()
        # 查询名片
        elif action_str == '3':
            search_dict = Cards_tools.search_card()
            Cards_tools.deal_card(search_dict)
    else:
        print('您输入的数字无效,请重新输入 ！')
