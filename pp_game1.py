import pygame
import random
import string
import itertools
pygame.init()
bg=pygame.image.load("tt.jpg")

myfont=pygame.font.SysFont("monospace",30,True)
stfont=pygame.font.SysFont("monospace",25,True)
stfont1=pygame.font.SysFont("monospace",45,True)
o=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
#mis=pygame.mixer.music.load("tic_song.mp3")
def check(h):
    u_count=0
    com_count=0
    h[0].sort()
    h[1].sort()
    for i in range(len(h[0])-2):
        o=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        for j in o:
            if(set(j).issubset(set(h[0]))):
                u_count+=1
            elif(set(j).issubset(set(h[1]))):
                com_count+=1
    if(u_count>0):
        x=1
        return x
    elif(com_count>0):
        x=0
        return x
    else:
        x=2
        return x
def click(r):
    if(r[0]<200)and(r[1]<200):
        p=1
    elif(r[0]>200)and(r[0]<400)and(r[1]<200):
        p=2
    elif(r[0]>400)and(r[1]<200):
        p=3
    elif(r[0]<200)and(r[1]>200)and(r[1]<400):
        p=4
    elif(r[0]>200)and(r[0]<400)and(r[1]>200)and(r[1]<400):
        p=5
    elif(r[0]>400)and(r[1]>200)and(r[1]<400):
        p=6
    elif(r[0]<200)and(r[1]>400):
        p=7
    elif(r[0]>200)and(r[0]<400)and(r[1]>400):
        p=8
    elif(r[0]>400)and(r[1]>400):
        p=9
    return p

