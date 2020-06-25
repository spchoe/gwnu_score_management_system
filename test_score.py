class Score:
    total = []
    avg = []
    ranking = []
    context = []# 클래스 내의 두가지 이상에 사용될 메서드들을 클래스 전역변수로 선언

    def open(self):
        fp = open("score.csv", "r", encoding="utf-8")
        self.context = fp.readlines()
        fp.close()
        
    def write(self):
        for i in range(len(self.context)):
            student = self.context[i].split(',')
            kor = int(student[2])
            eng = int(student[3])
            math = int(student[4])
            self.total.append(kor + eng + math)
            self.avg.append(round(self.total[i] / 3, 2))

csp = Score()
csp.open()
csp.write()