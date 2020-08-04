from manimlib.imports import *
import matplotlib.pyplot as plt
import csv
import codecs
# import pandas as pd

# import ctypes
# # from https://www.cnpython.com/qa/81434
# def GetTextLength(text, points=10, font='思源黑体 Bold'):
#     class SIZE(ctypes.Structure):
#         _fields_ = [("cx", ctypes.c_long), ("cy", ctypes.c_long)]
#
#     hdc = ctypes.windll.user32.GetDC(0)
#     hfont = ctypes.windll.gdi32.CreateFontA(points, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, font)
#     hfont_old = ctypes.windll.gdi32.SelectObject(hdc, hfont)
#
#     size = SIZE(0, 0)
#     ctypes.windll.gdi32.GetTextExtentPoint32A(hdc, text, len(text), ctypes.byref(size))
#
#     ctypes.windll.gdi32.SelectObject(hdc, hfont_old)
#     ctypes.windll.gdi32.DeleteObject(hfont)
#
#     # return (size.cx, size.cy)
#     return size.cx


def get_text_length(text):
    # xia j8 xie de 一个估算大致长度的代码
    l = 0
    for ch in text:
        if ch in 'abcdefghijklmnopqrstuvwxyz1234567890_':
            l += 0.5
        else:
            l += 1
    return l

class Test_max_length_of_Text(Scene):

    def construct(self):

        t = Text('哈' * 1000, font='思源黑体 Bold', color=WHITE, size=0.05).set_width(100).move_to(ORIGIN)
        print(len(t.text))
        print(len(t))
        self.add(t)
        self.wait()

class Test(Scene):

    def construct(self):

        im = plt.imread(r'E:\GitHub\manim\my_manim_projects\my_projects\resource\png_files\m_set_01.bmp')
        Z = im[:, :, 0]
        nx, ny = len(Z[0])-1, len(Z)-1

        def set_color4text(Text):
            for t in Text:
                loc = t.get_center()
                j, i = int((loc[0]/FRAME_WIDTH + 1/2) * nx), int((-loc[1]/FRAME_HEIGHT + 1/2) * ny)
                t.set_color(rgb_to_hex(im[i, j]/255))

        text_str = ''
        num = 0

        text_all = VGroup()

        str_01 = '可爱的cigar666的粉丝'
        for i in range(6000):
            text_str_i = '@' + str_01[0:np.random.randint(2, 14)]
            num += len(text_str_i)
            text_str += text_str_i
            if num > 400:
                t = Text(text_str, font='思源黑体 Bold', size=0.09)
                # set_color4text(t)
                text_all.add(t)
                print(len(t))
                text_str = ''
                num = 0

        text_all.arrange(DOWN, buff=0.005, aligned_edge=LEFT)
        if text_all.get_height()/text_all.get_width() > 8/14:
            text_all.set_height(7.9)
        else:
            text_all.set_width(13.8)

        for text in text_all:
            set_color4text(text)

        self.add(text_all)
        self.wait(1)

# data = []
#
# f = open(r"E:\GitHub\manim\my_manim_projects\my_projects\resource\data\FollowerData.csv", "r", encoding="utf8")
# reader = csv.reader(f)
# print(type(reader))
# for row in reader:
#     data.append(row)
#     print(row)
# fans_name = np.array(data)[:, 1]
# f.close()
# print('##################')
# print(sorted(fans_name, reverse=False, key=lambda name: len(name)))

class Show_followers(Scene):

    """
    建议在渲染时加上
    """

    CONFIG = {
        'image_path': r'E:\GitHub\manim\my_manim_projects\my_projects\resource\png_files\m_set_01.bmp', # 图片路径
        'data_file_path': r"E:\GitHub\manim\my_manim_projects\my_projects\resource\data\FollowerData.csv", # 粉丝数据（csv格式）
        'line_length': 700, # 每行文字的大致长度，具体粉丝数量不同这个会影响文字排出来的长宽比，
                            # 因为粉丝id长短不一所以难以给出具体值，建议先低分辨率试好了再调高分辨率
                            # 也可先缩小数据规模来预估参数

    }

    def construct(self):

        data = []

        f = open(self.data_file_path, "r", encoding="utf8")
        reader = csv.reader(f)
        print(type(reader))
        for row in reader:
            data.append(row)
            # print(row)
        f.close()
        fans_name = np.array(data)[:, 1]
        names = fans_name # 如果注释掉这行用下一行的话排序方式有区别
        # names = sorted(fans_name, reverse=False, key=lambda name: get_text_length(name)) # 注释掉的话就按照长度排序一下， 否则就是按关注时间排序

        im = plt.imread(self.image_path)
        Z = im[:, :, 0]
        nx, ny = len(Z[0])-1, len(Z)-1

        final_str = ''
        def set_color4text(Text):
            for t in Text:
                loc = t.get_center()
                j, i = int((loc[0]/FRAME_WIDTH + 1/2) * nx), int((-loc[1]/FRAME_HEIGHT + 1/2) * ny)
                t.set_color(rgb_to_hex(im[i, j]/255))

        text_str = ''
        l_max = 0
        line_num = 0
        text_all = VGroup()
        for i in range(len(names)):
            text_str_i = '@' + names[i]
            # length_i = GetTextLength(text_str_i)
            length_i = get_text_length(text_str_i)
            l_max += length_i
            text_str += text_str_i
            if l_max > self.line_length - length_i/2:
                line_num += 1
                text_str = str(line_num) + ' ' + text_str
                t = Text(text_str, font='思源黑体 Bold', size=0.08)
                # set_color4text(t)
                text_all.add(t)
                print(l_max)
                final_str += text_str + '\n'
                text_str = ''
                l_max = 0

        f = codecs.open('get_loction_of_fans.txt', 'w', encoding='utf-8')
        print(final_str)
        f.write(final_str)
        f.close()

        text_all.arrange(DOWN, buff=0.005, aligned_edge=LEFT)
        if text_all.get_height()/text_all.get_width() > FRAME_HEIGHT/FRAME_WIDTH:
            text_all.set_height(FRAME_HEIGHT-0.1)
        else:
            text_all.set_width(FRAME_WIDTH-0.1)
        for text in text_all:
            set_color4text(text)

        self.add(text_all)
        self.wait(1)

