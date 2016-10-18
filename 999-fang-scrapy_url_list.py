# -*- coding:utf-8 -*-

file = r'G:/morethan2000.txt'
fl = open(file,'r')
rl = fl.readlines()
# print rl[0].strip().split(',')
# print len(rl[0].strip().split(','))

for i in range(0,len(rl)):
	city_code =  rl[i].strip().split(',')[0]
	nb_city = len(rl[i].strip().split(','))
	city_ls = rl[i].strip().split(',')[1:]
	# print city_ls,nb_city

	for t in range(1,nb_city):
		print "http://esf."+city_code + ".fang.com/housing/"+city_ls[t-1]+"__1_0_0_0_1_0_0/"


# http://esf.suzhou.fang.com/housing/277__1_0_0_0_1_0_0/
