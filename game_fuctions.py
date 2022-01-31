import random
from random import choice

################################
###   產生可以刪除的各種可能   ###
################################
def genChoice(layer):
    
    if      layer == 3:
            oneChoice   = [ 1, 2, 3, 4, 5, 6]
            twoChoice   = [ (2,3), (4,5), (5,6),
                            (1,2), (2,4), (3,5),
                            (1,3), (3,6), (2,5)]
            thrChoice   = [ (4,5,6),
                            (1,2,4),
                            (1,3,6)]
    elif    layer == 4:
            oneChoice   = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            twoChoice   = [ (2,3), (4,5), (5,6), (7,8), (8,9), (9,10),
                            (1,2), (2,4), (4,7), (3,5), (5,8), (6,9),
                            (1,3), (3,6), (6,10), (2,5), (5,9), (4,8)]
            thrChoice   = [ (4,5,6), (7,8,9), (8,9,10),
                            (3,5,8), (1,2,4), (2,4,7),
                            (2,5,9), (1,3,6), (3,6,10)]
    elif    layer == 5:
            oneChoice   = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            twoChoice   = [ (2,3), (4,5), (5,6), (7,8), (8,9), (9,10), (11,12), (12,13), (13,14), (14,15),
                            (1,2), (2,4), (4,7), (7,11), (3,5), (5,8), (8,12), (6,9), (9,13), (10,14),
                            (1,3), (3,6), (6,10), (10,15), (2,5), (5,9), (9,14), (4,8), (8,13), (7,12)]
            thrChoice   = [ (4,5,6), (7,8,9), (8,9,10), (11,12,13), (12,13,14), (13,14,15),
                            (6,9,13), (3,5,8), (5,8,12), (1,2,4), (2,4,7), (4,7,11),
                            (4,8,13), (2,5,9), (5,9,14), (1,3,6), (3,6,10), (6,10,15)]
    elif    layer == 6:
            oneChoice   = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
            twoChoice   = [ (2,3), (4,5), (5,6), (7,8), (8,9), (9,10), (11,12), (12,13), (13,14), (14,15), (16,17), (17,18), (18,19), (19,20), (20,21),
                            (1,2), (2,4), (4,7), (7,11), (11,16), (3,5), (5,8), (8,12), (12,17), (6,9), (9,13), (13,18), (10,14), (14,19), (15,20),
                            (1,3), (3,6), (6,10), (10,15), (15,21), (2,5), (5,9), (9,14), (14,20), (4,8), (8,13), (13,19), (7,12), (12,18), (11,17)]
            thrChoice   = [ (4,5,6), (7,8,9), (8,9,10), (11,12,13), (12,13,14), (13,14,15), (16,17,18), (17,18,19), (18,19,20), (19,20,21),
                            (10,14,19), (6,9,13), (9,13,18), (3,5,8), (5,8,12), (8,12,17), (1,2,4), (2,4,7), (4,7,11), (7,11,16),
                            (7,12,18), (4,8,13), (8,13,19), (2,5,9), (5,9,14), (9,14,20), (1,3,6), (3,6,10), (6,10,15), (10,15,21)]
    else:   print("Can not analyze lower than 3 layers and larger than 6 layers !")

    return [oneChoice, twoChoice, thrChoice]


################################
###   電腦決定要刪除的圈圈     ###
################################
def computerRound(choiceListNow):

    # 決定刪除圈圈個數
    if      len(choiceListNow[0]) != 0 and len(choiceListNow[1]) != 0 and len(choiceListNow[2]) != 0    : deleteNum = random.randrange(1,4) 
    elif    len(choiceListNow[0]) != 0 and len(choiceListNow[1]) != 0                                   : deleteNum = random.randrange(1,3)
    else                                                                                                : deleteNum = 1
    
    # 決定刪除圈圈號碼
    if      deleteNum == 1  : readyToDeleteSet  = choice(choiceListNow[0])
    elif    deleteNum == 2  : readyToDeleteSet  = choice(choiceListNow[1])
    elif    deleteNum == 3  : readyToDeleteSet  = choice(choiceListNow[2])

    return deleteNum, readyToDeleteSet


