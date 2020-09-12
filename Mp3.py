from random import randint

class MP3():
    sarkilar = []
    listening = True
    what = ""
    secim = 0
    volume = 25

    def menu(self):
        self.secim = int(input("""
Welcome, select an operation what you want:

Song list : {}
Playing now : {}
Volume : {}

1-Select song
2-Increase the volume
3-Decrease the volume
4-Random Song
5-Add Song
6-Delete Song
7-Exit
        
Enter a number between 1 and 7 : 
        """.format(self.sarkilar,self.what,self.volume)))
        while self.secim<1 or self.secim>7:
            self.secim = int(input("Enter a number between 1 and 7 : "))



    def sarkisec(self):
        print(self.sarkilar)
        self.what = self.sarkilar[int(input("Enter a valid song id : "))]

    def sesiArttir(self):
        increase = int(input("Enter a number what you want(for increase volume) : "))

        while increase<0 or increase>(100-self.volume):
            increase = int(input("Enter a number : "))

        self.volume += increase


    def sesiAzalt(self):
        decrease = int(input("Enter a number what you want(for decrease volume) : "))

        while decrease < 0 or decrease > self.volume:
            decrease = int("Enter a number : ")

        self.volume -= decrease

    def rasgeleSarkiSec(self):
        i = randint(0,len(self.sarkilar)-1)
        self.what = self.sarkilar[i]


    def addSong(self):
        songToAdd = input("Enter which you want to add song : ")
        self.sarkilar.append(songToAdd)

    def deleteSong(self):
        silinecek = int(input("Enter a song id what you want to delete : "))
        self.sarkilar.pop(silinecek)

    def exit(self):
        self.listening = False

myPlayer = MP3()

while myPlayer.listening:

    myPlayer.menu()
    if myPlayer.secim == 1:
        myPlayer.sarkisec()
    elif myPlayer.secim == 2:
        myPlayer.sesiArttir()
    elif myPlayer.secim == 3:
        myPlayer.sesiAzalt()
    elif myPlayer.secim == 4:
        myPlayer.rasgeleSarkiSec()
    elif myPlayer.secim == 5:
        myPlayer.addSong()
    elif myPlayer.secim == 6:
        myPlayer.deleteSong()
    elif myPlayer.secim == 7:
        myPlayer.exit()
