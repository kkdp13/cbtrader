#!C:/Users/Tatum/AppData/Local/Programs/Python/Python37/python.exe
# print("Content-type: text/html")
# print()
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 12:04:11 2018

@author: Tatum

version 1.00
  -create bot for eyam
"""

from flask import Flask, request
import json
import requests
from googlesheet import getstockinfo
from breakr1 import breakr1

# ตรง YOURSECRETKEY ต้องนำมาใส่เองครับจะกล่าวถึงในขั้นตอนต่อๆ ไป
global LINE_API_KEY
# ห้ามลบคำว่า Bearer ออกนะครับเมื่อนำ access token มาใส่
LINE_API_KEY = 'Bearer pi/PPBybqenSQhskt2bdBpV+OXZTiA1SR96ef++xlwEGgILVvbZ+gqgnZto6woGcMTg85fHs4K+vTv4sCyDvFRxOu/F7h7rhrKrVP1PlCruWEga2G2nX+T/s5ntyC1lQDIbma7+QZGhCZsue/+tkggdB04t89/1O/w1cDnyilFU='

app = Flask(__name__)
 
@app.route('/')
def index():
    return 'This is chatbot server for eyam.'
@app.route('/bot', methods=['POST'])

def bot():
    # ข้อความที่ต้องการส่งกลับ
    replyQueue = list()
   
    # ข้อความที่ได้รับมา
    msg_in_json = request.get_json()
    # msg_in_string = json.dumps(msg_in_json)
    # writeindb(msg_in_json)    
    # with open('datacollection.json', 'w') as writefile:
    #    json.dump(msg_in_json, writefile)
    
    # Token สำหรับตอบกลับ (จำเป็นต้องใช้ในการตอบกลับ)
    replyToken = msg_in_json["events"][0]['replyToken']
    
    # ส่วนนี้ดึงข้อมูลพื้นฐานออกมาจาก json (เผื่อ)
    # userID =  msg_in_json["events"][0]['source']['userId']
    # msgType =  msg_in_json["events"][0]['message']['type']
    
    # ตรวจสอบว่า ที่ส่งเข้ามาเป็น text รึป่าว (อาจเป็น รูป, location อะไรแบบนี้ได้ครับ)
    # แต่ก็สามารถประมวลผลข้อมูลประเภทอื่นได้นะครับ
    # เช่น ถ้าส่งมาเป็น location ทำการดึง lat long ออกมาทำบางอย่าง เป็นต้น
    # if msgType != 'text':
    #    reply(replyToken, ['Only text is allowed.'])
    #    return 'OK',200
    
    # ตรงนี้ต้องแน่ใจว่า msgType เป็นประเภท text ถึงเรียกได้ครับ 
    # lower เพื่อให้เป็นตัวพิมพ์เล็ก strip เพื่อนำช่องว่างหัวท้ายออก ครับ
    text = msg_in_json["events"][0]['message']['text'].lower().strip()
    textstart = text[0]
    
    # if textstart == '/':
    #     if text[1] == 'b':
    #         stocklistr1 = breakr1()
    #         number = len(stocklistr1)
    #         numbertext = "stock list r1 {}".format(number)
    #         replyQueue.append(numbertext)
    #         reply(replyToken, replyQueue[:5])
    #     elif text[1] == 'y':
    #         yesterdaymode = text.split(",")[1]
    #         ymodeupdate(yesterdaymode)
    #         replyQueue.append("ymode updated : {}".format(yesterdaymode))
    #         reply(replyToken, replyQueue[:5])
    #     elif text[1] == 'h':
    #         todayHIGH = text.split(",")[1]
    #         highupdate(todayHIGH)
    #         replyQueue.append("HIGH updated : {}".format(todayHIGH))
    #         reply(replyToken, replyQueue[:5])
    #     elif text[1] == 'l':
    #         todayLOW = text.split(",")[1]
    #         lowupdate(todayLOW)
    #         replyQueue.append("LOW updated : {}".format(todayLOW))
    #         reply(replyToken, replyQueue[:5])
    #     elif text[1] == 'r':
    #         resetdone = resetnewday()
    #         if resetdone > 0:
    #             replyQueue.append("reset")
    #             reply(replyToken, replyQueue[:5])
    #         else:
    #             replyQueue.append("กด reset ไปแล้วครับ")
    #             reply(replyToken, replyQueue[:5])   
        # return 'OK', 200
    if textstart == '=':
        stockinfo = getstockinfo(text[1:])
        """stockname,stocklow,stocks1,stocksmode1,stocks2,stocksmode2,
        stocks3,stocksmode3,stockr1,stockrmode1,stockr2,stockrmode2,
        stockr3,stockrmode3,stockr4,stockrmode4,stockr5,stockrmode5,
        stocklastprice,stockbreaks1,stockbreaks2,stockbreaks3,
        stockbreakr1,stockbreakr2,stockbreakr3,stockbreakr4,
        stockbreakr5,stockrunentry,stockrunreward,stockrunrisk,stockrunrr,
        stocknewentry,stocknewreward,stocknewrisk,stocknewrr"""
        info = "Stock Name = {}\nStock Low = {}\nStock S1 = {}\nMode Range = {}\nStock S2 = {}\nMode Range = {}\nStock S3 = {}\nMode Range = {}\n".format(stockinfo[0],stockinfo[1],stockinfo[2],stockinfo[3],stockinfo[4],stockinfo[5],stockinfo[6],stockinfo[7])
        info2 = "Stock R1 = {}\nMode Range = {}\nStock R2 = {}\nMode Range = {}\nStock R3 = {}\nMode Range = {}\nStock R4 = {}\nMode Range = {}\nStock R5 = {}\nMode Range = {}\n".format(stockinfo[8],stockinfo[9],stockinfo[10],stockinfo[11],stockinfo[12],stockinfo[13],stockinfo[14],stockinfo[15],stockinfo[16],stockinfo[17])
        info3 = "Stock Last Price = {}\nStock Break S1 = {}\nStock Break S2 = {}\nStock Break S3 = {}\nStock Break R1 = {}\nStock Break R2 = {}\nStock Break R3 = {}\nStock Break R4 = {}\nStock Break R5 = {}\n".format(stockinfo[18],stockinfo[19],stockinfo[20],stockinfo[21],stockinfo[22],stockinfo[23],stockinfo[24],stockinfo[25],stockinfo[26])
        info4 = "Stock Entry (Run) = {}\nStock Reward (Run) = {}\nStock Risk (Run) = {}\nStock RR (Run) = {}\nStock Entry (New) = {}\nStock Reward (New) = {}\nStock Risk (New) = {}\nStock RR (New) = {}".format(stockinfo[27],stockinfo[28],stockinfo[29],stockinfo[30],stockinfo[31],stockinfo[32],stockinfo[33],stockinfo[34])
        replyQueue.append(info+info2+info3+info4)
        reply(replyToken, replyQueue[:5])
        return 'OK', 200
    elif textstart == '.':
        vdoLink = "https://github.com/kkdp13/cbtrader/blob/master/juti.mp4"
        replyQueue.append(vdoLink)
        replyvdo(replyToken, replyQueue[:5])
        return 'OK', 200
    else:
        # replyQueue.append('please start with / for asking bot')
        # reply(replyToken, replyQueue[:5]) 
        return 'OK', 200
 
def reply(replyToken, textList):
    # Method สำหรับตอบกลับข้อความประเภท text กลับครับ เขียนแบบนี้เลยก็ได้ครับ
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
    msgs = []
    for text in textList:
        msgs.append({
            "type":"text",
            "text":text
        })
    data = json.dumps({
        "replyToken":replyToken,
        "messages":msgs
    })
    requests.post(LINE_API, headers=headers, data=data)
    return

def replyvdo(replyToken, vdoLink):
    # Method สำหรับตอบกลับข้อความประเภท text กลับครับ เขียนแบบนี้เลยก็ได้ครับ
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
    video = []
    for vdo in vdoLink:
        video.append({
            "type":"video",
            "originalContentUrl":vdo,
            "previewImageUrl": "https://example.com/preview.jpg"
        })
    data = json.dumps({
        "replyToken":replyToken,
        "messages":video
    })
    requests.post(LINE_API, headers=headers, data=data)
    return

if __name__ == '__main__':
    app.run()
