import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import pprint
from stockdic import stocknumber

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name("cbworkshoptest-76588b3bb14b.json", scope)

gc = gspread.authorize(credentials)

wks = gc.open("CbWorkshoptest").worksheet("Current")
# worksheetCurrent = wks.worksheet("Current")
pp = pprint.PrettyPrinter()
glist = wks.get_all_values()
# pp.pprint(glist) #print all list in ggsheet

# stock =	1
# Low	=	2
# S1	=	3
# SMode1	=	4
# S2	=	5
# SMode2	=	6
# S3	=	7
# SMode3	=	8
# R1	=	9
# RMode1	=	10
# R2	=	11
# RMode2	=	12
# R3	=	13
# RMode3	=	14
# R4	=	15
# RMode4	=	16
# R5	=	17
# RMode5	=	18
# LastPrice	=	19
# BreakS1	=	20
# BreakS2	=	21
# BreakS3	=	22
# BreakR1	=	23
# BreakR2	=	24
# BreakR3	=	25
# BreakR4	=	26
# BreakR5	=	27
# Run1Entry	=	28
# Run1Reward	=	29
# Run1Risk	=	30
# Run1RR	=	31
# NewEntry	=	32
# NewReward	=	33
# NewRisk	=	34
# NewRR	=	35
# findstock = wks.cell(AAV,SMode3)
# print(findstock.value)

def getstockinfo(stockname):
    stock =	1
    Low	=	2
    S1	=	3
    SMode1	=	4
    S2	=	5
    SMode2	=	6
    S3	=	7
    SMode3	=	8
    R1	=	9
    RMode1	=	10
    R2	=	11
    RMode2	=	12
    R3	=	13
    RMode3	=	14
    R4	=	15
    RMode4	=	16
    R5	=	17
    RMode5	=	18
    LastPrice	=	19
    BreakS1	=	20
    BreakS2	=	21
    BreakS3	=	22
    BreakR1	=	23
    BreakR2	=	24
    BreakR3	=	25
    BreakR4	=	26
    BreakR5	=	27
    Run1Entry	=	28
    Run1Reward	=	29
    Run1Risk	=	30
    Run1RR	=	31
    NewEntry	=	32
    NewReward	=	33
    NewRisk	=	34
    NewRR	=	35
    stocknameUP = stockname.upper()
    getstocknumber = stocknumber(stocknameUP)
    stockname = wks.cell(getstocknumber,stock).value
    stocklow = wks.cell(getstocknumber,Low).value
    stocks1 = wks.cell(getstocknumber,S1).value
    stocksmode1 = wks.cell(getstocknumber,SMode1).value
    stocks2 = wks.cell(getstocknumber,S2).value
    stocksmode2 = wks.cell(getstocknumber,SMode2).value
    stocks3 = wks.cell(getstocknumber,S3).value
    stocksmode3 = wks.cell(getstocknumber,SMode3).value
    stockr1 = wks.cell(getstocknumber,R1).value
    stockrmode1 = wks.cell(getstocknumber,RMode1).value
    stockr2 = wks.cell(getstocknumber,R2).value
    stockrmode2 = wks.cell(getstocknumber,RMode2).value
    stockr3 =  wks.cell(getstocknumber,R3).value
    stockrmode3 = wks.cell(getstocknumber,RMode3).value
    stockr4 = wks.cell(getstocknumber,R4).value
    stockrmode4 = wks.cell(getstocknumber,RMode4).value
    stockr5 = wks.cell(getstocknumber,R5).value
    stockrmode5 = wks.cell(getstocknumber,RMode5).value
    stocklastprice = wks.cell(getstocknumber,LastPrice).value
    stockbreaks1 = wks.cell(getstocknumber,BreakS1).value
    stockbreaks2 = wks.cell(getstocknumber,BreakS2).value
    stockbreaks3 = wks.cell(getstocknumber,BreakS3).value
    stockbreakr1 = wks.cell(getstocknumber,BreakR1).value
    stockbreakr2 = wks.cell(getstocknumber,BreakR2).value
    stockbreakr3 = wks.cell(getstocknumber,BreakR3).value
    stockbreakr4 = wks.cell(getstocknumber,BreakR4).value
    stockbreakr5 = wks.cell(getstocknumber,BreakR5).value
    stockrunentry = wks.cell(getstocknumber,Run1Entry).value
    stockrunreward = wks.cell(getstocknumber,Run1Reward).value
    stockrunrisk = wks.cell(getstocknumber,Run1Risk).value
    stockrunrr = wks.cell(getstocknumber,Run1RR).value
    stocknewentry = wks.cell(getstocknumber,NewEntry).value
    stocknewreward = wks.cell(getstocknumber,NewReward).value
    stocknewrisk = wks.cell(getstocknumber,NewRisk).value
    stocknewrr = wks.cell(getstocknumber,NewRR).value
    return [stockname,stocklow,stocks1,stocksmode1,stocks2,stocksmode2,stocks3,stocksmode3,
    stockr1,stockrmode1,stockr2,stockrmode2,stockr3,stockrmode3,stockr4,stockrmode4,
    stockr5,stockrmode5,stocklastprice,stockbreaks1,stockbreaks2,stockbreaks3,
    stockbreakr1,stockbreakr2,stockbreakr3,stockbreakr4,stockbreakr5,stockrunentry,
    stockrunreward,stockrunrisk,stockrunrr,stocknewentry,stocknewreward,stocknewrisk,
    stocknewrr]

