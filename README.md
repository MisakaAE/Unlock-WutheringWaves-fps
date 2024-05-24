# 这是一个修改鸣潮帧数上限的脚本
## 原理
修改用户设置文件 `Wuthering Waves/Wuthering Waves Game/Client/Saved/LocalStorage/LocalStorage.db`中`GameQualitySetting`对应的`KeyCustomFrameRate`的值，默认是`60`

## 使用的库
都是 python3 自带的
```text
sqlite3
msvcrt
tkinter
os
```

## 使用
```bash
git clone https://github.com/MisakaAE/Unlock-WutheringWaves-fps
cd Unlock-WutheringWaves-fps
python.exe app.py
```
> 不需要选择到具体的`LocalStorage.db`
  只需要选择启动器所在的目录，也就是鸣潮的根目录

+ 启动脚本
  tkinter的窗口选择`鸣潮启动器`的文件夹，如`C:/Wuthering Waves`，随后按照脚本提示输入指定的项


## 编译
```bash
pyinstaller.exe -F ./app.py -n "Wuthering Waves Unlock fps"
```

## 声明
代码瞎几把写的，大佬们看个乐呵就行了
