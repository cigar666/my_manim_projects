一些视频对应代码的索引
================================
# 前言
我在b站发了不少视频，不少感兴趣的朋友希望获得相关的代码以供学习或参考。在多数情况，我在对应视频的视频简介或视频结尾中已经附上了对应的代码链接。
但为了更方便大家找到相关代码的位置，我在此按视频更新的时间顺序做一个各视频对源代码的整理和说明。
需要说明的是，由于版本问题及早期代码中有不少不好的实现方式和不推荐的写法，去年的一些老版本写的代码暂时未上传(或许有部分我会修改后上传)。<br  
[__cigar666的b站主页__](https://space.bilibili.com/66806831 '求关注求三连ღ( ´･ᴗ･` )')

## 关于代码使用的相关声明
 1. 代码主要用作大家交流学习使用，欢迎大家进行修改和补充<br
 2. 允许使用部分相关代码进行视频创作，但如果使用代码较多请注明下出处<br
 3. 禁止直接将该项目中的代码做简单无脑修改甚至不修改而做成视频<br
 4. 禁止未经允许将本项目的代码用作其他商业行为<br

# manim视频对应代码传送门
这部分对应标题即为视频链接。每个视频会有简介和对应代码的传送门。<br

## 1.[我的manim小练习](https://www.bilibili.com/video/BV1E4411J7ot/)<br
### 简介与说明：<br
这是一个汇集了平时写的一些不长的稍微有点价值的动画合集，在一年多的时间里陆陆续续更新了十多个，以后应该也会继续更新。  
已上传的代码中Wave of boxes的相关代码中有一个自己写的盒子类（MyBox类及MyBoxes类），可以制作与视频中类似的盒子阵列动画效果；
分形动画对应的代码是利用ifs原理的相关类实现的，能生成不少有意思的分形图案，具体的实现方式详见代码；
刚性小球碰撞相关的代码是自己写的实现平面上的多个小球完全弹性碰撞代码，目前物体一多效率极低，在之后代码有所优化后上传；
### 对应代码：
__P1 pi的艺术__: 未上传<br
__P2 生命游戏-超新星__: 未上传<br
__P3 1=2？__: 未上传<br
__P4-P6 Wave of boxes__: [代码传送门](https://github.com/cigar666/my_manim_projects/blob/master/my_utils/test_3D.py '注：这部分代码和视频中稍有区别')<br
__P7-P8 杨辉三角中的分形__: [代码传送门](https://github.com/cigar666/my_manim_projects/blob/master/my_projects/fractal/Pascal_triangle.py)<br
__P9-P11 分形小动画__: [代码传送门](https://github.com/cigar666/my_manim_projects/blob/master/my_projects/fractal/fractal_tree.py)<br
__P12-P13 利用刚性小球碰撞制作的小动画__: 代码尚未完善，未上传<br

## 2.[自然数立方和公式的几何证明](https://www.bilibili.com/video/BV11t411w7dj/)<br
### 简介与说明：
在这个视频中试了下三维场景动画，利用方块的堆叠阐释立方和公式的证明思路。其中方块相关的一些类和方法是自己新定义的，目前还是有不少瑕疵。<br
### 对应代码：
__3d证明动画对应场景__: [代码传送门](https://github.com/cigar666/my_manim_projects/blob/master/my_projects/ThreeD_projects/Sum_of_cubes.py)
__2d证明动画对应场景__: 未上传<br

## 3.[千粉纪念：用数学的方式比个心](https://www.bilibili.com/video/BV1s4411k7Ep/)
### 简介与说明：
在这个视频中用manim制作了绘制心形图形相关的动画。其中前面的一堆心形曲线是由geogebra绘制的，中间的心形线相关动画是manim制作的，后面的傅立叶绘图时自己当时试着改写的一个比较垃圾的傅里叶绘图方案。<br
### 对应代码：
[代码传送门](https://github.com/cigar666/my_manim_projects/blob/master/old_projects/1000_fans.py)<br

## 4.[用傅立叶级数画炮姐](https://www.bilibili.com/video/BV1VJ411D7b9/)
### 简介与说明：
基于Grant大佬写好的傅立叶绘图的相关类和方法，制作了傅立叶级数绘制炮姐的相关动画。
如果是想用manim制作傅立叶动画的朋友可以参考这部分代码（由于版本问题某些部分可能会有微调，比如import部分的内容）<br
### 对应代码：
[代码传送门](https://github.com/cigar666/my_manim_projects/blob/master/old_projects/misaka_by_fourier.py)

## 5.[简单的几何级数可视化](https://www.bilibili.com/video/BV1eJ411z78q/)<br
### 简介与说明：
介绍了几个（收敛的）几何级数的图形证明过程，有利于更直观地理解相关知识。相关动画实现起来并不难，利用基础的几何类就能基本实现。
### 对应代码：
[代码传送门](https://github.com/cigar666/my_manim_projects/blob/master/my_projects/geometric_series_vis.py)

## 6.[美妙的万花尺与旋轮线（上）](https://www.bilibili.com/video/BV1JJ411v7ms/)
### 简介与说明：
这部分视频主要展示了不同参数下万花尺对应生成的旋轮线情况，具体的原理分析在下集视频（实际上想讲的也还没讲完，但由于一些原因暂时先讲这么多）。<br
在写这部分代码时自己写了一个齿轮类（渐开线齿轮），用来模拟万花尺的运行情况（实际上的万花尺可能并不是渐开线齿轮，但意思到了就行），也可以在其他场合下使用；
这部分代码中也有一些updater的相关用法，用来实现万花尺一边运转一边画图，类似的方法也可以用来实现其他动画；
### 对应代码：
__齿轮及万花尺相关代码__: [代码传送门](https://github.com/cigar666/my_manim_projects/blob/master/my_projects/spirograph/Gears.py)<br
__内旋轮线相关代码__: [代码传送门](https://github.com/cigar666/my_manim_projects/blob/master/my_projects/spirograph/Hypocycloid.py)

## 7.[美妙的万花尺与旋轮线（下）](https://www.bilibili.com/video/BV1w7411q7xH/)
### 简介与说明：
这部分视频接着上部视频，讲了万花尺的运动分析与如何求解得到万花尺对应的内旋轮线方程。<br
利用了不少上个视频的代码，比如齿轮类（Gear_outline）、万花尺类（Spirograph）等，实际上这些类还有优化改进空间（但后面太懒就没动了）；  
这部分写了一些关于复数和旋转的相关代码，其实顺着写下去也能写出一个傅立叶绘图的实现代码，但是Grant已经做了，所以...
### 对应代码：
[代码传送门](https://github.com/cigar666/my_manim_projects/blob/master/my_projects/spirograph/Spirograph_explain.py)

## 8.[复数、旋转与三角函数](https://www.bilibili.com/video/BV157411p7iS/)
### 简介与说明：
一个小视频，讲了随时间t变化的复数e^iwt旋转的相关动画。主要试了下在三维场景中的曲线曲面画法及其他操作。
### 对应代码：
[代码传送门](https://github.com/cigar666/my_manim_projects/blob/master/my_projects/ThreeD_projects/Rotate_by_complex.py)

## 9.[均值不等式链的几何证明](https://www.bilibili.com/video/av87824738/)
### 简介与说明：
介绍了均值不等式链的几何证明。<br
代码中大量使用了updater，但实现得过于粗暴（无脑地复制粘贴修改之后就写好了），更靠谱的做法是利用ValueTracker来更新包含整个图形的VGroup（为了更清晰点可以直接写成一个类，单步的更新可以直接写成类方法来根据一个入口参数生成整个图形）。
此外，里面的虚线圆之类的直接使用DashedMobject就好了。
### 对应代码
[代码传送门](https://github.com/cigar666/my_manim_projects/blob/master/my_projects/Inequality_proved_by_geo.py)

## 10.[心形麦比乌斯带](https://www.bilibili.com/video/BV167411g73H/)
### 简介与说明：
 在三维场景中使用ParametricSurface等绘制了一下麦比乌斯带及心形的麦比乌斯带。
### 对应代码
[代码传送门](https://github.com/cigar666/my_manim_projects/blob/master/my_projects/ThreeD_projects/Mobius.py)

## 11.[摆线拱面积计算](https://www.bilibili.com/video/BV1VE411n7KC/)
### 简介与说明：
介绍了三种方法来计算摆线拱的面积，重点介绍的是前两种几何方法。<br
对应的代码并不算特别复杂，其中：利用updater制作了圆在滚动时其余部分的变化更新的动画；利用边数足够多的的Polygon来近似表示了图中带曲边的不规则图形的面积。
### 对应代码
[代码传送门](https://github.com/cigar666/my_manim_projects/blob/master/my_projects/Cycloid_Area.py)

## 12.[三体运动模拟](https://www.bilibili.com/video/BV1mE411u7Mf/)
### 简介与说明：
利用updater制作的三体系统（可以添加行星）的数值模拟（但过于粗糙，基本上除了看个效果之外没啥实际价值）<br
在代码中使用VGroup为基类自己写了一些有用的类，比如具有光晕效果的恒星（Sun类）及利用能显示目标物体的逐渐变淡的运动轨迹的Trail类；
三体系统（Three_Body类）由updater进行计算（根据对应时间步的力学和运动学结果来计算下一步的状态）并更新，并且会同时更新对应的运动尾迹（由Trail类实现）；
其中文件中仅有部分测试参数能用，原因在于之后又调整了引力常数（这块儿并没有按实际的给）等物理量，导致前面的一些数据参数失效
### 对应代码
__封装好的相关类和方法__: [代码传送门](https://github.com/cigar666/my_manim_projects/blob/master/my_utils/my_geometry.py)<br
__视频中的三体运动相关项目__: [代码传送门](https://github.com/cigar666/my_manim_projects/blob/master/my_projects/ThreeBody.py)<br

## 13.[自然数立方和公式的七种妙证](https://www.bilibili.com/video/BV1P741117QQ/)
### 简介与说明：
这是[manim-kindergarten](https://github.com/manim-kindergarten)的成员合作视频，介绍了其中自然数立方和公式的证明（其中第三个证明和之前的视频中的[自然数立方和3d证明](https://github.com/cigar666/my_manim_projects/blob/master/my_projects/ThreeD_projects/Sum_of_cubes.py)
相同）
### 对应代码
[代码传送门](https://github.com/manim-kindergarten/manim_sandbox/tree/master/videos/HomeworkVol01)

## 14.[一个和反演变换相关的画圈圈动画](https://www.bilibili.com/video/BV1PV411o7Y9/)
### 简介与说明：
参考了@Matt Henderson的推特制作的一个小动画，和反演变换有这相似之处。<br
主要利用了updater和TracedPath(可以绘制简单的动点的轨迹，和之前的Trail类类似，虽没有轨迹的渐变效果但计算量更小)来绘制动点轨迹；关于反演部分的代码写得十分简陋，更为完善的反演变换相关的代码可参考[@Solara570](https://github.com/Solara570)的[相关代码](https://github.com/Solara570/demo-solara/blob/master/articles/inversion.py)<br
### 对应代码
[代码传送门](https://github.com/cigar666/my_manim_projects/blob/master/my_projects/Touching_circles.py)

## 15.[矛盾空间三角形小动画](https://www.bilibili.com/video/BV14V411r7S2/)
### 简介与说明：
很短的类似埃舍尔风格的动画，看起来像矛盾的三维空间其实是由二维三角形网格实现的。
### 对应代码
[代码传送门](https://github.com/cigar666/my_manim_projects/blob/master/my_projects/Triangle_plotter.py)

## 16.[如何让凸四边形切两刀后重新拼成平行四边形](https://www.bilibili.com/video/BV1aT4y1E7Ex/)
### 简介与说明：
介绍了如何让任意凸四边形切两刀后重新拼成平行四边形的方法，后面又加了些和四边形密铺相关的小动画。<br
代码并不难，用了基本的几何类以及自己写的一些几何类（比如角类Angle）；文字动画用了一些自己写的效果，在[my_text.py](https://github.com/cigar666/my_manim_projects/blob/master/my_utils/my_text.py)里面都有
### 对应代码
[代码传送门](https://github.com/cigar666/my_manim_projects/blob/master/my_projects/Jigsaw.py)


# 暂时未上传代码的相关manim视频

1.[自然数立方和公式的证明](https://www.bilibili.com/video/BV18b411G78M/)<br
2.[堆盒子与调和级数](https://www.bilibili.com/video/BV1T4411n7an/)<br
3.[手算开平方的方法与原理](https://www.bilibili.com/video/BV1vt411g7oL/)<br
4.[10个优雅的勾股定理妙证（上）](https://www.bilibili.com/video/BV18E411R7Zg/)<br
5.[10个优雅的勾股定理妙证（下）](https://www.bilibili.com/video/BV1sE411b7ZD/)<br
6.[浅谈自然数平方根的连分数表示](https://www.bilibili.com/video/BV1uE411d7Sv/)<br
7.[基于python的曼德勃罗集的简单可视化](https://www.bilibili.com/video/BV1jJ411s7q5/)<br

