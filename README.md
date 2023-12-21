<h1>bilibili_qrcode_login</h1>
基于python的bilibili网页登录二维码输出到控制台的小工具

----------

<h2>简介</h2>

本项目基于python，主要使用qrcode库生成二维码、使用PIL库识别二维码，根据像素值转换为▀▄ █等方块输出到控制台；扫码成功登录后获取到cookie值。

<b>本项目仅用于学习和测试！利用本项目提供的接口、文档等造成不良影响及后果与本人无关！</b>

----------

<h2>参考接口</h2>
<a href="https://github.com/SocialSisterYi/bilibili-API-collect">bilibili-API-collect</a> 哔哩哔哩-API收集整理

----------

<h2>使用方法</h2>
1、把项目 git clone 到本地，安装好相关依赖(requirements.txt里的库)

2、运行main.py(使用cmd执行输出的二维码有问题，请使用其它终端测试)

3、二维码输出到控制台后，使用B站app扫码登录(如果使用手机远程登录服务器执行，可以在手机截图二维码后再使用app读取相册扫码)

4、成功登录后，即可获取到cookie，再按需使用

----------