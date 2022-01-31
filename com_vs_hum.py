import game_fuctions

# 設定圈圈有幾層 (2 < layer < 7)
layer           = 5

# 相關變數(不要調整)
totalCircle     = 0                                 # 圈圈總數
deleteNum       = 0                                 # 當次回合要刪除的圈圈個數
deleteTotal     = 0                                 # 目前總共刪除的個數
deleteOrder     = []                                # 用來儲存刪除的過程
choiceListNow   = game_fuctions.genChoice(layer)    # 產生可以刪除的各種可能

# 計算圈圈總數
for i in range(1, layer+1): totalCircle += i

# 開始遊戲(電腦人類對弈)
for i in range(0, totalCircle):
    
    # 電腦決定刪除圈圈號碼
    if  i % 2 == 0  :  deleteNum, readyToDeleteSet = game_fuctions.computerRound(choiceListNow)
    else            :  deleteNum, readyToDeleteSet = game_fuctions.humanRound(choiceListNow)
    
    # 將要刪除的圈圈記錄下來
    deleteOrder.append(readyToDeleteSet)
    print("目前刪除的圈圈: " + str(deleteOrder))
    
    # 抽出刪除圈圈的號碼
    choiceListNow = game_fuctions.choiceExtract(deleteNum, readyToDeleteSet, choiceListNow)
    
    # 計算目前刪除的圈圈數
    deleteTotal += deleteNum
    
    # 刪完15個圈圈後停止
    if deleteTotal == totalCircle: break

print(deleteOrder)
if len(deleteOrder) % 2 == 0    : print("電腦獲勝")
else                            : print("人類獲勝")