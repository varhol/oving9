class Question:
    def __init__(self,spørsmål,fasit,forslag):
        self.spørsmål=spørsmål
        self.fasit= fasit
        self.forslag = forslag
        
    def __str__(self):
        
        x=0
        mulighet= ""
        for i in self.forslag:
            mulighet += "\n" + str(x) + ":" + i
            x+=1
        
        return f"{self.spørsmål} {mulighet}"
    
    def sjekk_svar(self,svar):
        #print("hva er svaret ditt?") #fjerne
        
        if svar == self.fasit:
            print("dette er riktig") # poeng += 1 
            #poeng += 1
            return True
       
        else: 
            print("dette var feil,riktig er" f"{self.forslag[self.fasit]}" ) 
            return False
    
    def korrekt_svar_tekst(self):
        return f"riktig svar er {self.forslag[self.fasit]}"
    
    

        
liste_spm = list()
txt = open("sporsmaalsfil.txt","r",encoding=("UTF8"))
for line in txt:
    line = line.strip()
    line =  line.split(":")
    spørsmål = line[0]
    fasit = int(line[1])
    forslag= line[2]
    forslag= forslag.strip()
    forslag = forslag.strip("[]")
    forslag= forslag.strip()
    forslag = forslag.split(",")
    liste_spm.append(Question(spørsmål, fasit, forslag))
    

if __name__=="__main__": 
    poeng1 = 0
    poeng2 = 0
   
    for spm in liste_spm:
        print(spm)
        play1=int(input("spiller 1: \n"))
        play2 =int(input("spiller 2: \n"))
        if spm.sjekk_svar(play1) == True:
            poeng1 += 1
        if spm.sjekk_svar(play2) == True:
            poeng2 += 1
            
    print(f"poeng1 {poeng1}")
    print(f"poeng2 {poeng2}")