# -*- coding: utf-8 -*-
# ODTÜ İLETİŞİM TOPLULUĞU 1995-2020
# MUAMMER BUĞRA KURNAZ VE ÇAĞDAŞ YARDIMCI TARAFINDAN YAZILMIŞTIR. TÜM HAKLARI SAKLIDIR.
# Bu sihirbaz python3 dili ve PyQt5 modülleri ile yazılmıştır.


import random
import sys
import time
from PyQt5.QtWidgets import QApplication, QLabel, QWidget,QMessageBox
from PyQt5.QtWidgets import QDesktopWidget, QPushButton, QLineEdit
from PyQt5.QtWidgets import QInputDialog, QHBoxLayout
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
import png
from time import process_time
global cv
cv = 0
mega_staff_list = []
mega_schedule = []
schedule_modifier = False
MEGA_STAFF_LIST = mega_staff_list
global strange_modifier
strange_modifier = False
CLASS_HOURS = []
CLASSES = []
input_string = "program.xls"
nump = 0
number_of_hours = 0
list_of_all_classes = []


answer_list = []

def main():
    global strange_modifier
    global CLASSES
    global CLASS_HOURS
    global CLASS_ACTIVITY_LIST
    CLASS_ACTIVITY_LIST = []
    global CLASS_ACTIVITIES_LIST
    CLASS_ACTIVITIES_LIST = []
    global number_of_hours
    def random_guess(num):
        a = random.random()
        if a >0.5:
            return int(num)
        else:
            return int(num-0.5)
    work = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    work[1] = "SESSİZ DÜNYA"
    work[2] = "OKYANUS ATÖLYESİ"
    work[3] = "HİKAYE TAMAMLAMA"
    work[4] = "MACERA PARKURU"
    work[5] = "BİL BAKALIM"
    work[6] = "ÇARKIFELEK"
    work[7] = "KÜTÜPHANE ETKİNLİĞİ"
    work[8] = "MAKARNA KULESİ"
    work[9] = "ÇOCUK HAKLARI ATÖLYESİ"
    work[10] = "MASKE"
    work[11] = "RÜZGAR GÜLÜ"
    work[12] = "BALON PATLATMA"
    work[13] = "ORİGAMİ"
    work[14] = "ELEKTRİK AKIMI VE EL ZİNCİRİ"
    for itemsMAIN in work:
        if strange_modifier:
            continue
        if type(itemsMAIN) == int:
            continue
        else:
            CLASS_ACTIVITY_LIST.append(itemsMAIN)
    def is_suitable(works,classs):
        if works == work[1]:
            if classs >= 5: # >= 3
                return True
            return False
        elif works == work[2]:
            if classs == 1 or classs == 2: # 3 de olur
                return True
            return False
        elif works == work[3]:
            if classs == 1 or classs == 2 : #3 de olur
                return True
            return False
        elif works == work[4]: #iki sınıf birleşiyor
            return True
        elif works == work[5] or works == work[6]:
            if classs in range(5,9):
                return True
            return False
        elif works == work[8]:
            if classs in range(5,7):# 4 de olur
                return True
            return False
        elif works == work[9]:
            if classs in range(3,6):
                return True
            return False
        elif works == work[10]:
            if classs in range(1,4):
                return True
            return False
        elif works == work[11]:
            if classs in range(2,5):
                return True
            return False
        elif works == work[12]:
            if classs in range(6,9): #5i zorla
                return True
            return False
        elif works == work[13]:
            if classs in range(8,9):
                return True
            return False
        elif works == work[14]:
            if classs in range(5,7): # 4ü zorla belki 7i de
                return True
            return False
        else:
            return False
        
    def is_suitable2(works,classs):
        if works == work[1]:
            if classs >= 3: # >= 3
                return True
            return False
        elif works == work[2]:
            if classs == 1 or classs == 2 or classs == 3:
                return True
            return False
        elif works == work[3]:
            if classs == 1 or classs == 2 or classs ==3:
                return True
            return False
        elif works == work[4]: #iki sınıf birleşiyor
            return True
        elif works == work[5] or works == work[6]:
            if classs in range(5,9):
                return True
            return False
        elif works == work[8]:
            if classs in range(4,7):# 4 de olur
                return True
            return False
        elif works == work[9]:
            if classs in range(3,6):
                return True
            return False
        elif works == work[10]:
            if classs in range(1,4):
                return True
            return False
        elif works == work[11]:
            if classs in range(2,5):
                return True
            return False
        elif works == work[12]:
            if classs in range(5,9): #5i zorla
                return True
            return False
        elif works == work[13]:
            if classs in range(8,9):
                return True
            return False
        elif works == work[14]:
            if classs in range(4,8): # 4ü zorla belki 7i de
                return True
            return False
        else:
            return False

    past_activities=[]
    for itemms in list_of_all_classes:
        past_activities.append([itemms[0],itemms[1],[]])
    

    def more_than_once(wourk):
        if wourk == work[2] or wourk == work[3] or wourk == work[8] or wourk == work[9] or wourk == work[10] or wourk == work[14]:
            return True
        return False
    
    for xpp in range(0,number_of_hours):
        k_var = 0
        activity_temp = []
        guess_yet = 0
        current_hour_list = []
        answer_list = []
        if xpp == number_of_hours -1:
            very_temporary = []
            for hites in list_of_all_classes:
                class_yet = hites[0]
                char_yet = hites[1]
                which_class = hites[2]
                answer_list.append([class_yet,char_yet,xpp+1,work[7],which_class])
                very_temporary.append(work[7])
            CLASS_ACTIVITIES_LIST.append(very_temporary)
        else:
            for ites in list_of_all_classes:
                local_list = []
                class_yet = ites[0]
                char_yet = ites[1]
                which_class = ites[2]
                modifier = True
                length=len(work)
                if guess_yet >= 100000000:
                    main()
                    strange_modifier = True
                    answer_list = []
                    k_var = 0
                    activity_temp = []
                    guess_yet = 0
                    current_hour_list = []
                    break
                while modifier == True:
                    current_guess = random_guess(length*random.random())
                    guess_yet += 1
                    work_yet = work[current_guess]
                    if guess_yet <= 100000:
                        if is_suitable(work_yet,class_yet):
                            if work_yet in local_list:
                                continue
                            else:
                                if work_yet in past_activities[k_var][2] :
                                    continue
                                elif work_yet in current_hour_list and not more_than_once(work_yet):
                                    continue
                                else:
                                    modifier = False
                                    local_list.append(work_yet)
                                    past_activities[k_var][2].append(work_yet)
                                    k_var += 1
                                    current_hour_list.append(work_yet)
                                    answer_list.append([class_yet,char_yet,xpp+1,work_yet,which_class])
                                    activity_temp.append(work_yet)
                    else:
                        if is_suitable2(work_yet,class_yet):
                            if work_yet in local_list:
                                continue
                            else:
                                if work_yet in past_activities[k_var][2] :
                                    continue
                                elif work_yet in current_hour_list and not more_than_once(work_yet):
                                    continue
                                else:
                                    modifier = False
                                    local_list.append(work_yet)
                                    past_activities[k_var][2].append(work_yet)
                                    k_var += 1
                                    current_hour_list.append(work_yet)
                                    answer_list.append([class_yet,char_yet,xpp+1,work_yet,which_class])
                                    activity_temp.append(work_yet)
            if strange_modifier:
                break
            CLASS_ACTIVITIES_LIST.append(activity_temp)
    for itemsXXX in answer_list:
        such_temp=("%d %s" % (itemsXXX[0],itemsXXX[1]))
        if such_temp not in CLASSES:
            CLASSES.append([such_temp])

    
