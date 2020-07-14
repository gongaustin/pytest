import itchat
import matplotlib.pyplot as plt
# 登录方法，会弹出二维码，用微信扫描登录
itchat.auto_login()
friends = itchat.get_friends(update=True)

#统计好友的性别，微信中男性为1，女性为2，未知为0
def sex(friends):
    total_friends = len(friends)
    male =  female = other = 0
    for friend in friends:
        sex = friend['Sex']
        if sex == 1:
            male = male + 1
        elif sex == 2:
            female = female + 1
        else:
            other = other + 1
    sex_list = ["男生","女生","不明性别"]
    sex_number_list = [male,female,other]
    # 此行代码用来设置中文
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title(friends[0]['NickName'] +'微信中的男女比例')
    plt.bar(range(len(sex_list)),sex_number_list,tick_label=sex_list,color="yellow")
    plt.show()
    print("男性好友 ： ", male)
    print("女性好友 ： ", female)
    print("不明性别好友 ： ", other)
    print("好友总数 ; ", total_friends)

# 调用函数sex()
sex(friends)