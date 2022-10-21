import datetime

class Save(object):
    save =[]
    def __init__(self):
        file = open("save.dat", "r")
        self.save.clear()
        try:
            for i in file:
                self.save.append(i.split(", "))
        finally:
            file.close()

    def saveFile(self):
        file = open("save.dat", "w")
        try:
            for i in self.save:
                file.writelines(i)
        finally:
            file.close()

    def dodaj(self, score):
        temp=[]
        temp.append(str(datetime.datetime.now())+", ")
        temp.append(str(score)+"\n")
        self.save.append(temp)
        self.saveFile()

    def checkScore(self, score):
        if len(self.save)<5:
            self.dodaj(score)
        else:
            for i in self.save:
                if score>int(i[1]):
                    break