def main2():
    global error_list
    global number_of_hours
    global nump
    global mega_schedule
    global answerTrouble
    def random_guess_from_people():
        global mega_staff_list
        global length_of_mega
        my_index = length_of_mega*random.random()
        if random.random() >0.5:
            my_index = int(my_index)
        else:
            my_index += 1
            if my_index>=length_of_mega:
                my_index -=2
            my_index = int(my_index)
        return my_index
    
    def main3(numh,numc):
        global mega_schedule
        global mega_staff_list
        mega_schedule = []
        sacred = numc
        length_of_mega = len(mega_staff_list)
        each_class = length_of_mega//numc
        ram = length_of_mega - (numc*each_class)
        for electrical_department in range(0,numh):
            liste_temporary = []
            remainder_i_wish = ram
            numc = sacred
            while numc != 0:
                if remainder_i_wish == 0:
                    liste_temporary.append(each_class)
                    numc -= 1
                elif remainder_i_wish != 0:
                    if random.random() > 0.5:
                        liste_temporary.append(each_class+1)
                        remainder_i_wish -= 1
                        numc -= 1
                    elif numc == 1:
                        liste_temporary.append(each_class+1)
                        remainder_i_wish -= 1
                        numc -= 1
                    else:
                        if numc > remainder_i_wish:
                            liste_temporary.append(each_class)
                            numc -= 1
                        else:
                            continue
            mega_schedule.append(liste_temporary)
    
    def trouble_enchanced():
        global number_of_hours
        global answerTrouble
        global length_of_mega
        global list_of_past_people
        global mega_staff_list
        global slight_modifier
        global finite_errors
        global mega_schedule
        global mega_staff_list
        slight_modifier = False
        sufficient = 0
        whole_list_of_answers = []
        while sufficient <= 1000:
            main3(number_of_hours,nump)
            answerTrouble = []
            for hoursY in range(0,number_of_hours):
                arbitrary_list = []
                for classesY in range(0,nump):
                    arbitrary_list.append([])
                answerTrouble.append(arbitrary_list)
                
            list_of_past_people = []
            for zeroindex in range(0,nump):
                list_of_past_people.append([])
            sufficient += 1
            errorX = 0
            any_list = mega_schedule
            for hoursX in range(0,number_of_hours):
                local_hour_people = []
                iteration = 0
                for classesX in range(0,nump):
                    temporary_integer = any_list[hoursX][classesX]
                    while temporary_integer!=0:
                        iteration += 1
                        if iteration >= 5000:
                            slight_modifier = True
                        so_called_index = random_guess_from_people()
                        if ((mega_staff_list[so_called_index] not in local_hour_people ) and (mega_staff_list[so_called_index] not in list_of_past_people[classesX] or slight_modifier)):
                            if slight_modifier:
                                errorX += 1
                            slight_modifier = False
                            iteration = 0
                            temporary_integer -=1
                            local_hour_people.append(mega_staff_list[so_called_index])
                            answerTrouble[hoursX][classesX].append(mega_staff_list[so_called_index])
                            list_of_past_people[classesX].append(mega_staff_list[so_called_index])
                        else:
                            continue
            whole_list_of_answers.append([answerTrouble,errorX])
            if errorX == 0:
                break
        initial_min = 1000 
        for items_not_clear in whole_list_of_answers:
            if items_not_clear[1] <initial_min:
                answerTrouble = items_not_clear[0]
                finite_errors = items_not_clear[1]
                continue
            
    def save_to_xls2():
        global answerTrouble
        global CLASSES
        global CLASS_HOURS
        global CLASS_ACTIVITY_LIST
        global CLASS_ACTIVITIES_LIST
        SCHEDULE = answerTrouble
        def hextobin(num):
            bin_num=[]
            for i in range(len(num)):
                    if num[i]== '0':
                            bin_num.append(0)
                            bin_num.append(0)
                            bin_num.append(0)
                            bin_num.append(0)                     
                    elif num[i]== '1':
                            bin_num.append(0)
                            bin_num.append(0)
                            bin_num.append(0)
                            bin_num.append(1)   
                    elif num[i]== '2':
                            bin_num.append(0)
                            bin_num.append(0)
                            bin_num.append(1)
                            bin_num.append(0)                 
                    elif num[i]== '3':
                            bin_num.append(0)
                            bin_num.append(0)
                            bin_num.append(1)
                            bin_num.append(1)   
                    elif num[i]== '4':
                            bin_num.append(0)
                            bin_num.append(1)
                            bin_num.append(0)
                            bin_num.append(0)   
                    elif num[i]== '5':
                            bin_num.append(0)
                            bin_num.append(1)
                            bin_num.append(0)
                            bin_num.append(1)   
                    elif num[i]== '6':
                            bin_num.append(0)
                            bin_num.append(1)
                            bin_num.append(1)
                            bin_num.append(0)   
                    elif num[i]== '7':
                            bin_num.append(0)
                            bin_num.append(1)
                            bin_num.append(1)
                            bin_num.append(1)   
                    elif num[i]== '8':
                            bin_num.append(1)
                            bin_num.append(0)
                            bin_num.append(0)
                            bin_num.append(0)   
                    elif num[i]== '9':
                            bin_num.append(1)
                            bin_num.append(0)
                            bin_num.append(0)
                            bin_num.append(1)   
                    elif num[i]== 'A':
                            bin_num.append(1)
                            bin_num.append(0)
                            bin_num.append(1)
                            bin_num.append(0)   
                    elif num[i]== 'B':
                            bin_num.append(1)
                            bin_num.append(0)
                            bin_num.append(1)
                            bin_num.append(1)   
                    elif num[i]== 'C':
                            bin_num.append(1)
                            bin_num.append(1)
                            bin_num.append(0)
                            bin_num.append(0)   
                    elif num[i]== 'D':
                            bin_num.append(1)
                            bin_num.append(1)
                            bin_num.append(0)
                            bin_num.append(1)   
                    elif num[i]== 'E':
                            bin_num.append(1)
                            bin_num.append(1)
                            bin_num.append(1)
                            bin_num.append(0)   
                    elif num[i]== 'F':
                            bin_num.append(1)
                            bin_num.append(1)
                            bin_num.append(1)
                            bin_num.append(1)   
                    else:
                            return []
            return bin_num
        def frame(_WIDTH_,_HEIGHT_,_THICKNESS_=0,_COLOUR_=0):
            IMAGE=[]
            ROW=[]
            for HEIGHT in range(_HEIGHT_):
                    for WIDTH in range(_WIDTH_):
                            if HEIGHT < _THICKNESS_:
                                    ROW.append(_COLOUR_)            
                            elif _HEIGHT_-_THICKNESS_<= HEIGHT < _HEIGHT_:
                                    ROW.append(_COLOUR_)
                            elif WIDTH< _THICKNESS_:
                                    ROW.append(_COLOUR_)
                            elif _WIDTH_-_THICKNESS_<= WIDTH < _WIDTH_:
                                    ROW.append(_COLOUR_)
                            else:
                                    ROW.append(255)
                    IMAGE.append(ROW.copy())
                    ROW.clear()
            return IMAGE
        def line(_LINE_WIDTH_,_LINE_HEIGHT_,LINE_TYPE,_COLOUR_=0):
            LINE=[]
            ROW=[]
            if LINE_TYPE.upper() == 'VERTICAL':
                for HEIGHT in range(_LINE_HEIGHT_):
                    for WIDTH in range(_LINE_WIDTH_):
                            ROW.append(_COLOUR_)
                    LINE.append(ROW.copy())
                    ROW.clear()
                return LINE
            elif LINE_TYPE.upper() == 'HORIZONTAL':
                for HEIGHT in range(_LINE_HEIGHT_):
                    for WIDTH in range(_LINE_WIDTH_):
                            ROW.append(_COLOUR_)
                    LINE.append(ROW.copy())
                    ROW.clear()
                return LINE
            else:
                return []
        def merge(MATRIX_1,MATRIX_2,X_POS,Y_POS):
            _HEIGHT_= len(MATRIX_2)
            _WIDTH_ = len(MATRIX_2[0])
            for HEIGHT in range(_HEIGHT_):
                    for WIDTH in range(_WIDTH_):
                            if MATRIX_1[Y_POS+HEIGHT][X_POS+WIDTH] > MATRIX_2[HEIGHT][WIDTH]:
                                    MATRIX_1[Y_POS+HEIGHT][X_POS+WIDTH]= MATRIX_2[HEIGHT][WIDTH]
            return MATRIX_1
        def cell(_CELL_WIDTH_,_CELL_HEIGHT_,_COLOUR_=255):
            IMAGE=[]
            ROW=[]
            for HEIGHT in range(_CELL_HEIGHT_):
                    for WIDTH in range(_CELL_WIDTH_):
                            ROW.append(_COLOUR_)
                    IMAGE.append(ROW.copy())
                    ROW.clear()
            return IMAGE    
        def transpose(_MATRIX_):
            T_MATRIX_=[]
            ROW=[]
            for HEIGHT in range(len(_MATRIX_[0])):
                    for WIDTH in range(len(_MATRIX_)):
                            ROW.append(_MATRIX_[WIDTH][HEIGHT])
                    T_MATRIX_.append(ROW.copy())
                    ROW.clear()
            return T_MATRIX_
        def text(_TEXT_,_COLOUR_=0):
            CHARACTERS =list(_TEXT_)
            TEXT=[]
            ROW= []
            TEXT_LENGTH=len(CHARACTERS)
            if TEXT_LENGTH == 0:
                    FONT_HEIGHT=0
                    FONT_WIDTH =0  
            else:
                    FONT_HEIGHT=len(FONT[CHARACTERS[0]])
                    FONT_WIDTH =len(FONT[CHARACTERS[0]][0])
            CODING= []
            for CHAR in range(TEXT_LENGTH):
                    CODING.append(FONT[CHARACTERS[CHAR]])
            for HEIGHT in range(FONT_HEIGHT):
                    for CHAR in range(TEXT_LENGTH):
                            for WIDTH in range(FONT_WIDTH):
                                    BIT= CODING[CHAR][HEIGHT][WIDTH]
                                    if BIT==1:
                                        ROW.append(_COLOUR_)
                                    else:
                                        ROW.append(255)
                    TEXT.append(ROW.copy())
                    ROW.clear()
            return TEXT
        def fiil(_WIDTH_,_HEIGHT_,_X_POS_,_Y_POS_,_MATRIX_):
            MATRIX=[]
            MATRIX_WIDTH=0
            MATRIX_HEIGHT=0
            ROW=[]
            for WIDTH in range(_WIDTH_):
                    ROW.append(255)
            for HEIGHT in range(_HEIGHT_):
                    MATRIX.append(ROW.copy())
            ROW.clear()
            for MATRIX_ROW in _MATRIX_:
                    for MATRIX_COLUMN in MATRIX_ROW:
                            MATRIX[_Y_POS_+MATRIX_HEIGHT][_X_POS_+MATRIX_WIDTH]= MATRIX_COLUMN
                            MATRIX_WIDTH+=1
                    MATRIX_HEIGHT+=1
                    MATRIX_WIDTH=0
            return MATRIX
        FONT={}
        CHARACTER=[]
        BIN_REP_LIST=[]
        f=open("font.txt", "r", encoding='utf-16')
        if f.mode == 'r':
            FONT_DOC =f.readlines()
        for CHAR in range(len(FONT_DOC)):
            FONT_DOC[CHAR]=FONT_DOC[CHAR].replace('$','')
            FONT_DOC[CHAR]=FONT_DOC[CHAR].replace('\n','')
            FONT_DOC[CHAR]=FONT_DOC[CHAR].replace('\t',',')
            FONT_DOC[CHAR]=FONT_DOC[CHAR].replace('; ','')
            FONT_DOC[CHAR]=FONT_DOC[CHAR].split(',')
        for CHAR in range(len(FONT_DOC)):
            CHARACTER.append(FONT_DOC[CHAR][-1])
            FONT_DOC[CHAR].pop()
            BIN_REP=[]
            for ROW in range(len(FONT_DOC[CHAR])):
                    BIN_REP.append(hextobin(FONT_DOC[CHAR][ROW]))
            BIN_REP_LIST.append(BIN_REP.copy())
            BIN_REP.clear()
        for CHAR in range(len(FONT_DOC)):
            FONT[CHARACTER[CHAR]]=BIN_REP_LIST[CHAR]
        CLASS_ACTIVITIES_LIST_LIST=[]
        for ROW in CLASS_ACTIVITIES_LIST:
            TEMP=[]
            for COLUMN in ROW:
                    TEMP.append([COLUMN])
            CLASS_ACTIVITIES_LIST_LIST.append(TEMP)
            TEMP.clear
        CLASS_HOURS.insert(0,[' '])
        for INDEX, ACTIVITY in enumerate(CLASS_ACTIVITIES_LIST_LIST):
            SCHEDULE.insert(2*INDEX,ACTIVITY)
            CLASS_HOURS.insert(2*INDEX+2,[' '])
        SCHEDULE.insert(0,CLASSES)       
        SCHEDULE=transpose(SCHEDULE)
        SCHEDULE.insert(0,CLASS_HOURS)
        SCHEDULE=transpose(SCHEDULE)
        BIN_NAME_REP={}
        BIN_NAME_DIM={}
        for NAME in MEGA_STAFF_LIST:
            BIN_NAME_REP[NAME]=text(NAME)
            HEIGHT=len(text(NAME))
            WIDTH =len(text(NAME)[0])
            BIN_NAME_DIM[NAME]=[WIDTH,HEIGHT]
        for COLUMN in CLASSES:
            for CLASS in COLUMN:
                    BIN_NAME_REP[CLASS]=text(CLASS)
                    HEIGHT= len(text(CLASS))
                    WIDTH = len(text(CLASS)[0])
                    BIN_NAME_DIM[CLASS]=[WIDTH,HEIGHT]
        for COLUMN in CLASS_HOURS:
            for HOUR in COLUMN:
                    BIN_NAME_REP[HOUR]=text(HOUR)
                    HEIGHT=len(text(HOUR))
                    if HEIGHT == 0:
                            WIDTH =0  
                    else:
                            WIDTH =len(text(HOUR)[0])
                    BIN_NAME_DIM[HOUR]=[WIDTH,HEIGHT]
        for ACTIVITY in CLASS_ACTIVITY_LIST:
            BIN_NAME_REP[ACTIVITY]=text(ACTIVITY)
            HEIGHT=len(text(ACTIVITY))
            WIDTH =len(text(ACTIVITY)[0])
            BIN_NAME_DIM[ACTIVITY]=[WIDTH,HEIGHT]

        f = open('program.png', 'wb')      # binary mode is important
        _FRAME_THICKNESS_ = 10
        _LINE_THICKNESS_  = 8
        CELL_SIZES        = []
        ROW_HEIGHT        = []
        COLUMN_WIDTH      = []
        H_CELL_POS        = []
        V_CELL_POS        = []
        V_LINE_POS        = []
        H_LINE_POS        = []

        for ROW in SCHEDULE:
            TEMP=[]
            for COLUMN in ROW:
                    HEIGHT=[]
                    WIDTH=[]
                    for MEMBER in COLUMN:
                            WIDTH.append(BIN_NAME_DIM[MEMBER][0])
                            HEIGHT.append(BIN_NAME_DIM[MEMBER][1])
                    if len(WIDTH)==0:
                            CELL_WIDTH=0
                    else:
                            CELL_WIDTH =max(WIDTH)
                            
                    if len(HEIGHT)==0:
                            CELL_HEIGHT=0
                    else:
                            CELL_HEIGHT=sum(HEIGHT)
                    TEMP.append([CELL_WIDTH,CELL_HEIGHT])
            CELL_SIZES.append(TEMP.copy())
            TEMP.clear()
        for ROW in range(len(CELL_SIZES)):
            CELL_SIZES[ROW]=transpose(CELL_SIZES[ROW])
            COLUMN_WIDTH.append(CELL_SIZES[ROW][0])
            ROW_HEIGHT.append(CELL_SIZES[ROW][1])
        COLUMN_WIDTH=transpose(COLUMN_WIDTH)
        for ROW in range(len(COLUMN_WIDTH)):
            COLUMN_WIDTH[ROW]=max(COLUMN_WIDTH[ROW])
        for ROW in range(len(ROW_HEIGHT)):
            ROW_HEIGHT[ROW]  =max(ROW_HEIGHT[ROW])
        _H_CELL_NUMBER_   = len(ROW_HEIGHT)
        _V_CELL_NUMBER_   = len(COLUMN_WIDTH)       

        _WIDTH_           = sum(COLUMN_WIDTH)+ 2 * _FRAME_THICKNESS_ + (_V_CELL_NUMBER_-1) * _LINE_THICKNESS_
        _HEIGHT_          = sum(ROW_HEIGHT)  + 2 * _FRAME_THICKNESS_ + (_H_CELL_NUMBER_-1) * _LINE_THICKNESS_

        for POS in range(_H_CELL_NUMBER_):
            H_LINE_POS.append(sum(ROW_HEIGHT[:POS+1])  +_FRAME_THICKNESS_+_LINE_THICKNESS_*POS)
        for POS in range(_V_CELL_NUMBER_):
            V_LINE_POS.append(sum(COLUMN_WIDTH[:POS+1])+_FRAME_THICKNESS_+_LINE_THICKNESS_*POS)   
        for POS in range(_H_CELL_NUMBER_):
            H_CELL_POS.append(sum(ROW_HEIGHT[:POS])    +_FRAME_THICKNESS_+_LINE_THICKNESS_*POS)
        for POS in range(_V_CELL_NUMBER_):
            V_CELL_POS.append(sum(COLUMN_WIDTH[:POS])  +_FRAME_THICKNESS_+_LINE_THICKNESS_*POS)

        w = png.Writer(_WIDTH_,_HEIGHT_, greyscale=True)

        FRAME=frame(_WIDTH_,_HEIGHT_,_FRAME_THICKNESS_)

        global IMAGE
        IMAGE=FRAME
        for V_POS in V_LINE_POS:
            V_LINE=line(_LINE_THICKNESS_,_HEIGHT_,'VERTICAL')
            IMAGE=merge(IMAGE,V_LINE,V_POS,0)
        for H_POS in H_LINE_POS:
            H_LINE=line(_WIDTH_,_LINE_THICKNESS_,'HORIZONTAL')
            IMAGE=merge(IMAGE,H_LINE,0,H_POS)

        for ROW in range(_H_CELL_NUMBER_):
            for COLUMN in range(_V_CELL_NUMBER_):
                    LINE_HEIGHT=0
                    for NAME in SCHEDULE[ROW][COLUMN]:
                            IMAGE=merge(IMAGE,BIN_NAME_REP[NAME],V_CELL_POS[COLUMN],H_CELL_POS[ROW]+LINE_HEIGHT)
                            LINE_HEIGHT+=BIN_NAME_DIM[NAME][1]
        w.write(f, IMAGE)
        f.close()

    trouble_enchanced()
    save_to_xls2()


        
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("logo2.png")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        
        self.line = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        hbox.addWidget(lbl)
        self.setLayout(hbox)
        
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Kaç saat etkinlik yapılacağını buraya giriniz:')
        self.nameLabel.move(50,750)
        self.nameLabel.adjustSize()
        
        self.name2Label = QLabel(self)
        self.name2Label.setText("%d Katılımcı girildi" % (cv))
        self.name2Label.move(30,700)
        self.name2Label.adjustSize()
        
        self.line[1] = QLineEdit(self)
        self.line[1].move(30,20)
        
        self.line[2] = QLineEdit(self)
        self.line[2].move(30,60)
        
        self.line[3] = QLineEdit(self)
        self.line[3].move(30,100)
                
        self.line[4] = QLineEdit(self)
        self.line[4].move(30,140)
                
        self.line[5] = QLineEdit(self)
        self.line[5].move(30,180)
                
        self.line[6] = QLineEdit(self)
        self.line[6].move(30,220)
                
        self.line[7] = QLineEdit(self)
        self.line[7].move(30,260)
               
        self.line[8] = QLineEdit(self)
        self.line[8].move(30,300)
                
        self.line[9] = QLineEdit(self)
        self.line[9].move(30,340)
                
        self.line[10] = QLineEdit(self)
        self.line[10].move(30,380)
                
        self.line[11] = QLineEdit(self)
        self.line[11].move(30,420)
                
        self.line[12] = QLineEdit(self)
        self.line[12].move(30,460)
        
        self.line0 = QLineEdit(self)
        self.line0.move(435,750)
        
        self.lineX = QLineEdit(self)
        self.lineX.move(30,600)

        self.resize(1080,800)
        
        pyfirebutton = QPushButton("Çalıştır!",self)
        pyfirebutton.clicked.connect(self.fire)
        pyfirebutton.resize(150,32)
        pyfirebutton.move(900, 600)
        
        pybutton = QPushButton('Verileri yükle!', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(150,32)
        pybutton.move(900, 560)
        
        pycreditsbutton = QPushButton('Hakkında',self)
        pycreditsbutton.clicked.connect(self.credits_method)
        pycreditsbutton.resize(150,32)
        pycreditsbutton.move(900,750)
        
        pyfire2button = QPushButton('Katılımcı gir:',self)
        pyfire2button.clicked.connect(self.fire2)
        pyfire2button.resize(150,32)
        pyfire2button.move(30,650)
        
        self.lineX.editingFinished.connect(self.enterPress)
        
        self.center()
        self.setWindowTitle('ODTÜ İletişim Topluluğu Paylaşım Etkinlikleri Atama Sihirbazı')
        self.setWindowIcon(QIcon('logo.png'))        
        self.show()
    
    def fire2(self):
        global length_of_mega
        global cv
        bigtext = self.lineX.text()
        if len(bigtext) >0:
            mega_staff_list.append(bigtext)
            length_of_mega = len(mega_staff_list)
            self.lineX.clear()
            cv += 1
            self.name2Label.setText("%d Katılımcı girildi" % (cv))
        
    def credits_method(self):
        bmsg = QMessageBox()
        bmsg.setWindowTitle("Hakkında:")
        bmsg.setText("ODTÜ İLETİŞİM TOPLULUĞU\nMM-Z04, ODTÜ Kampüsü, Üniversiteler Mah. Dumlupınar Blv. No:1\n06800 Çankaya/Ankara \n \nProgramı hazırlayanlar: \nMuammer Buğra KURNAZ \nODTÜ Bilgisayar Mühendisliği öğrencisi \n\nÇağdaş YARDIMCI\nODTÜ Elektrik ve Elektronik Mühendisliği öğrencisi\n\nKatkıda bulunanlar:\nÇağla BİLGİN\n\nDaha fazla bilgi için:\nuser.ceng.metu.edu.tr/~e2448660/topluluk.html")
        bmsgexe = bmsg.exec_()
    
    def clickMethod(self):
        global nump
        global list_of_all_classes
        global number_of_hours
        global CLASS_HOURS
        aptal = 0
        try:
            while True:
                aptal += 1
                stir = self.line[aptal].text()
                if len(stir) >= 3:
                    a1 = int(stir[0])
                    b1 = stir[2]
                    list_of_all_classes.append([a1,b1,nump])
                    nump += 1
                else:
                    break
            our_stir = self.line0.text()
            number_of_hours = int(our_stir)
            for havuc_borona in range(0,number_of_hours):
                initial_integer = 540
                initial_integer += (havuc_borona*50)
                outer_integer = initial_integer +40
                hours_with_havuc = initial_integer//60
                minutes_with_havuc = initial_integer -(60*hours_with_havuc)
                string_hours = str(hours_with_havuc)
                string_minutes = str(minutes_with_havuc)
                hours_with_borona = outer_integer//60
                minutes_with_borona = outer_integer - (hours_with_borona*60)
                string_hours_borona = str(hours_with_borona)
                string_minutes_borona = str(minutes_with_borona)
                if len(string_minutes) == 1:
                    string_minutes = "0"+string_minutes
                if len(string_minutes_borona) == 1:
                    string_minutes_borona = "0" + string_minutes_borona
                CLASS_HOURS.append(["%s.%s - %s.%s" %(string_hours,string_minutes,string_hours_borona,string_minutes_borona)])
                continue
            
                
                
        except ValueError:
            error_message = QMessageBox()
            error_message.setWindowTitle('Hata oluştu.')
            error_message.setText('Verilerin yüklenmesinde bir hata meydana geldi. Verileri doğru şekilde girdiğinizden emin olunuz.')
            duty = error_message.exec_()
            nump = 0
            number_of_hours = 0
            list_of_all_classes = []
            
    def enterPress(self):
        self.fire2()
    
    def fire(self):
        global mega_schedule
        global finite_schedule
        global error_list
        global finite_errors
        global second_schedule

        my_message_box = QMessageBox()
        my_message_box.setWindowTitle('Bilgilendirme')
        my_message_box.setText('Veriler doğru şekilde yüklendi. Şimdi sihirbaz çalışmaya başlayacaktır. Özellikle saat sayısı sınıf sayısından fazlaysa programın çalışması uzun bir vakit alabilir. Bu süre içerisinde sihirbazın herhani bir kısmına tıklamayınız. Sihirbaz çalışmayı tamamladığınıda sizi bilgilendirecektir. Bir çay için isterseniz. :)\nOK düğmesine tıklayınız ve sihirbazı başlatınız.')
        box_exe = my_message_box.exec_()

        main()
        main2()
        
        if finite_errors >0:
            self.popup2()
        self.popup()
        sys.exit()

        
    def popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Başarılı !")
        msg.setText("Program başarıyla tamamlandı ve program.png dosyasına kayıt yapıldı. Bu dosyayı programın çalıştığı dizinde bulabilirsiniz.\n\nTopluluğumuzun 25. yılı kutlu olsun!\n \n Programı kapatılacaktır.")
        qoqoqoqo = msg.exec_()
        
    def popup2(self):
        global finite_errors
        hele = QMessageBox()
        hele.setWindowTitle("Uyarı:")
        hele.setText("Program mecbur kaldığı için %d kez bir katılımcının bir sınıfa bir daha girmeme kuralını çiğnemiştir." % (finite_errors))
        qwert = hele.exec_()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def closeEvent(self,event):
        box = QMessageBox()
        box.setText('Çıkmak mı istiyorsunuz?')
        box.setWindowTitle('Uyarı')
        box.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        evet = box.button(QMessageBox.Yes)
        evet.setText('Evet.')
        hayir = box.button(QMessageBox.No)
        hayir.setText('Hayır.')
        box.exec_()
        if box.clickedButton() == evet:
            event.accept()
        elif box.clickedButton() == hayir:
            event.ignore()
            
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

app.exec_()
                


