# by riskis7, team : Bengkulu Cyber Team.
# alat : domain grabber
# versi 3.4


import sys
import os, re, requests
from multiprocessing.dummy import Pool as ThreadPool
from time import time as timer
import json
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
import requests, re, sys, threading, json
import threading
from multiprocessing.dummy import Pool
from queue import Queue


def kentot(site):
	try:
		page = 1
		while True:
			url2 = ('{}{}.xml' .format(site,page) )
			tai = requests.get(url2)
			toket = tai.url
			if toket == site:
				print('Done Scraping ... ')
				exit()
			else:
				m = requests.get(url2).text
				memek = re.findall(r'https://webstatsdomain.org/d/(.*?)</loc>', m)
				page += 1
				print("")
				print("Scraping page {} ...  " .format(page))
				print("")
				for ye in memek:
					kontol = ye.strip()
					print(kontol) 
					open('DOMAINRESULT.txt', 'a').write('http://'+kontol+'\n')
	except Exception as e:
		pass


if __name__ == '__main__':
	"""
	try:
		mmc = "web.txt"
		a = open(mmc, 'r').read().splitlines()
		p = Pool(50)
		p.map(kentot, a)
		p.close()
		p.join()
	except Exception as e:
		print(e)
	"""
	os.system('cls' if os.name == 'nt' else 'clear')
	thread= input(' Thread : ')
	a = 'https://webstatsdomain.org/sitemap-'.splitlines()
	ThreadPool = Pool(int(thread))
	Threads = ThreadPool.map(kentot, a)
	
	
