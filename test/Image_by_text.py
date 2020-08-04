from manimlib.imports import *
import matplotlib.pyplot as plt
import csv
# import codecs
# import pandas as pd

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

    def construct(self):

        data = []

        f = open(r"E:\GitHub\manim\my_manim_projects\my_projects\resource\data\FollowerData.csv", "r", encoding="utf8")
        reader = csv.reader(f)
        print(type(reader))
        for row in reader:
            data.append(row)
            print(row)
        f.close()
        fans_name = np.array(data)[:, 1]
        names = sorted(fans_name, reverse=False, key=lambda name: len(name))

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
        for i in range(len(names)):
            text_str_i = '@' + names[i]
            num += len(text_str_i)
            text_str += text_str_i
            if num > 600:
                t = Text(text_str, font='思源黑体 Bold', size=0.09)
                # set_color4text(t)
                text_all.add(t)
                print(len(t))
                text_str = ''
                num = 0

        text_all.arrange(DOWN, buff=0.005, aligned_edge=LEFT)
        if text_all.get_height()/text_all.get_width() > FRAME_HEIGHT/FRAME_WIDTH:
            text_all.set_height(FRAME_HEIGHT-0.1)
        else:
            text_all.set_width(FRAME_WIDTH-0.1)
        for text in text_all:
            set_color4text(text)
        self.add(text_all)
        self.wait(1)

