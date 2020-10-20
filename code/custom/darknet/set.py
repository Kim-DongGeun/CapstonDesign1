from distutils.dir_util import copy_tree
import shutil   
import os
#.txt 경로 변경
def setTxt():
    ftrain = open("/root/volume/custom/darknet/custom_data/Train.txt", mode="rt", encoding="utf-8")
    ftest = open("/root/volume/custom/darknet/custom_data/Valid.txt", mode="rt", encoding="utf-8")
    fTrain = open("/root/volume/custom/darknet/custom_data/train.txt", mode="wt", encoding="utf-8")
    fTest = open("/root/volume/custom/darknet/custom_data/test.txt", mode="wt", encoding="utf-8")

    line = ftrain.readline()
    while line:
        fTrain.write('custom_data/images' + line[3:])
        line = ftrain.readline()

    line = ftest.readline()
    while line:
        fTest.write('custom_data/images' + line[3:])
        line = ftest.readline()
#txt 파일 라벨로 옮기기
def Move():
    dir_list = os.listdir('/root/volume/custom/darknet/custom_data/images')
    path = '/root/volume/custom/darknet/custom_data/images/'

    for Dir in dir_list:
        if os.path.isdir('/root/volume/custom/darknet/custom_data/labels/' + Dir) == False:
            os.makedirs('/root/volume/custom/darknet/custom_data/labels/' + Dir)
    
    for i in os.walk('/root/volume/custom/darknet/custom_data/images'):
        for j in range(len(i[2])):
            if i[2][j][-3:] == 'txt':
                shutil.move(i[0] + '/' + i[2][j], '/root/volume/custom/darknet/custom_data/labels/' + i[0].split('/')[-1] + '/' + i[2][j])

def rename():
    dir_list = os.listdir('/root/volume/custom/darknet/custom_data/labels')

    for Dir in dir_list:
        if 'raw' in Dir:
            Str = Dir[:Dir.find('raw')] + 'labels' + Dir[Dir.find('raw') + 3:]
            os.rename('/root/volume/custom/darknet/custom_data/labels/' + Dir, '/root/volume/custom/darknet/custom_data/labels/' + Str)
def check():
    f = open('/root/volume/custom/darknet/31000_train.log', mode='rt', encoding='utf-8')

    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    while line:
        if line[0] == 'R' or line[0] == 'L':
            line = f.readline()
            continue
        num = int(line[:line.find(':')])
        if num % 1000 == 0 or (num < 2000 and num % 200 == 0):
            print(line[:-1])
        line = f.readline()

if __name__ == "__main__":
    check()
    #rename()
    #Move()
    #check()
    #setTxt()