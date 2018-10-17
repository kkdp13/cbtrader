import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import pprint

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name("cbworkshoptest-76588b3bb14b.json", scope)

gc = gspread.authorize(credentials)

wks = gc.open("CbWorkshoptest").worksheet("Current")
# worksheetCurrent = wks.worksheet("Current")
# pp = pprint.PrettyPrinter()
# glist = wks.get_all_values()
# pp.pprint(glist) #print all list in ggsheet
def breakr1():
    stockdicts = {
        "AAV":3,
        "ADVANC":4,
        "AMATA":5,
        "AOT":6,
        "AP":7,
        "BANPU":8,
        "BBL":9,
        "BCH":10,
        "BCP":11,
        "BCPG":12,
        "BDMS":13,
        "BEAUTY":14,
        "BEM":15,
        "BGRIM":16,
        "BH":17,
        "BJC":18,
        "BLA":19,
        "BLAND":20,
        "BPP":21,
        "BTS":22,
        "CBG":23,
        "CENTEL":24,
        "CHG":25,
        "CK":26,
        "CKP":27,
        "COM7":28,
        "CPALL":29,
        "CPF":30,
        "CPN":31,
        "DELTA":32,
        "DTAC":33,
        "EA":34,
        "EGCO":35,
        "EPG":36,
        "ERW":37,
        "ESSO":38,
        "GFPT":39,
        "GGC":40,
        "GLOBAL":41,
        "GLOW":42,
        "GPSC":43,
        "GUNKUL":44,
        "HANA":45,
        "HMPRO":46,
        "INTUCH":47,
        "IRPC":48,
        "ITD":49,
        "IVL":50,
        "KBANK":51,
        "KCE":52,
        "KKP":53,
        "KTB":54,
        "KTC":55,
        "LH":56,
        "LPN":57,
        "MAJOR":58,
        "MEGA":59,
        "MINT":60,
        "MTC":61,
        "ORI":62,
        "PRM":63,
        "PSH":64,
        "PSL":65,
        "PTG":66,
        "PTT":67,
        "PTTEP":68,
        "PTTGC":69,
        "QH":70,
        "RATCH":71,
        "ROBINS":72,
        "RS":73,
        "SAWAD":74,
        "SCB":75,
        "SCC":76,
        "SGP":77,
        "SIRI":78,
        "SPALI":79,
        "SPRC":80,
        "STA":81,
        "STEC":82,
        "SUPER":83,
        "TASCO":84,
        "TCAP":85,
        "THAI":86,
        "THANI":87,
        "TISCO":88,
        "TKN":89,
        "TMB":90,
        "TOA":91,
        "TOP":92,
        "TPIPL":93,
        "TPIPP":94,
        "TRUE":95,
        "TTW":96,
        "TU":97,
        "TVO":98,
        "UV":99,
        "WHA":100,
        "WHAUP":101,
        "WORK":102
    }

    stock =	1
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
    BreakR1	=	23
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
    stocklistr1 = []
    # stocklistr2 = []
    # stocklistr3 = []
    # stocklistr4 = []
    # stocklistr5 = []
    for stockdict in stockdicts.values():
        # stocknameUP = stockname.upper()
        getstocknumber = stockdict #stocknumber(stocknameUP)
        # print(getstocknumber)
        stockname = wks.cell(getstocknumber,stock).value
        # print(stockname)
        # stocklow = wks.cell(getstocknumber,Low).value
        # stocks1 = wks.cell(getstocknumber,S1).value
        # stocksmode1 = wks.cell(getstocknumber,SMode1).value
        # stocks2 = wks.cell(getstocknumber,S2).value
        # stocksmode2 = wks.cell(getstocknumber,SMode2).value
        # stocks3 = wks.cell(getstocknumber,S3).value
        # stocksmode3 = wks.cell(getstocknumber,SMode3).value
        # stockr1 = wks.cell(getstocknumber,R1).value
        # stockrmode1 = wks.cell(getstocknumber,RMode1).value
        # stockr2 = wks.cell(getstocknumber,R2).value
        # stockrmode2 = wks.cell(getstocknumber,RMode2).value
        # stockr3 =  wks.cell(getstocknumber,R3).value
        # stockrmode3 = wks.cell(getstocknumber,RMode3).value
        # stockr4 = wks.cell(getstocknumber,R4).value
        # stockrmode4 = wks.cell(getstocknumber,RMode4).value
        # stockr5 = wks.cell(getstocknumber,R5).value
        # stockrmode5 = wks.cell(getstocknumber,RMode5).value
        # stocklastprice = wks.cell(getstocknumber,LastPrice).value
        # stockbreaks1 = wks.cell(getstocknumber,BreakS1).value
        # stockbreaks2 = wks.cell(getstocknumber,BreakS2).value
        # stockbreaks3 = wks.cell(getstocknumber,BreakS3).value
        stockbreakr1 = wks.cell(getstocknumber,BreakR1).value
        # print(stockbreakr1)
        # stockbreakr2 = wks.cell(getstocknumber,BreakR2).value
        # stockbreakr3 = wks.cell(getstocknumber,BreakR3).value
        # stockbreakr4 = wks.cell(getstocknumber,BreakR4).value
        # stockbreakr5 = wks.cell(getstocknumber,BreakR5).value
        # stockrunentry = wks.cell(getstocknumber,Run1Entry).value
        # stockrunreward = wks.cell(getstocknumber,Run1Reward).value
        # stockrunrisk = wks.cell(getstocknumber,Run1Risk).value
        # stockrunrr = wks.cell(getstocknumber,Run1RR).value
        # stocknewentry = wks.cell(getstocknumber,NewEntry).value
        # stocknewreward = wks.cell(getstocknumber,NewReward).value
        # stocknewrisk = wks.cell(getstocknumber,NewRisk).value
        # stocknewrr = wks.cell(getstocknumber,NewRR).value
        if stockbreakr1 == "Yes":
            if stocklistr1 == "":
                stocklistr1 = stockname
                # print("stocklistr1 created")
            else:
                stocklistr1.append(stockname)
                # print("stocklistr1 added")
    #     print(stocklistr1)
    #     if stockbreakr2 == "Yes":
    #         stocklistr2.append(stockname)
    #     if stockbreakr3 == "Yes":
    #         stocklistr3.append(stockname)
    #     if stockbreakr4 == "Yes":
    #         stocklistr4.append(stockname)
    #     if stockbreakr5 == "Yes":
    #         stocklistr5.append(stockname)
    return stocklistr1

# stocklistr1 = breakr1()
# print(stocklistr1)
# print("----"*10)
# for x in stocklistr1:
#     print(x)
# number = len(stocklistr1)
# numbertext = "stock list r1 {}".format(number)
# print(numbertext)
    # print("----"*10)
    # for x in stocklistr2:
    #     print(x)
    # print("----"*10)
    # for x in stocklistr3:
    #     print(x)
    # print("----"*10)
    # for x in stocklistr4:
    #     print(x)
    # print("----"*10)
    # for x in stocklistr5:
    #     print(x)
    # print("----"*10)