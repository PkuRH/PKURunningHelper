# PKURunningHelper

请自行承担使用不当造成的一切后果🧐

该项目改写自学长的项目 [PKURunningHelper](https://github.com/zhongxinghong/PKURunningHelper)

## 依赖环境

该项目目前仅支持 `Python 3`

安装依赖包 `requests`, `requests_toolbelt`
```
$ pip3 install requests requests_toolbelt
```

可选择安装 `simplejson`
```
$ pip3 install simplejson
```


## 下载

下载这个分支到本地
```
$ git clone https://github.com/PkuRH/PKURunningHelper
```


## 用法

进入项目根目录
```console
$ cd PKURunningHelper/
```

首先根据提示，修改配置文件 `config.ini`
```console
$ vim config.ini
```

确保配置文件书写，即可完成一次上传。默认为 `debug` 模式，因此还会输出每次请求返回的 json 数据包
```console
$ python3 runner.py

[INFO] runner, 2018-09-28 18:08:55, upload record success !
```


## 文件夹结构

```
PKURunningHelper/
├── LICENSE
├── PKURunner                 // PKURunner 客户端程序包
│   ├── __init__.py
│   ├── client.py                 // PKURunner 客户端类
│   ├── data                  // 跑步记录数据
│   │   └── 400m.250p.54.pkurunner.json    // 五四跑廊走一圈的高德 GPS 数据，共 250 点，坐标手动校正过
│   ├── error.py                  // 错误类定义
│   ├── iaaa.py                   // 北大 iAAA 统一认证客户端类
│   └── record.py                 // 跑步记录类
├── README.md
├── cache                     // 缓存文件夹
│   └── PKURunner_AccessToken.json    // PKURunner 的 iAAA 认证所得 token 缓存
├── config.ini                    // 项目配置文件
├── requirements.txt
├── runner.py                     // 项目主程序
└── util                      // 通用程序包
    ├── __init__.py
    ├── class_.py                 // 通用类
    ├── func.py                   // 通用函数库
    └── module.py                 // 通用模板类，统一 import 导入结果
```

## 声明

本项目仅供参考学习，你可以修改和使用这个项目，但请自行承担使用不当造成的一切后果。

## 证书

[MIT LICENSE](https://github.com/PkuRH/PKURunningHelper/blob/master/LICENSE)