################################
###   人類決定要刪除的圈圈     ###
################################
def humanRound(choiceListNow):
    
    delete_str              = input("請決定刪除個數:")
    deleteNum               = int(delete_str)
    
    if deleteNum == 1:
        readyToDelete_str   = input("請決定刪除圈圈:")
        readyToDeleteSet    = int(readyToDelete_str)
    else:
        readyToDelete_str   = input("請決定刪除圈圈:")
        readyToDeleteSet    = tuple(map(int, readyToDelete_str.split(',')))

    return deleteNum, readyToDeleteSet


################################
###   抽出被刪除圈圈的號碼     ###
################################
def choiceExtract(deleteNum, readyToDeleteSet, choiceListNow):

    oneChoiceNow    = choiceListNow[0]
    twoChoiceNow    = choiceListNow[1]
    thrChoiceNow    = choiceListNow[2]
    diffCircleSet   = []

    for i in range(0,deleteNum):
        if deleteNum > 1   : readyToDelete = readyToDeleteSet[i]
        else               : readyToDelete = readyToDeleteSet
        
        # 整理oneChoiceNow
        for j in range(0,len(oneChoiceNow)):
            if oneChoiceNow[j] == readyToDelete:
                diffCircleSet.append(oneChoiceNow[j])
        oneChoiceNow    = list(set(oneChoiceNow) - set(diffCircleSet))
        diffCircleSet   = []
        
        # 整理twoChoiceNow
        for j in range(0,len(twoChoiceNow)):
            for k in range(0,2):
                if twoChoiceNow[j][k] == readyToDelete:
                    diffCircleSet.append(twoChoiceNow[j])
                    break
        twoChoiceNow    = list(set(twoChoiceNow) - set(diffCircleSet))
        diffCircleSet   = []
        
        # 整理thrChoiceNow
        for j in range(0,len(thrChoiceNow)):
            for k in range(0,3):
                if thrChoiceNow[j][k] == readyToDelete:
                    diffCircleSet.append(thrChoiceNow[j])
                    break
        thrChoiceNow    = list(set(thrChoiceNow) - set(diffCircleSet))
        diffCircleSet   = []

    return [oneChoiceNow, twoChoiceNow, thrChoiceNow]


################################
###   電腦 VS 電腦 (一回)     ###
################################
def com_vs_com(layer):

    totalCircle     = 0                 # 圈圈總數
    deleteNum       = 0                 # 當次回合要刪除的圈圈個數
    deleteTotal     = 0                 # 目前總共刪除的個數
    deleteOrder     = []                # 用來儲存刪除的過程
    choiceListNow   = genChoice(layer)  # 產生可以刪除的各種可能

    # 計算圈圈總數
    for i in range(1, layer+1): totalCircle += i

    # 開始遊戲(電腦自行對弈)
    while deleteTotal < totalCircle:

        # 電腦決定刪除圈圈號碼
        deleteNum, readyToDeleteSet = computerRound(choiceListNow)

        # 將要刪除的圈圈記錄下來
        deleteOrder.append(readyToDeleteSet)

        # 抽出刪除圈圈的號碼
        choiceListNow = choiceExtract(deleteNum, readyToDeleteSet, choiceListNow)

        # 計算目前刪除的圈圈數
        deleteTotal += deleteNum

        # 刪完圈圈後停止
        if deleteTotal == totalCircle: break

    return deleteOrder


################################
###       產生勝利棋譜        ###
################################
def genVicChess(vicChessNum, layer):

    vicChessNow     = 0     # 目前儲存的勝利棋譜數量
    vicChessList    = []    # 勝利棋譜大集合

    while vicChessNow < vicChessNum:
        
        # 執行一回合遊戲
        deleteOrder = com_vs_com(layer)
        
        # 儲存勝利棋譜至vicChessList
        if len(deleteOrder) % 2 == 0: 
            vicChessList.append(deleteOrder)
            vicChessNow += 1
        
            # 進度顯示
            if vicChessNow % (vicChessNum / 10) == 0:
                print("genVicChess progress: " + str(100.0 * vicChessNow/vicChessNum) + " %")

        if vicChessNow == vicChessNum: break

    return vicChessList


