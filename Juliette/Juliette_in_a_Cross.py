# coding=utf-8
from browser import document,html
can1 = document['image']
ctx_img = can1.getContext("2d")
can2 = document['text']
ctx_txt = can2.getContext("2d")
room = "square.jpg"
def draw(event):
    ctx_img.drawImage(html.IMG(src=room),0,0,680,480)
document["start"].bind("click",draw);

#--------------定义类-----------------#
class room:
    #name：room名字；ju：朱丽叶；npc：三维数组[名字，x坐标，y坐标]
    def __init__(self,name,ju,npc):
        self.name = name
        self.ju = ju
        self.npc = npc
        ctx_img.clearRect(0,0,680,480)
        ctx_img.drawImage(html.IMG(src=room),0,0,50,50)
        ctx_txt.clearRect(0,0,680,90)