# -*- coding: utf-8 -*-
import datetime,re,urllib,time,sys,os,requests,copy,json
from urllib import request as url
from clint.textui import colored, puts

def now():
	return datetime.datetime.now().strftime('%Y%m%d%H%M%S')
# 비덴트 : 121800
# 평화산업 : 090080
# STX : 011810
# STX엔진 : 077970
s = "주식코드: "
# s = "Please enter your Code: "
code = input(s)
if code == "":
	code = "005930,121800,090080,011810,077970,008970,000520,091090,067160,079660,016790,011390,003720,010950,007540,248170,004980,225530,112040"
white = '\033[0;39m'
green = '\033[0;32m'
red = '\033[01;31m'
cyen = '\033[01;29m'
blue = '\033[1;34m'
native = '\033[0;36m'
bred = '\033[0;41m'
bblue = '\033[0;44m'
yellow = '\033[1;33m'
up = "▲"
down = "▼"
data = {}
before_data = {}
while True:
	html = requests.get("https://polling.finance.naver.com/api/realtime.nhn?query=SERVICE_INDEX:KOSPI|SERVICE_ITEM:%s" % (code)).text
	html = json.loads(html)
	h = html['result']['areas']	

	# time.sleep(100)
	os.system('cls')
	adata = h[1]["datas"]
	jdata = h[0]["datas"][0]
	if len(h[0]["datas"]) > len(h[1]["datas"]):
		adata = h[0]["datas"]
		jdata = h[1]["datas"][0]

	# jisu= jdata["cv"]


	print("\n=================STATE================")
	# print(data)
	# print('{:{}{}.{}}'.format(str(jdata['cv']),'+',10,2))
	print("%sKOSPI 종합주가지수  :  %s 전일대비 %s%%  | %s%%%s\n" % (yellow,jdata['nv'],jdata['cv'],jdata['cr'],native))
	# print(name,price,price2,percent)
	for rows in adata:
		# print(rows)
		state = red
		angle = up
		back_color = bred
		strange = False
		try:
			if rows["nv"] != data[rows["cd"]]["nv"]:
				strange = True
		except:
				pass
		# print(rows)
		# print(rows['pcv'], rows["nv"], type(rows["pcv"]), type(rows["nv"]))
		try:
			if rows["nv"] < rows["pcv"]:
				state = cyen
				angle = down
				back_color = bblue
				rows["cv"] = rows["cv"]*-1


			if strange:
				print("%s%s%s (%s%s%%) %s%s / %s%s \n" % (white,back_color,rows['nm'], angle,rows['cr'], angle,rows['cv'], rows['nv'],native))
			else:
				print("%s%s%s (%s%s%s%%%s) %s%s%s%s / %s \n" % (green,rows['nm'],native, state,angle,rows['cr'],native, state,angle,rows['cv'],native, rows['nv']))
		except:
			pass

	for rows in adata:
		data[rows['cd']] = copy.deepcopy(rows)
	time.sleep(2)
	
	
	# clear()