def play():
    win=pygame.display.set_mode((600,600))
    pygame.display.set_caption("Tic-Toe Game")
    myfont=pygame.font.SysFont("monospace",30,True)
    stfont=pygame.font.SysFont("monospace",25,True)
    stfont1=pygame.font.SysFont("monospace",45,True)
    pygame.mixer.music.load("tic_song.mp3")
    pygame.mixer.music.play(-1)
    pos1={1:((20,20),(180,180),(20,180),(180,20)),2:((220,20),(380,180),(220,180),(380,20)),3:((420,20),(580,180),(420,180),(580,20)),4:((20,220),(180,380),(20,380),(180,220)),5:((220,220),(380,380),(220,380),(380,220)),6:((420,220),(580,380),(420,380),(580,220)),7:((20,420),(180,580),(20,580),(180,420)),8:((220,420),(380,580),(220,580),(380,420)),9:((420,420),(580,580),(420,580),(580,420))}
    li=[1,2,3,4,5,6,7,8,9]
    pos2={1:(100,100),2:(300,100),3:(500,100),4:(100,300),5:(300,300),6:(500,300),7:(100,500),8:(300,500),9:(500,500)}
    h=[[],[]]
    winn=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    run=True
    s=0
    z=0
    s1=0
    s2=0
    opt=0
    mute=True
    String=[]
    Name=[]
    for i in string.ascii_lowercase:
        String.append(i)
    def Take_name(Name):
        pygame.time.delay(150)
        name=''
        for i in Name:
            name=name+i
        t=stfont.render("Enter Your Name and press enter",10,(255,255,255))
        win.blit(t,(40,50))
        pygame.draw.rect(win,(255,255,0),(200,100,200,40))
        pygame.draw.rect(win,(255,0,0),(200,100,200,40),1)
        t=stfont.render(name,10,(0,0,0))
        win.blit(t,(200,100))
        f=pygame.key.get_pressed()
        for i in String:
            d=String.index(i)
            if(f[97+d])and(f[303]==0)and(f[304]==0):
                Name.append(i)
            elif(f[97+d])and(f[304] or f[303]):
                Name.append(i.upper())
        if f[pygame.K_BACKSPACE]:
            del Name[len(Name)-1]
        if f[pygame.K_RETURN]:
            return name
        if f[pygame.K_SPACE]:
            Name.append(" ")
        pygame.display.update()
    while(run):
        win.blit(bg,(1,1))
        #pygame.time.delay(200)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        
        pygame.draw.rect(win,(0,255,0),(70,250,200,70))
        pygame.draw.rect(win,(0,255,0),(350,250,200,70))
        if(mute):
            #pygame.draw.rect(win,(100,100,100),(500,50,50,50))
            pygame.draw.polygon(win,(100,100,100),[(500,50),(510,50),(520,40),(520,70),(510,60),(500,60)])
            
        elif(mute==False):
            pygame.draw.polygon(win,(100,100,100),[(500,50),(510,50),(520,40),(520,70),(510,60),(500,60)])
            #pygame.draw.rect(win,(100,100,100),(500,50,50,50))
            pygame.draw.line(win,(255,0,0),(500,45),(520,65),3)
            pygame.draw.line(win,(255,0,0),(500,65),(520,45),3)
        t=stfont1.render("THE TIC TOE GAME",10,(0,0,0))
        t1=stfont.render("Vs Computer",10,(0,0,0))
        t2=stfont.render("Vs Human",10,(0,0,0))
        win.blit(t,(80,65))
        win.blit(t1,(90,270))
        win.blit(t2,(390,270))
        r=pygame.mouse.get_pos()
        if(r[0]>80)and(r[0]<260)and(r[1]>250)and(r[1]<320):
            pygame.draw.rect(win,(255,0,0),(70,250,200,70))
            win.blit(t1,(90,270))
        elif(r[0]>350)and(r[0]<530)and(r[1]>250)and(r[1]<320):
            pygame.draw.rect(win,(255,0,0),(350,250,200,70))
            win.blit(t2,(390,270))
        pygame.display.update()
        f=pygame.mouse.get_pressed()
        
        
            
        if(f[0]==1):
            
            r=pygame.mouse.get_pos()
            if(r[0]>500)and(r[0]<550)and(r[1]>40)and(r[1]<70):
                if(mute):
                    
                    pygame.mixer.music.pause()
                    pp=(pygame.mixer.music.get_pos())
                    pp=pp/1000
                    pygame.mixer.music.load("click.mp3")
                    pygame.mixer.music.play()
                    pygame.time.delay(300)
                    mute=False
                elif(mute==False):
                    
                    pygame.mixer.music.load("click.mp3")
                    pygame.mixer.music.play(0,pp)
                    pygame.time.delay(300)
                    pygame.mixer.music.load("tic_song.mp3")
                    pygame.mixer.music.play()
                    
                    mute=True
                
                
            if(r[0]>80)and(r[0]<260)and(r[1]>250)and(r[1]<320):
                opt=1
                pp=(pygame.mixer.music.get_pos())
                pp=pp/1000
                pygame.mixer.music.load("click.mp3")
                pygame.mixer.music.play()
                pygame.time.delay(300)
                #pygame.mixer.music.load("click.mp3")
                #pygame.mixer.music.play()
                break
            elif(r[0]>350)and(r[0]<530)and(r[1]>250)and(r[1]<320):
                opt=2
                pp=(pygame.mixer.music.get_pos())
                pp=pp/1000
                pygame.mixer.music.load("click.mp3")
                pygame.mixer.music.play()
                pygame.time.delay(300)
                #pygame.mixer.music.load("click.mp3")
                #pygame.mixer.music.play()
                break
    pygame.display.set_mode((600,600)).fill((0,0,0))
    pygame.display.flip()
    if(opt==1):
        pygame.mixer.music.load("tic_song.mp3")
        pygame.mixer.music.play(0,pp)
        while(run):
            
            #pygame.time.delay(100)
            #pygame.time.delay(140)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
            name=Take_name(Name)
            if(name!=None):
                break
            #pygame.display.update()
        pygame.display.set_mode((600,600)).fill((0,0,0))
        pygame.display.update()
        while(run):
            pygame.mixer.music.stop()
            #pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
    
    
            pygame.draw.line(win,(255,0,0),(1,200),(599,200),8)
            pygame.draw.line(win,(255,0,0),(1,400),(599,400),8)
            pygame.draw.line(win,(255,0,0),(200,1),(200,599),8)
            pygame.draw.line(win,(255,0,0),(400,1),(400,599),8)
            pygame.display.update()
            f=pygame.mouse.get_pressed()
            #pygame.mixer.music.load("click.mp3")
            #pygame.mixer.music.play()
            if(f[0]==1):
                pygame.mixer.music.load("click.mp3")
                pygame.mixer.music.play()
                pygame.time.delay(300)
                r=pygame.mouse.get_pos()
                p=click(r)
                if p not in li:
                    continue
                pygame.draw.line(win,(0,255,0),pos1[p][0],pos1[p][1],6)
                pygame.draw.line(win,(0,255,0),pos1[p][2],pos1[p][3],6)
                pygame.display.update()
                li.remove(p)
                h[0].append(p)
                if(s>=4):
                    break
                if(s<4):
                    if(len(h[1])==0):
                        suggestion=[]
                        if(h[0][0]==5):
                            suggestion=[1,3,7,9]
                        else:
                            for i in range(len(o)):
                                if(h[0][len(h[0])-1] in o[i]):
                                    for j in range(3):
                                        if(o[i][j]!=h[0][len(h[0])-1])and(o[i][j] in li):
                                            suggestion.append(o[i][j])
                    if(len(h[1])==1):
                        suggestion=[]
                        if(h[0][0]==5)and(h[0][1]==1):
                            suggestion=[3]
                        elif(h[0][0]==5)and(h[0][1]==3):
                            suggestion=[1]
                        elif(h[0][0]==5)and(h[0][1]==7):
                            suggestion=[9]
                        elif(h[0][0]==5)and(h[0][1]==9):
                            suggestion=[7]
                        else:
                            for i in range(len(o)):
                                if(h[0][len(h[1])-1] in o[i])and(h[0][len(h[1])-2] in o[i]):
                                    for j in range(3):
                                        if(o[i][j]!=h[0][len(h[0])-1])and(o[i][j] in li)and((o[i][j]!=h[0][len(h[0])-1])):
                                            suggestion.append(o[i][j])

                        if(len(suggestion)==0):
                            for i in range(len(o)):
                                if(h[1][len(h[1])-1] in o[i]):
                                    for j in range(3):
                                        if(o[i][j]!=h[0][len(h[0])-1])and(o[i][j] in li):
                                            suggestion.append(o[i][j])
                    if(len(h[1])>1):
                        suggestion=[]
                        gh=list(itertools.combinations(h[0],2))
                        sh=list(itertools.combinations(h[1],2))
                        for i in range(len(o)):
                            for k in range(len(sh)):
                                if(sh[k][0] in o[i])and(sh[k][1] in o[i]):
                                    for j in range(3):
                                        if((o[i][j]!=sh[k][1])or(o[i][j]!=sh[k][0]))and(o[i][j] in li):
                                            #print(o[i][j],sh)
                                            suggestion.append(o[i][j])
                        if(len(suggestion)>0):
                            pass
                        else:
                            for i in range(len(o)):
                                for k in range(len(gh)):
                                    if(gh[k][0] in o[i])and(gh[k][1] in o[i]):
                                        for j in range(3):
                                            if(o[i][j]!=gh[k][1])and(o[i][j] in li)and(o[i][j]!=gh[k][0]):
                                                suggestion.append(o[i][j])
                        print(suggestion)
                        if(len(suggestion)==0):
                            for i in range(len(o)):
                                if(h[1][len(h[1])-1] in o[i]):
                                    for j in range(3):
                                        if(o[i][j]!=h[0][len(h[0])-1])and(o[i][j] in li):
                                            suggestion.append(o[i][j])
                    if(len(h[0])>=3):
                        if(check(h)==1):

                            z+=1
                            t=myfont.render(name+" won the game.",10,(255,255,255))
                            break
                        elif(check(h)==0):
                            z+=1
                            t=myfont.render("Computer won the game.",10,(255,255,255))
                            break   
                    if(len(suggestion)!=0):        
                        p=random.choice(suggestion)
                    else:
                        p=random.choice(li)
                    #print(suggestion)
                    pygame.draw.circle(win,(0,0,255),pos2[p],70,6)
                    pygame.display.update()
                    li.remove(p)
                    h[1].append(p)
                    s+=1
            
                if(len(h[0])>=3):
                    if(check(h)==1):

                        z+=1
                        t=myfont.render(name+" won the game.",10,(255,255,255))
                        break
                    elif(check(h)==0):
                        z+=1
                        t=myfont.render("Computer won the game.",10,(255,255,255))
                        break
            pygame.display.update()
