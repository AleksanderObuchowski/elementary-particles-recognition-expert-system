import string
t=[]
matches=[]
def setup():
    size(1000, 700)

    for i in range(0,34):
        t.append(0)
        
    for i in range(0,22):
        matches.append(0)    
    
data = ['X is indivisible',                             #0
        'X is divisible',                               #1

        'X has a half-integer spin',                    #2
        'X has an integer spin',                        #3

        'X has a non-integer charge',                   #4
        'X has an integer charge',                      #5
        'X has 0 charge',                               #6
        'X has a positive charge',                      #7
        'X has a negative charge',                      #8

        'X is in the Family I',                         #9
        'X is in the Family II',                        #10
        'X is in the Family III',                       #11

        'X is fundamental',                             #12
        'X is a hadron',                                #13

        'X is a fermion',                               #14
        'X is a boson',                                 #15
        'X is a barion',                                #16
        'X is a meson',                                 #17

        'X is a lepton',                                #18
        'X is a quark',                                 #19

        'X is an electron',                             #20
        'X is a mion',                                  #21
        'X is a taon',                                  #22
        'X is a neutrino',                              #23

        'X is a quark u',                               #24
        'X is a quark c',                               #25
        'X is a quark t',                               #26
        'X ia a quark d',                               #27
        'X is a quark s',                               #28
        'X is a quark b',                               #29
                
        'X is a Gauge boson',                           #30
        'X is a Higgs boson',                           #31
        
        'X has 0-value spin',                            #32
        'X has positive spin']                          #33
def draw():
    background(42)
    textSize(20)
    text("Primary",60,40)
    text("Additional",350,40)
    text("Information found",750,40)
    textSize(15)
    fill(255)
    stroke(255)
    kwadraciki(60,80,1,2)
    kwadraciki(60,150,3,4)
    kwadraciki(60,230,5,6)
    if(t[4]==1):
        kwadraciki(60,230,7,9)
    if(t[5]==1):
        kwadraciki(60,230,7,8)
        t[8]=0
    kwadraciki(350,-190,10,12)
    if(t[9]==1 or t[10]==1 or t[11]==1):
        t[0]=1
        t[2]=1
    fill(255)
    system()
    fill(70)
    if(mouseX>60 and mouseX<130 and mouseY>600 and mouseY<630):
        fill(100)
        if(mousePressed):
            for i in range(0,34):
                t[i]=0
    rect(60,600,100,30)
    fill(255)
    text("restart",85,620)
    
    
