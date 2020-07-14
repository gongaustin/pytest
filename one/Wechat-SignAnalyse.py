import itchat
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image

# 设置登录方法
itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)

# 获取好友签名信息并储存在 siglist 中
siglist = []
for indedx,friend in enumerate(friends):
    sigture = friend['Signature']
    # 如果存在签名的话
    if len(friend['Signature']) > 0:
        # 将个性签名中的表情符号去掉（这里没有去除干净，利用正则表达式）
        sigture = sigture.replace('span','').replace('class','').replace('emoji','').replace('< =','').replace('"','').replace('</>','').replace('>','')
        siglist.append(sigture)

# 将siglist中的元素拼接为一个字符串
text = ''.join(siglist)

# jieba(结巴分词：有全模式、精确模式、默认模式、新词识别、搜索引擎模式）
# jieba.cut()所接收的两个参数，第一个参数为需要分词的字符串，第二个为是否采用全模式
word_list = jieba.cut(text, cut_all=True)
# 空格拼接
word_space_split = ' '.join(word_list)
# 字体的颜色为对应路径的背景图片的颜色
coloring = np.array(Image.open("D:/PythonWorkplace/WeChat/image.png"))
# font_path: 字体路径；  random_state: 为每个字体返回一个PIL颜色；  scale：按照比例放大画布；max_font_size:显示的最大字体的大小
# 如果参数 mask 为空，则使用二维遮罩绘制词云。如果 mask 非空，设置的宽高值将被忽略，遮罩形状被 mask 取代
my_wordcloud = WordCloud(background_color="white", max_words=2000,
                         mask=coloring, max_font_size=150, random_state=42, scale=3,
                         font_path="C:/Windows/Fonts/simkai.ttf").generate(word_space_split)
# 画布的颜色
image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()                                                                                                                                                                                      