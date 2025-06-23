import random
#가위바위보 게임한판 - computer, person, 승부 여부
class GameData:
    #변수 선언을 생성자에서 하자 : 이유, 그래야 객체가 생성될때마다 
    #새로운 메모리를 만들어준다.
    def __init__(self):
        self.computre = 0
        self.person = 0
        self.winner = 0

    def gameStart(self):
        self.computer = random.randint(1,3)
        self.person = int(input("1. 가위, 2. 바위, 3. 보 : "))
        self.winner = self.iswinner()

    def iswinner(self):
        if self.computer == self.person:
            return 3 #무승부
        #명령어가 한문장 이상일때 연결하는 문자 \ 양쪽에 공백 필요함
        if (self.computer == 1 and self.person ==3) or  \
            (self.computer == 2 and self.person ==1) or \
            (self.computer == 3 and self.person ==2):
            return 1 #컴퓨터 승
        return 2 #사람 승
    
    def printLog(self):
        print(f'컴퓨터:{self.computer}, 사람:{self.person}, 승자:{self.winner}')

class Game:
    titles1 = ["", "가위", "바위", "보"]
    titles2 = ["", "컴퓨터승", "사람승", "무승부"]

    def __init__(self):
        self.gameList = []

    def printLog(self, g):
        print(f'컴퓨터 : {self.titles1[g.computer]}', end = "\t")
        print(f'사람 : {self.titles1[g.person]}', end = "\t")
        print(f'승부 : {self.titles2[g.winner]}')

    def start(self):
        while True:
            g = GameData()
            g.gameStart()
            # g.printLog()
            self.printLog(g)
            self.gameList.append(g)

            again = input("게임을 계속 하시겠습니까? (1. 계속 2. 종료))")
            if again != "1":
                return
            
    def printResult(self):
        print(f'총 {len(self.gameList)}번 수행함')
        for g in self.gameList:
            self.printLog(g)

    def mainStart(self):

        self.start()
        self.printResult()
    
if __name__ == "__main__": #프로그램 시작 시 처음 실행되는 함수 (테스트로 암기해버리자!)
    # g = GameData() #객체 생성
    # g.gameStart() #g -> self로 전달된다.
    # g.printLog()
    game = Game()
    game.mainStart()