################################
###        抽出勝利棋譜       ###
################################
def vicChessExtract(vicChessList, deleteOrder):
    
    vicChessListNew = []

    for i in range(0, len(vicChessList)):
        for j in range(len(deleteOrder)-1, len(deleteOrder)): # 只檢查deleteOrder最後一個
            
            if type(vicChessList[i][j]) is int and type(deleteOrder[j]) is int and vicChessList[i][j] == deleteOrder[j]:
                vicChessListNew.append(vicChessList[i])
            
            elif type(vicChessList[i][j]) is tuple and type(deleteOrder[j]) is tuple and vicChessList[i][j] == deleteOrder[j]:
                vicChessListNew.append(vicChessList[i])
    
    return vicChessListNew


################################
###       產生失敗棋譜        ###
################################
def genFailChess(failChessNum, layer):

    failChessNow     = 0     # 目前儲存的失敗棋譜數量
    failChessList    = []    # 失敗棋譜大集合

    while failChessNow < failChessNum:
        
        # 執行一回合遊戲
        deleteOrder = com_vs_com(layer)
        
        # 儲存失敗棋譜至failChessList
        if len(deleteOrder) % 2 == 1: 
            failChessList.append(deleteOrder)
            failChessNow += 1

            # 進度顯示
            if failChessNow % (failChessNum / 10) == 0:
                print("genFailChess progress: " + str(100.0 * failChessNow/failChessNum) + " %")
        
        if failChessNow == failChessNum: break

    return failChessList


################################
###        抽出失敗棋譜       ###
################################
def failChessExtract(failChessList, deleteOrder):
    
    failChessListNew = []

    for i in range(0, len(failChessList)):
        for j in range(len(deleteOrder)-1, len(deleteOrder)): # 只檢查deleteOrder最後一個
            
            if type(failChessList[i][j]) is int and type(deleteOrder[j]) is int and failChessList[i][j] == deleteOrder[j]:
                failChessListNew.append(failChessList[i])
            
            elif type(failChessList[i][j]) is tuple and type(deleteOrder[j]) is tuple and failChessList[i][j] == deleteOrder[j]:
                failChessListNew.append(failChessList[i])
    
    return failChessListNew


################################
###  策略1: 根據勝利棋譜刪除   ###
################################
def strategy_vicChess(vicChessList, deleteOrder):
    
    vicChessUsedNum     = random.randrange(0,len(vicChessList))
    readyToDeleteSet    = vicChessList[vicChessUsedNum][len(deleteOrder)]

    if type(readyToDeleteSet) is int    : deleteNum = 1
    else                                : deleteNum = len(readyToDeleteSet)

    return deleteNum, readyToDeleteSet


################################
###  策略2: 根據失敗棋譜刪除   ###
################################
def strategy_failChess(failChessList, deleteOrder, choiceListNow):

    failChoiceList      = [[],[],[]]    # 用來儲存失敗棋譜的選擇
    choiceList_temp     = [[],[],[]]    # 刪除失敗棋譜的選擇後所剩的選擇
    
    # 挑選出失敗棋譜的選擇
    for i in range(0, len(failChessList)):
        if type(failChessList[i][len(deleteOrder)]) is int:
            failChoiceList[0].append(failChessList[i][len(deleteOrder)])
        elif type(failChessList[i][len(deleteOrder)]) is tuple and len(failChessList[i][len(deleteOrder)]) == 2:
            failChoiceList[1].append(failChessList[i][len(deleteOrder)])
        elif type(failChessList[i][len(deleteOrder)]) is tuple and len(failChessList[i][len(deleteOrder)]) == 3:
            failChoiceList[2].append(failChessList[i][len(deleteOrder)])
    
    # 把會失敗的選擇刪除
    choiceList_temp[0] = list(set(choiceListNow[0]) - set(failChoiceList[0]))
    choiceList_temp[1] = list(set(choiceListNow[1]) - set(failChoiceList[1]))
    choiceList_temp[2] = list(set(choiceListNow[2]) - set(failChoiceList[2]))
    
    # 電腦避開失敗棋譜，如果沒有一個圈圈的選擇可以刪除，則隨機刪除
    if len(choiceList_temp[0]) != 0 : deleteNum, readyToDeleteSet = computerRound(choiceList_temp)
    else                            : deleteNum, readyToDeleteSet = computerRound(choiceListNow)

    return deleteNum, readyToDeleteSet