# stockname = "dtac"
# stockinfo = getstockinfo(stockname)
# info = "Stock Name = {}\nStock Low = {}\nStock S1 = {}\nMode Range = {}\nStock S2 = {}\nMode Range = {}\nStock S3 = {}\nMode Range = {}\n".format(stockinfo[0],stockinfo[1],stockinfo[2],stockinfo[3],stockinfo[4],stockinfo[5],stockinfo[6],stockinfo[7])
# info2 = "Stock R1 = {}\nMode Range = {}\nStock R2 = {}\nMode Range = {}\nStock R3 = {}\nMode Range = {}\nStock R4 = {}\nMode Range = {}\nStock R5 = {}\nMode Range = {}\n".format(stockinfo[8],stockinfo[9],stockinfo[10],stockinfo[11],stockinfo[12],stockinfo[13],stockinfo[14],stockinfo[15],stockinfo[16],stockinfo[17])
# info3 = "Stock Last Price = {}\nStock Break S1 = {}\nStock Break S2 = {}\nStock Break S3 = {}\nStock Break R1 = {}\nStock Break R2 = {}\nStock Break R3 = {}\nStock Break R4 = {}\nStock Break R5 = {}\n".format(stockinfo[18],stockinfo[19],stockinfo[20],stockinfo[21],stockinfo[22],stockinfo[23],stockinfo[24],stockinfo[25],stockinfo[26])
# info4 = "Stock Entry (Run) = {}\nStock Reward (Run) = {}\nStock Risk (Run) = {}\nStock RR (Run) = {}\nStock Entry (New) = {}\nStock Reward (New) = {}\nStock Risk (New) = {}\nStock RR (New) = {}".format(stockinfo[27],stockinfo[28],stockinfo[29],stockinfo[30],stockinfo[31],stockinfo[32],stockinfo[33],stockinfo[34])
# print(info+info2+info3+info4)

# stockname = "dtac"
# datainfos = getstockinfo(stockname)
# print(datainfos)

# def eyaminfo():
#     ymode1 = 3
#     ymode2 = 3
#     tmode1 = 4
#     tmode2 = 3
#     ttrend1 = 3
#     ttrend2 = 5
#     tLY1 = 5
#     tLY2 = 4
#     tJP1 = 6
#     tJP2 = 4
#     tNN11 = 7
#     tNN12 = 4
#     tNN21 = 8
#     tNN22 = 4
#     tKM11 = 9
#     tKM12 = 4
#     tKM21 = 10
#     tKM22 = 4
#     tLOW1 = 12
#     tLOW2 = 2
#     tHIGH1 = 12
#     tHIGH2 = 5
#     tSet1 = 13
#     tSet2 = 3
#     yesterdaymode = wks.cell(ymode1,ymode2).value
#     todaymode = wks.cell(tmode1,tmode2).value
#     todaytrend = wks.cell(ttrend1,ttrend2).value
#     todayLY = wks.cell(tLY1,tLY2).value
#     todayJP = wks.cell(tJP1,tJP2).value
#     todayNN1 = wks.cell(tNN11,tNN12).value
#     todayNN2 = wks.cell(tNN21,tNN22).value
#     todayKM1 = wks.cell(tKM11,tKM12).value
#     todayKM2 = wks.cell(tKM21,tKM22).value
#     todayLOW = wks.cell(tLOW1,tLOW2).value
#     todayHIGH = wks.cell(tHIGH1,tHIGH2).value
#     todaySet0 = wks.cell(tSet1,tSet2).value
#     return [yesterdaymode,todaymode,todaytrend,todayLY,todayJP,todayNN1,todayNN2,todayKM1,todayKM2,todayLOW,todayHIGH,todaySet0]

# def modeupdate(todaymode):
#     tmode1 = 4
#     tmode2 = 3
#     wks.update_cell(tmode1,tmode2,todaymode)

# def ymodeupdate(yesterdaymode):
#     ymode1 = 3
#     ymode2 = 3
#     wks.update_cell(ymode1,ymode2,yesterdaymode)

# def highupdate(todayhigh):
#     tHIGH1 = 12
#     tHIGH2 = 5
#     wks.update_cell(tHIGH1,tHIGH2,todayhigh)

# def lowupdate(todaylow):
#     tLOW1 = 12
#     tLOW2 = 2
#     wks.update_cell(tLOW1,tLOW2,todaylow)

# def resetnewday():
#     tLOW1 = 12
#     tLOW2 = 2
#     tHIGH1 = 12
#     tHIGH2 = 5
#     ymode1 = 3
#     ymode2 = 3
#     samemode1 = 2
#     samemdoe2 = 7
#     tmode1 = 4
#     tmode2 = 3
#     newset1 = 14
#     newset2 = 5
#     tmode = wks.cell(tmode1,tmode2).value
#     tmode = float(tmode)
#     if tmode > 0:
#         wks.update_cell(ymode1,ymode2,tmode)
#         wks.update_cell(tHIGH1,tHIGH2,0)
#         wks.update_cell(tLOW1,tLOW2,0)
#         wks.update_cell(tmode1,tmode2,0)
#         wks.update_cell(samemode1,samemdoe2,0)
#         wks.update_cell(newset1,newset2,0)   
#         return tmode
#     else:
#         return tmode
