#!/usr/bin/env python
# -*- coding: utf8 -*-
# marutoが変更した
import matplotlib
import random
import sys

#センサ数         
S_NUM = 5000
#検知半径
SR=50


class Sensor:
    def __init__(self,id,x,y):
        self.sid=id
        self.x=x
        self.y=y
        self.cgrids=set()
        #x,yはセンサの座標
        #集合cgridsは，被覆するグリッドのidを入れる
		#集合で定義しているがリストにしてもよい
		#また，不要なら使用しなくてもよい．
class Grid:
    def __init__(self,id,x,y):
        self.gid=id
        self.x=x
        self.y=y
        self.csensors=set()
        #p,qはグリッドの座標
        #集合csensorsは，そのグリッドを被覆するセンサのidを入れる
		#集合で定義しているがリストにしてもよい
		#また，不要なら使用しなくてもよい．

#センサに対してcgridsを計算し，グリッドに対してcsensorsを計算する関数
def get_csensors(g,s_list):
    pass

#極大なセンサカバーを作成する関数
def maximal_sc(s_list,g_list):
    pass
# センサーの削減を行う


# matplotlibを使って描画ウィンドウを作成する


#センサの作成
print ("Preparing sensors ... ",end="")
S_list=[]

print ("done.")

#グリッドの作成
print ("Preparing grids ... ",end="")
G_list=[]

print ("done.")

#センサとグリッドの被覆関係を作成
print ("Computing covarage between sensors and grids ... ")

print ("\n done.")

#極大なセンサカバーを作成
#以下では，mscというセンサのリストにセンサカバーに含まれるセンサのリストが入っているものとする
print ("Computing covarage maximam sensors cover ... ",end="")
msc = []
maximal_sc(S_list,G_list)

sensor_count = len(msc)

print ("done.")

print ("The number of sensor is "+str(len(msc)))