import sqlite3
from msvcrt import getch
import tkinter as tk
from tkinter import filedialog
from os import path as osPath
import pythoncom
from win32com.client import Dispatch
import json


def create_shortcut(target_path, shortcut_path):
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = target_path
    shortcut.Save()


def get_path(dir_pth):
    root = tk.Tk()
    root.withdraw()
    f_path = filedialog.askdirectory(title="选择鸣潮主文件夹，比如 C:\\Wuthering Waves",
                                    initialdir=dir_pth)
    return f_path

    
def mainMenu(readOnly=None):
    setFrameRateChoose = input("选择修改Fps: [1] 60fps [2] 120fps [3] 自己输入 \n输入选项数字\n> ")
    if setFrameRateChoose == "1":
        setFrameRate = 60
    elif setFrameRateChoose == "2":
        setFrameRate = 120
    elif setFrameRateChoose == "3": 
        setFrameRate = input("请输入数字:")
        try:
            int(setFrameRate)
        except ValueError:
            print("非法输入,请重新输入！")
            pressAnyKeyToContinue(0)
            mainMenu()
        else: 
            pass
        
    else:
        print("非法输入，返回默认值 60")
        setFrameRate = 60
    
    return setFrameRate


def pressAnyKeyToContinue(val=0):
    if val == 0:
        print("\n按任意键继续...")
        pass
    
    elif val == 1:
        print("\n按任意键退出...")
        pass
    
    getch()

 

def main(path,setFrameRate=60):
    # 连接到数据库
    conn = sqlite3.connect(path)

    # 获取游标
    cursor = conn.cursor()

    # 查询 key 值为 "GameQualitySetting" 的项
    query_key = "GameQualitySetting"
    cursor.execute(f"SELECT value FROM {table_name} WHERE key = ?", (query_key,))
    result = cursor.fetchone()
    
    if result:
        
        # 解析 JSON 数据
        data = json.loads(result[0])
        
        # 修改 KeyCustomFrameRate 的值
        data['KeyCustomFrameRate'] = setFrameRate
        
        # 将修改后的 JSON 数据转换回字符串
        updated_json = json.dumps(data)
        
        # 更新Value
        cursor.execute(f"UPDATE {table_name} SET value = ? WHERE key = 'GameQualitySetting'", (updated_json,))
        
        conn.commit()
        print(f"已成功将 {query_key} 的 value 中的 \"KeyCustomFrameRate\" 修改为 {setFrameRate}。")
    else:
        print(f"未找到 key 为 {query_key} 的项。")

    # 关闭数据库连接
    cursor.close()
    conn.close()
    
if __name__ == "__main__":
    # 获取路径
    desktop_path = osPath.join(osPath.expanduser("~"), "Desktop")
    path = get_path(dir_pth="C:/Wuthering Waves")
        
    target_path = path + "/Wuthering Waves Game/Wuthering Waves.exe"
    table_name = "LocalStorage"

    full_path = path + "/Wuthering Waves Game/Client/Saved/LocalStorage/LocalStorage.db"
    print("路径设置为：",full_path)

    if osPath.exists(full_path):  
        # 主菜单
        main(full_path,mainMenu())
        
        # 创建桌面快捷方式
        shortcut_path = osPath.join(desktop_path, "鸣潮-解锁帧.lnk")
        create_shortcut(target_path, shortcut_path)

        print("游戏路径为",target_path,"\n已生成桌面快捷方式")
        pressAnyKeyToContinue(1)
            
    else:
        print("路径错误，没有找到 'LocalStorage.db'")
        pressAnyKeyToContinue(1)


