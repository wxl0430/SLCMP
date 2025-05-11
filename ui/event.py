import pygame
from type.touching import *
from ui.toollist import *
from tool.doing import *
from tool.database import *
from type.touching import *
from tool.xyconverter import *
from tool.filewindow import *
from file.slcm import *

def init_event():
    global touching,movescreenkeylist, mousedown, ctrldown, shiftdown
    movescreenkeylist=[0,0,0,0]
    mousedown=0
    ctrldown=0
    shiftdown=0

def handle_event(screen : pygame.Surface) -> None:
    global touching, movescreenkeylist, mousedown, ctrldown, shiftdown
    nowstepsize=getstepsize()
    nowstepsize=getstepsize()
    nowscaling = getnowscaling()
    nowkeepnotmovetick=getkeepnotmovetick() 
    nowmousewheelspeed=getmousewheelspeed()
    nowscalingstepsize=getscalingstepsize()
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movescreenkeylist[0]=nowkeepnotmovetick
            if event.key == pygame.K_RIGHT:
                movescreenkeylist[1]=nowkeepnotmovetick
            if event.key == pygame.K_UP:
                movescreenkeylist[2]=nowkeepnotmovetick
            if event.key == pygame.K_DOWN:
                movescreenkeylist[3]=nowkeepnotmovetick
            if event.key == pygame.K_LSHIFT:
                shiftdown=1
            if event.key == pygame.K_LCTRL:
                ctrldown=1
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                movescreenkeylist[0]=0
            if event.key == pygame.K_RIGHT:
                movescreenkeylist[1]=0
            if event.key == pygame.K_UP:
                movescreenkeylist[2]=0
            if event.key == pygame.K_DOWN:
                movescreenkeylist[3]=0
            if event.key == pygame.K_LSHIFT:
                shiftdown=0
            if event.key == pygame.K_n:
                newnode()
            if event.key == pygame.K_l:
                newline()
            if event.key == pygame.K_LCTRL:
                ctrldown=0
            if event.key == pygame.K_z:
                if ctrldown:
                    undo()
            if event.key == pygame.K_y:
                if ctrldown:
                    redo()
            if event.key == pygame.K_s:
                if ctrldown and shiftdown:
                    savepath=filesavewindow("另存为项目文件",[("SLCM文件项目","*.slcm")],".slcm")   
                    if savepath:
                        setprojectsavepath(savepath)
                        makeslcmprojectfile(savepath)
                        messagebox("另存为成功","另存为成功")
                    else:
                        warningbox("未选择目录","另存为失败")
                elif ctrldown:
                    if getprojectsavepath()=="":
                        savepath=filesavewindow("保存项目文件",[("SLCM文件项目","*.slcm")],".slcm")
                        if savepath:
                            setprojectsavepath(savepath)
                            makeslcmprojectfile(savepath)
                            messagebox("保存成功","保存成功")
                        else:
                            warningbox("未选择目录","保存失败")
                    else:
                        makeslcmprojectfile(getprojectsavepath())
                        messagebox("保存成功","保存成功")
            if event.key == pygame.K_o:
                if ctrldown:
                    openpath=fileopenwindow("打开项目文件",[("SLCM文件项目","*.slcm")],".slcm")
                    if openpath:
                        if os.path.exists(openpath):
                            openslcmprojectfile(openpath)
                        else:
                            errorbox("文件不存在","文件不存在")
                    else:
                        warningbox("未选择文件","打开失败")
                    
        if event.type == pygame.MOUSEWHEEL:
            if event.precise_x==0.0 and event.precise_y==1.0:
                addscaling(nowscalingstepsize)
            elif event.precise_x==0.0 and event.precise_y==-1.0:
                addscaling(-nowscalingstepsize)
            else:
                movescreen(-int(event.precise_x*nowmousewheelspeed),int(event.precise_y*nowmousewheelspeed))

        if event.type == pygame.MOUSEBUTTONDOWN:
            Cdata=getimgdata()
            posx=event.pos[0]
            posy=event.pos[1]
            flag=1
            for i in range(len(Cdata)-1,-1,-1):
                nowrect=[Cdata[i]["x"],Cdata[i]["y"],Cdata[i]["x"]+Cdata[i]["width"],Cdata[i]["y"]+Cdata[i]["height"]]
                if posx>=nowrect[0] and posx<=nowrect[2] and posy>=nowrect[1] and posy<=nowrect[3]:
                    # print(Cdata[i]["name"])
                    exec(Cdata[i]["doing"])
                    flag=0
                    break
            if flag:
                if nowtouching.type=="NewNode":
                    newnodenow()
                elif nowtouching.type=="NewLine":
                    if nowtouching.args["count"]<2:
                        nowpos=screenxytodatabasexy(event.pos[0],event.pos[1])
                        reallydis=15/nowscaling
                        touchnode=findnodebyxy(nowpos[0],nowpos[1],reallydis)
                        # print(nowpos,reallydis,touchnode)
                        if touchnode:
                            nowtouching.args["count"]+=1
                            if nowtouching.args["count"]==1:
                                nowtouching.args["from_id"]=touchnode.id
                            else:
                                nowtouching.args["to_id"]=touchnode.id
                    if nowtouching.args["count"]==2:
                        newlinenow()
                else:
                    touchnode = findnodebyxy(*screenxytodatabasexy(event.pos[0],event.pos[1]),15/nowscaling)
                    if touchnode:
                        nowtouching.type="Node"
                        nowtouching.args={"id":touchnode.id,"fromx":touchnode.x,"fromy":touchnode.y}
                mousedown=1

        if event.type == pygame.MOUSEBUTTONUP:
            mousedown=0
            if nowtouching.type=="Node":
                nowxy=screenxytodatabasexy(event.pos[0],event.pos[1])
                adddoing({"type":"MoveNode","id":nowtouching.args["id"],"fromx":nowtouching.args["fromx"],"fromy":nowtouching.args["fromy"],"tox":nowxy[0],"toy":nowxy[1]})
                nowtouching.type="None"
                nowtouching.args={}
                

        if event.type == pygame.MOUSEMOTION:
            if mousedown:
                if nowtouching.type=="None":
                    movescreen(event.rel[0],event.rel[1])
                elif nowtouching.type=="Node":
                    findnode(nowtouching.args["id"]).setxy(*screenxytodatabasexy(event.pos[0],event.pos[1]))

    for i in range(4):
        if movescreenkeylist[i]==nowkeepnotmovetick or movescreenkeylist[i]==1:
            if i==0:
                movescreen(nowstepsize,0)
            if i==1:
                movescreen(-nowstepsize,0)
            if i==2:
                movescreen(0,-nowstepsize)
            if i==3:
                movescreen(0,nowstepsize)
        if movescreenkeylist[i]>1:
            movescreenkeylist[i]-=1