################################
###  策略3: 奇數原則          ###
################################
def strategy_oddNumber(deleteOrder, choiceListNow, totalCircle):

    deleteNumNow = 0  # 目前已刪除的圈圈個數

    # 先計算目前已刪除的圈圈個數
    for i in range(0, len(deleteOrder)):
        if type(deleteOrder[i]) is int  : deleteNumNow += 1
        else                            : deleteNumNow += len(deleteOrder[i])
    
    # 若剩下的圈圈有奇數個，則刪除偶數個圈圈(即刪除2個)
    if (totalCircle - deleteNumNow) % 2 == 1:
        if len(choiceListNow[1]) != 0:
            deleteNum = 2
            readyToDeleteSet = choice(choiceListNow[1])
        else:
            deleteNum, readyToDeleteSet = computerRound(choiceListNow)
    
    # 若剩下的圈圈有偶數個，則刪除奇數個圈圈(即刪除1或3個)
    else:
        if len(choiceListNow[0]) != 0 and len(choiceListNow[2]) != 0:
            
            # 決定要刪除1個圈圈還是3個圈圈
            if random.randrange(1,3) == 1: # 選到1就消1個圈圈,選到2就消3個圈圈
                deleteNum = 1
                readyToDeleteSet = choice(choiceListNow[0])
            else:
                deleteNum = 3
                readyToDeleteSet = choice(choiceListNow[2])
        else:
            deleteNum, readyToDeleteSet = computerRound(choiceListNow)

    return deleteNum, readyToDeleteSet


################################
###  演算法1: 策略1           ###
################################
def algo1_Round(choiceListNow, vicChessList, deleteOrder):

    # 若有勝利棋譜則參考勝利棋譜刪除(策略1)
    if len(vicChessList) != 0:
        deleteNum, readyToDeleteSet = strategy_vicChess(vicChessList, deleteOrder)
    
    # 沒有勝利棋譜可以參考則隨機刪除
    else:
        deleteNum, readyToDeleteSet = computerRound(choiceListNow)

    return deleteNum, readyToDeleteSet


################################
### 演算法2: 策略1 + 2        ###
################################
def algo2_Round(choiceListNow, vicChessList, failChessList, deleteOrder):

    # 若有勝利棋譜則參考勝利棋譜刪除(策略1)
    if len(vicChessList) != 0:
        deleteNum, readyToDeleteSet = strategy_vicChess(vicChessList, deleteOrder)
    
    # 若沒有勝利棋譜，則參考失敗棋譜(策略2)
    elif len(vicChessList) == 0 and len(failChessList) != 0:
        deleteNum, readyToDeleteSet = strategy_failChess(failChessList, deleteOrder, choiceListNow)
    
    # 沒有勝利以及失敗棋譜可以參考
    else:
        deleteNum, readyToDeleteSet = computerRound(choiceListNow)

    return deleteNum, readyToDeleteSet


################################
### 演算法3: 策略1 + 2 + 3    ###
################################
def algo3_Round(choiceListNow, vicChessList, failChessList, deleteOrder, totalCircle):

    # 若有勝利棋譜則參考勝利棋譜刪除(策略1)
    if len(vicChessList) != 0:
        deleteNum, readyToDeleteSet = strategy_vicChess(vicChessList, deleteOrder)
    
    # 若沒有勝利棋譜，則參考失敗棋譜(策略2)
    elif len(vicChessList) == 0 and len(failChessList) != 0:
        deleteNum, readyToDeleteSet = strategy_failChess(failChessList, deleteOrder, choiceListNow)
    
    # 若沒有勝利棋譜、失敗棋譜可以參考，則遵循奇數原則(策略3)
    else:
        deleteNum, readyToDeleteSet = strategy_oddNumber(deleteOrder, choiceListNow, totalCircle)

    return deleteNum, readyToDeleteSet