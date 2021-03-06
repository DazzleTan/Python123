# -*- coding: utf-8 -*-
# Author  : Mifen
# Email   : 2952277346@qq.com
# Date  : 2018/9/7


import time
import turtle as t
from turtle import *

t.setup(1280,720)
t.speed(0)
t.pensize(1)
length = 13
path = 'F'
angle = 22
up()
color("#262626")
goto(-600,300)
write('Author:DazzleTan',font=("微软雅黑", 18))
goto(-600,250)
write('E-mail :377648526@qq.com',font=("微软雅黑", 18))
goto(-600,-350)
down()
expalnation = {
      'F':'画线',
      'x':'-',
      '+':'逆时针旋转',
      '-':'顺时针旋转',
      '[':'记录当前位置',
      ']':'恢复上一个位置',
      'a':'上色',
      'b':'上色',
      'c':'上色'
      }
rules = {
      'F':'aFF-[b-F+F+F]+[c+F-F-F]'
      }

      
def draw_path(path,expalnation):
      posList ,angleList= [],[]
      t.up()
      t.goto(0,-350)
      t.down()
      t.lt(90)
      for symbol in path:
            if symbol == 'F':
                  t.forward(length)
            elif symbol == '+':
                  t.left(angle)
            elif symbol == '-':
                  t.rt(angle)
            elif symbol == '[':
                  posList.append(t.pos())
                  angleList.append(t.heading())
            elif symbol == 'a':
                  t.pensize(4)
                  t.color("#8c503c")
            elif symbol == 'b':
                  t.color("#4ab441")
                  t.pensize(3)
            elif symbol == 'c':
                  t.pensize(2)
                  t.color("#18b418")
            elif symbol == ']':
                  t.up()
                  t.home()
                  t.goto(posList.pop())
                  t.left(angleList.pop())
                  t.down()

def apply_rules(path,rules):
      L = [_ for _ in path]
      for i in range(len(L)):
            symbol = L[i]
            if symbol == 'F':
                  L[i] = rules[symbol]
      path = ''.join(L)
      return path


for _ in range(4):
      path = apply_rules(path,rules)
draw_path(path,expalnation)

