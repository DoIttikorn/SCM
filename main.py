"""
    pip3 install requests  datetime Openpyxl
    
"""
import json
import time
import os
import requests
import platform
from datetime import datetime
from openpyxl import Workbook, worksheet


def Getjson(str: str) -> dict:
    r = requests.get(str)
    return r


def CreateTimeDateValue(timeValues: list) -> list:
    for xran in timeValues:
        timeStamp = xran[0] // 1000
        dt_object = datetime.fromtimestamp(timeStamp)
        timeValues[0][0] = dt_object

    return timeValues


def CheckOSAndFindAddressDesktop() -> str:
    name = platform.system()
    if name == 'Windows':
        DesktopAddress = os.path.join(os.path.join(
            os.environ['USERPROFILE']), 'Desktop')
        # Prints: C:\Users\sdkca\Desktop
        # print("The Desktop path is: " + desktop)
    if name == 'Linux':
        DesktopAddress = os.path.join(
            os.path.join(os.environ['HOME']), 'Desktop')
    return DesktopAddress


def SaveValuesExcel(result: list, columnName: str, address):
    pass


if __name__ == "__main__":
    t0 = time.time()

    str = 'https://api.netpie.io/feed/Rapoo?apikey=8YzoLCrqTRZXLv4YVW5IvmGJoEgXByuI&granularity=15minutes&since=1year&fbclid=IwAR2JA_UpUFyW_dvOpxG1s7QdB021EzpxXa7EDlM5vgnSwmBaN1ueOuo0DjQ'
    # Get text in String
    StringInformationWeb = Getjson(str)
    # เป็นค่าภายในให้เป็น ่json ใน python อยู่ในรูป dict
    jsonContent = StringInformationWeb.json()
    # เลือกส่วนที่เป็นข้อมูล
    data = jsonContent.get('data')
    # วนลูปเพื่อเอาค่าแต่ละ ข้อมูลออกมา เช่น อุณหภูมิ ,ความดัน
    for typeData in data:
        # ค่าตัวเลขจะอยู่ใน values
        values = typeData.get('values')
        #  ชื่อคอลัมเอาไว้ใส่ใน excel
        columnName = typeData.get('attr')
        #  เอาค่าเวลากับค่าผลลัพธ์ส่งไปเป็น list เป็น timestamp เป็นวันเวลาปกติ เก้บในตัวแปร succ
        succ = CreateTimeDateValue(values)
        desktopAddress = CheckOSAndFindAddressDesktop()
        # ทำการ save ค่าลงใน excel
        SaveValuesExcel(succ, columnName, desktopAddress)

    t1 = time.time()

    total = t1-t0
    print("\n\n Performance python file : ", total)
