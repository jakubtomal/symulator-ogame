
class dane_statkow:
    def __init__(self):
        
        tmplist=[]
        file1 = open('Dane_statkow.txt' , 'r')
        file1.readline()
        for i in file1:
            tmplist.append(i[3:-1].split(','))
        file1.close()
            
        self.mt = tmplist[0]
        self.dt = tmplist[1]
        self.lm = tmplist[2]
        self.cm = tmplist[3]
        self.kr = tmplist[4]
        self.ow = tmplist[5]
        self.sk = tmplist[6]
        self.re = tmplist[7]
        self.ss = tmplist[8]
        self.bb = tmplist[9]
        self.ns = tmplist[10]
        self.gs = tmplist[11]
        self.pa = tmplist[12]
        
        
        
