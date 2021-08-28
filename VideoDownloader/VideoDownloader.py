#coding:utf-8
import requests
from os import getcwd,mkdir

def download(url,name,number,num_len):
    req = requests.get(url)
    loc = locals()
    exec('filename = "'+getcwd()+'\\'+name+'\\'+name+'_{:0>'+str(num_len)+'d}.mkv".format('+str(number)+')')
    filename = loc['filename']
    print("正在下载：%s……" % filename)
    with open(filename,'wb') as file:
        file.write(req.content)

f = open("streaming.m3u8")
print("正在读取文件……")
file_content = f.readlines()
f.close()
print("正在获取链接……")
playlist = []
for i in file_content:
    if i.startswith("https"):
        i.rstrip()
        i.lstrip()
        playlist.append(i)
name_number = input("请输入文件名，格式为“名称_起始编号数字”，名称不可以数字开头，且不能有下划线或空格。如“GoodOmens好兆头_000”是合法文件名。\n请注意，起始编号数字位数决定了文件编号位数，为防止数字溢出造成排序混乱，请计算好文件数。文件数约为时长（单位：秒）/10，以防万一可以多留一位。\n文件名：")
while 1:
    name = name_number[:name_number.find("_")]
    number_len = len(name_number[name_number.find("_")+1:])
    try:
        number = int(name_number[name_number.find("_")+1:])
        break
    except ValueError:
        name_number = input("文件名有误，请重新输入：")
mkdir(getcwd()+'\\'+name)

for j in playlist:
    download(j,name,number,number_len)
    number = number+1
print("下载完成，请使用可合并文件播放的播放器（如PotPlayer→全选播放列表后右键→合并选中的文件为单个文件播放）或用转码软件合并文件后播放。")