#pygame.display.set_mode((600,600)).fill((0,0,0))
#pygame.display.flip()
        while(run):
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
            if(check(h)==1)and(z==0):
                t=myfont.render(name+" won the game.",10,(255,255,255))
            elif(check(h)==0)and(z==0):
                t=myfont.render("Computer won the game.",10,(255,255,255))
            elif(z==0):
                t=myfont.render("It is a draw.",10,(255,255,255))
            win.blit(t,(90,300))
            pygame.display.update()
            pygame.draw.rect(win,(0,255,0),(150,450,200,70))
            u1=myfont.render("Replay",10,(255,255,255))
            win.blit(u1,(190,465))
            r=pygame.mouse.get_pos()
            if(r[0]>150)and(r[0]<350)and(r[1]>450)and(r[1]<520):
                pygame.draw.rect(win,(255,0,0),(150,450,200,70))
                win.blit(u1,(190,465))
            f=pygame.mouse.get_pressed()
            if(f[0]==1):
                pygame.mixer.music.load("click.mp3")
                pygame.mixer.music.play()
                pygame.time.delay(300)
                r=pygame.mouse.get_pos()
                if(r[0]>150)and(r[0]<350)and(r[1]>450)and(r[1]<520):
                    play()
        pygame.quit()

    elif(opt==2):
        while(run):
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
    
    
            pygame.draw.line(win,(255,0,0),(1,200),(599,200),8)
            pygame.draw.line(win,(255,0,0),(1,400),(599,400),8)
            pygame.draw.line(win,(255,0,0),(200,1),(200,599),8)
            pygame.draw.line(win,(255,0,0),(400,1),(400,599),8)
            pygame.display.update()
            f=pygame.mouse.get_pressed()
            #pygame.mixer.music.load("click.mp3")
            #pygame.mixer.music.play(-0)
            if(f[0]==1)and(s1==s2)and(s2<=4):
                pygame.mixer.music.load("click.mp3")
                pygame.mixer.music.play()
                pygame.time.delay(300)
                r=pygame.mouse.get_pos()
                p=click(r)
                if p not in li:
                    continue
                pygame.draw.line(win,(0,255,0),pos1[p][0],pos1[p][1],6)
                pygame.draw.line(win,(0,255,0),pos1[p][2],pos1[p][3],6)
                pygame.display.update()
                li.remove(p)
                h[0].append(p)
                s1+=1
            
            elif(f[0]==1)and(s1!=s2)and(s2<4):
                pygame.mixer.music.load("click.mp3")
                pygame.mixer.music.play()
                pygame.time.delay(300)
                r=pygame.mouse.get_pos()
                p=click(r)
                if p not in li:
                    continue
                pygame.draw.circle(win,(0,0,255),pos2[p],70,6)
                pygame.display.update()
                li.remove(p)
                h[1].append(p)
                s2+=1
            elif(s2>=4)and(s1==5):
                break
            if(len(h[0])>=3):
                if(check(h)==1):
                    z+=1
                    t=myfont.render("Player 1 won the game.",10,(255,255,255))
                    break
                elif(check(h)==0):
                    z+=1
                    t=myfont.render("Player 2 won the game.",10,(255,255,255))
                    break
            pygame.display.update()
        while(run):
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
            if(check(h)==1)and(z==0):
                t=myfont.render("Player 1 won the game.",10,(255,255,255))
            elif(check(h)==0)and(z==0):
                t=myfont.render("Player 2 won the game.",10,(255,255,255))
            elif(check(h)==2)and(z==0):
                t=myfont.render("It is a draw.",10,(255,255,255))
            win.blit(t,(130,300))
            pygame.display.update()
            pygame.draw.rect(win,(0,255,0),(150,450,200,70))
            u1=myfont.render("Replay",10,(255,255,255))
            win.blit(u1,(190,465))
            r=pygame.mouse.get_pos()
            if(r[0]>150)and(r[0]<350)and(r[1]>450)and(r[1]<520):
                
                pygame.draw.rect(win,(255,0,0),(150,450,200,70))
                win.blit(u1,(190,465))
            f=pygame.mouse.get_pressed()
            if(f[0]==1):
                pygame.mixer.music.load("click.mp3")
                pygame.mixer.music.play()
                pygame.time.delay(300)
                r=pygame.mouse.get_pos()
                if(r[0]>150)and(r[0]<350)and(r[1]>450)and(r[1]<520):
                    play()
    pygame.quit()
play()
