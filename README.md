<div align="center">
<h1 align="center">
Auto-ShiXiBeiAn
</h1>
<p align="center">
🥰实习备案自动打卡解决方案🥰
</p>
<p align="center">
支持多用户、自定义位置与时间、微信消息推送
</br>
</p>
</br>
<a target="_blank" href="https://b23.tv/hsaDxKf">视频教程</a>
</div>
</br>



## 前言

**1、请务必认真阅读此文档后继续！**

**2、在开始之前请帮我点一下右上角的star。**

**3、此项目仅限学习交流，禁止用于任何商业或违法用途！**

**4、此项目仅限学习交流，禁止用于任何商业或违法用途！**

**5、此项目仅限学习交流，禁止用于任何商业或违法用途！**

**6、此项目仅限学习交流，您必须在Fork或下载此仓库源码后的24小时内删除所有内容。**

**7、此项目仅限学习交流，学习或使用此项目造成任何损失均由个人承担。**


</br>

## 目录

- [前言](#前言)
- [使用门槛](#使用门槛)
- [使用方法](#使用方法)
  - [Github Actions](#github-actions)
  - [使用自己的服务器部署](#使用自己的服务器部署)
- [修改自动打卡时间🎯](#修改自动打卡时间)
- [赞助支持](#赞助支持)

</br>
</br>

## 使用门槛

1、帮我点一下右上角的star（星星）

2、仅限个人学习交流使用，禁止任何平台或个人将此项目用于盈利或违法！



</br></br>

## 使用方法

### Github Actions

推荐指数：⭐⭐⭐⭐⭐


优点：适合没有自己服务器的人使用。


缺点： 每日打卡时间无法保证十分准时，拥有10-30分钟的误差。

</br>

1.点击Star后Fork本仓库🤪
![1.png](https://tc.xuanran.cc/2022/12/01/9b1d336235e28.png)
![2.png](https://tc.xuanran.cc/2022/12/01/2c1c3b427a14a.png)
</br>
2.准备配置文件🤔

如果想同时打卡多个用户,请再添加一个数据体就好了(如果还不理解加我微信（XuanRan_Dev）（记得备注来意）我教你)

**注意：配置文件模板下方有配置含义，请务必参照配置含义填写**
```json
[
  {
    "enable": true,
    "alias": "张三",
    "phone": "18888888888",
    "password": "123456...",
    "deviceType": "Xiaomi|Mi 13|13",
    "deviceId": "设备ID",
    "address": "打卡地址",
    "longitude": "位置经度",
    "latitude": "位置纬度",
    "pushKey": "推送Key"
  }
]
```

其配置含义如下：

| 参数名称   | 含义                                                         |
| ---------- | ------------------------------------------------------------ |
| enable     | 是否启用该用户的打卡（true或false)                           |
| alias      | 别名，用于在打卡日志中标识不同用户，可空。                   |
| phone      | 手机号                                                       |
| password   | 密码                                                         |
| deviceType | 设备类型,格式:手机品牌英文名称\|手机代号\|安卓系统版本,例如:Xiaomi\|Mi 13\|13 |
| deviceId   | 设备ID,36位字母+数字组合,[点我获取随机ID](http://did.sxba.xuanran.cc)          |
| address    | 打卡地址,例如中国河南省洛阳市xxxxx                           |
| longitude  | 打卡位置经度,通过坐标拾取来完成，[传送门](https://jingweidu.bmcx.com/) |
| latitude   | 打卡位置纬度,通过坐标拾取来完成，[传送门](https://jingweidu.bmcx.com/) |
| pushKey    | 打卡结果微信推送，微信推送使用的是pushPlus，请到官网绑定微信([传送门](https://www.pushplus.plus/))，然后在发送消息里面把你的token复制出来粘贴到pushKey这项 |





</br>

3.配置Secret

填写完成后请复制如上配置文件，然后打开仓库的Settings->Secrets->Actions->New repository secret

Name填USERS

Secret填改好的配置文件

![3.png](https://tc.xuanran.cc/2022/11/13/2143b390f8199.png)
![5.png](https://tc.xuanran.cc/2022/12/01/36cadab52b21b.png)

4.运行测试

**以下部分图片复用了工学云自动打卡，除左上角forked from xxxx外与视频教程无其他区别**
![5.png](https://tc.xuanran.cc/2022/11/13/500e789b3dfec.png)
![6.png](https://tc.xuanran.cc/2022/11/13/1366e5e0ced97.png)
![7.png](https://tc.xuanran.cc/2022/11/13/2a2b4b7e01884.png)
![8.png](https://tc.xuanran.cc/2022/11/13/bd1cd3218f77a.png)
![9.png](https://tc.xuanran.cc/2022/11/13/33c6cec2e37ec.png)
![4.png](https://tc.xuanran.cc/2022/12/01/735c10732d2e0.png)
</br></br></br></br>

至此，自动打卡将会在每天8点左右自动运行打卡。😉


</br></br></br>

### 使用自己的服务器部署

推荐指数：⭐⭐⭐⭐⭐

优点：运行稳定、准时。

缺点：有一定的上手成本。

具体教程：

1、下载本仓库源码到你服务器。

2、在服务器中安装好Python环境。

3、运行命令来下载依赖。

```python
pip install requests
pip install pytz
pip install pycryptodome
```

4、在百度搜索：你的操作系统+ 定时任务，查看如何创建定时任务。

5、创建一个user.json配置文件在项目目录，并将配置文件放入其中

6、运行python Main.py测试

</br></br></br>


## 修改自动打卡时间🎯	

修改自动打卡时间需要了解Cron表达式的使用，且需注意不要将打卡时间设置为11点以及23点，此时间段中会运行每日打卡检查，自动打卡在此时间段内不生效。😴


</br>
1.编辑sign.yml文件，找到图中我圈出的部分

![image-20221021093411661](https://tc.xuanran.cc/2022/11/10/5d81dcc0bff46.png)

</br>

2.编辑表达式

GitHub的cron表达式不支持精准到秒，所以从最左边开始，分别为：

分钟 小时 日 月份 星期

而且Github的服务器时间会比我们晚八个小时，所以在你需要打卡的时间-8配置到里面就行了

</br>

例如说在上午十点打卡就是:

```yml
- cron: "00 02 * * *"
```

</br>
</br>





## 赞助支持

如果此仓库帮助了你学到了新知识，你可以帮我买杯可乐，但如果你使用此项目产生任何盈利，请不要支持。

![赞助支持](https://tc.xuanran.cc/2022/11/20/b8f5ddc944634.png)



</br></br>
最后，帮我点下仓库的小星星，Thanks.

😀😀😀😀😀