def system():
    czy_juz_wszystko=0                                      #Zmienna warunkująca koniec programu

    while(czy_juz_wszystko==0):
    
        if(t[0]==1):                                        #Sprawdzanie, które zasady są 1 - Matching
            if(matches[0]==0):
                matches[0]=1
        if(t[1]==1):
            if(matches[1]==0):
                matches[1]=1
        if(t[2]==1):
            if(matches[2]==0):
                matches[2]=1
        if(t[3]==1):
            if(matches[3]==0):
                matches[3]=1
        if((t[13]==1) and (t[14]==1)):
            if(matches[4]==0):
                matches[4]=1
        if((t[13]==1) and (t[15]==1)):
            if(matches[5]==0):
                matches[5]=1
        if(t[4]==1):
            if(matches[6]==0):
                matches[6]=1
        if(t[19]==1):
            if(matches[7]==0):
                matches[7]=1
        if((t[5]==1) and (t[14]==1)):
            if(matches[8]==0):
                matches[8]=1
        if((t[18]==1) and (t[8]==1) and (t[9]==1)):
            if(matches[9]==0):
                matches[9]=1
        if((t[18]==1) and (t[8]==1) and (t[10]==1)):
            if(matches[10]==0):
                matches[10]=1
        if((t[18]==1) and (t[8]==1) and (t[11]==1)):
            if(matches[11]==0):
                matches[11]=1
        if((t[18]==1) and (t[6]==1)):
            if(matches[12]==0):
                matches[12]=1
        if((t[19]==1)  and (t[7]==1) and (t[9]==1)):
            if(matches[13]==0):
                matches[13]=1
        if((t[19]==1) and (t[7]==1) and (t[10]==1)):
            if(matches[14]==0):
                matches[14]=1
        if((t[19]==1) and (t[7]==1) and (t[11]==1)):
            if(matches[15]==0):
                matches[15]=1
        if((t[19]==1) and (t[8]==1) and (t[9]==1)):
            if(matches[16]==0):
                matches[16]=1
        if((t[19]==1) and (t[8]==1) and (t[10]==1)):
            if(matches[17]==0):
                matches[17]=1
        if((t[19]==1) and (t[8]==1) and (t[11]==1)):
            if(matches[18]==0):
                matches[18]=1
        if((t[15]==1) and (t[12]==1) and (t[32]==1)):
            if(matches[19]==0):
                matches[19]=1
        if((t[15]==1) and (t[12]==1) and (t[33]==1)):
            if(matches[20]==0):
                matches[20]=1
        if((t[15]==1) and ((t[7]==1) or (t[8]==1))):
            if(matches[21]==0):
                matches[21]=1                               

        for i in range(0,22):
            if((i==21) and (matches[i]!=1)):                             #Jeśli przeszedłem przez wszystko matches i nie został żaden do odpalenia, to daję warunek kończący
                czy_juz_wszystko=1
            if(matches[i]==1):                              #Gdy znajduję pierwszy 1 - Matching, ale nie 2 -Fired, to go zmieniam na 3 - Firing
                matches[i]=3
                break

        if(matches[0]==3):                                  #Sprawdzenie, która zasada jest 3 - Firing, odpalenie jej oraz zmienienie na 2 - Fired
            t[12]=1
            matches[0]=2
        if(matches[1]==3):
            t[13]=1
            matches[1]=2
        if(matches[2]==3):
            t[14]=1
            matches[2]=2
        if(matches[3]==3):
            t[15]=1
            matches[3]=2
        if(matches[4]==3):
            t[16]=1
            matches[4]=2
        if(matches[5]==3):
            t[17]=1
            matches[5]=2
        if(matches[6]==3):
            t[19]=1
            matches[6]=2
        if(matches[7]==3):
            t[12]=1
            t[14]=1
            matches[7]=2
        if(matches[8]==3):
            t[18]=1
            matches[8]=2
        if(matches[9]==3):
            t[20]=1
            matches[9]=2
        if(matches[10]==3):
            t[21]=1
            matches[10]=2
        if(matches[11]==3):
            t[22]=1
            matches[11]=2
        if(matches[12]==3):
            t[23]=1
            matches[12]=2
        if(matches[13]==3):
            t[24]=1
            matches[13]=2
        if(matches[14]==3):
            t[25]=1
            matches[14]=2
        if(matches[15]==3):
            t[26]=1
            matches[15]=2
        if(matches[16]==3):
            t[27]=1
            matches[16]=2
        if(matches[17]==3):
            t[28]=1
            matches[17]=2
        if(matches[18]==3):
            t[29]=1
            matches[18]=2
        if(matches[19]==3):
            t[31]=1
            matches[19]=2
        if(matches[20]==3):
            t[30]=1
            matches[20]=2
        if(matches[21]==3):
            t[30]=1
            matches[21]=2                                   
    j=0
    for i in range(0,34):                                    #Wypisanie, co wiemy
        if(t[i]==1):
            text(data[i],750,80+j)
            j+=30
        
def kwadraciki(startX,startY,startNum,endNum):
     stroke(255)
     for i in range (startNum-1,endNum):
        fill(255)
        text(data[i],startX,startY+i*30)
        noFill()
        if (mouseX>startX-30 and mouseX<startX-20 and mouseY>startY-12+i*30 and mouseY<startY-2+i*30):
            fill(100)
        if(t[i]==1):
            fill(255)
        rect(startX-30,startY-12+i*30,10,10)
        if (mouseX>startX-30 and mouseX<startX-20 and mouseY>startY-12+i*30 and mouseY<startY-2+i*30 and mousePressed):
            t[i]=1
            for j in range(startNum-1,endNum):
                if(i!=j):
                    t[j]=0