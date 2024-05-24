import sqlite3
from msvcrt import getch
import tkinter as tk
from tkinter import filedialog
from os import path as osPath



def get_path(dir_pth):
    root = tk.Tk()
    root.withdraw()
    f_path = filedialog.askdirectory(title="选择鸣潮主文件夹，比如 C:\\Wuthering Waves",
                                    initialdir=dir_pth)
    return f_path

    
def mainMenu():
    setFrameRateChoose = input("选择修改Fps: [1] 60fps [2] 120fps [3] 240fps [4]自己输入\n输入选项数字\n> ")
    if setFrameRateChoose == "1":
        setFrameRate = 60
    elif setFrameRateChoose == "2":
        setFrameRate = 120
    elif setFrameRateChoose == "3":
        setFrameRate = 240
    elif setFrameRateChoose == "4": 
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
        # 解析 value 中的字典
        value_dict = eval(result[0])
        value_dict["KeyCustomFrameRate"] = setFrameRate

        # 更新 value
        cursor.execute(f"UPDATE {table_name} SET value = ? WHERE key = ?", (str(value_dict), query_key))
        conn.commit()
        print(f"已成功将 {query_key} 的 value 中的字典 \"KeyCustomFrameRate\" 修改为 {setFrameRate}。")
    else:
        print(f"未找到 key 为 {query_key} 的项。")

    # 关闭数据库连接
    conn.close()
    
if __name__ == "__main__":
    table_name = "LocalStorage"
    path = get_path(dir_pth="C:/Wuthering Waves")
    full_path = path + "/Wuthering Waves Game/Client/Saved/LocalStorage" + "/LocalStorage.db"
    print("路径设置为：",full_path)
    if osPath.exists(full_path):  
        main(full_path,mainMenu())
        pressAnyKeyToContinue(1)
    else:
        print("路径错误，没有找到 'LocalStorage.db'")
        pressAnyKeyToContinue(1)
