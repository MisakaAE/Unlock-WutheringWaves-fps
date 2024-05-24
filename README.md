# 这是一个修改鸣潮帧数上限的脚本
## 原理
修改用户设置文件 `Wuthering Waves/Wuthering Waves Game/Client/Saved/LocalStorage/LocalStorage.db`中`GameQualitySetting`对应的`KeyCustomFrameRate`的值，默认是`60`

## 使用的库
```text
pywin32==306
```

## 使用
### 方法一
下载release运行，启动后选择鸣潮的根目录，按照程序提示输入指定内容
最后程序在桌面生成一个快捷方式，启动新的快捷方式启动游戏。
**不要用启动器启动游戏！配置会失效**

### 方法二
```bash
git clone https://github.com/MisakaAE/Unlock-WutheringWaves-fps
cd Unlock-WutheringWaves-Fps
pip install -r requirements.txt
python.exe app.py
```
启动后同方法一

测试环境为3.11.x，Windows11


## 编译
```bash
pyinstaller.exe -F ./app.py -n "Wuthering Waves Unlock fps"
```

## 声明
代码瞎几把写的，大佬们家人们看个乐呵就行了
