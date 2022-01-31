import game_fuctions

# 相關變數(可以調整)
layer           = 5                                 # 2 < layer < 7
vicChessNum     = 10000                             # 參考的勝利棋譜數量

# 相關變數(不要調整)
vicChessList    = []                                # 勝利棋譜
totalCircle     = 0                                 # 圈圈總數
deleteNum       = 0                                 # 當次回合要刪除的圈圈個數
deleteTotal     = 0                                 # 目前總共刪除的個數
deleteOrder     = []                                # 用來儲存刪除的過程
choiceListNow   = game_fuctions.genChoice(layer)    # 產生可以刪除的各種可能

# 計算圈圈總數
for i in range(1, layer+1): totalCircle += i

# 產生勝利棋譜(需要較長的時間)
vicChessList    = game_fuctions.genVicChess(vicChessNum, layer)

# 開始遊戲(電腦人類對弈)
for i in range(0, totalCircle):
    
    # 電腦決定刪除圈圈號碼
    if  i % 2 == 0  :  deleteNum, readyToDeleteSet  = game_fuctions.algo1_Round(choiceListNow, vicChessList, deleteOrder)
    else            :  deleteNum, readyToDeleteSet  = game_fuctions.humanRound(choiceListNow)
    
    # 將要刪除的圈圈記錄下來
    deleteOrder.append(readyToDeleteSet)
    print("目前刪除的圈圈: " + str(deleteOrder))
    
    # 抽出勝利棋譜
    vicChessList = game_fuctions.vicChessExtract(vicChessList, deleteOrder)
    
    # 抽出刪除圈圈的號碼
    choiceListNow = game_fuctions.choiceExtract(deleteNum, readyToDeleteSet, choiceListNow)
    
    # 計算目前刪除的圈圈數
    deleteTotal += deleteNum
    
    # 刪完15個圈圈後停止
    if deleteTotal == totalCircle: break

print(deleteOrder)
if len(deleteOrder) % 2 == 0    : print("電腦獲勝")
else                            : print("人類獲勝")