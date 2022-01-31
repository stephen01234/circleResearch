import game_fuctions

# 相關變數(可以調整)
layer           = 3         # 2 < layer < 7
gameNum         = 1000      # 遊戲次數
vicChessNum     = 100000      # 參考的勝利棋譜數量
failChessNum    = 100000      # 參考的失敗棋譜數量

# 相關變數(不要調整)
vicNum          = 0         # AI獲勝次數
vicChessList    = []        # 勝利棋譜
failChessList   = []        # 失敗棋譜
totalCircle     = 0         # 圈圈總數
continue_flag   = 1         # 1:繼續; 其它數字:不繼續

# 計算圈圈總數
for i in range(1, layer+1): totalCircle += i

# 產生勝利及失敗棋譜(需要較長的時間)
vicChessList    = game_fuctions.genVicChess(vicChessNum, layer)
failChessList   = game_fuctions.genFailChess(failChessNum, layer)

# while continue_flag == 1:
for i_test in range(0,3):

    for i_game in range(0, gameNum):
    
        # 變數更新
        deleteNum           = 0                                 # 當次回合要刪除的圈圈個數
        deleteTotal         = 0                                 # 目前總共刪除的個數
        deleteOrder         = []                                # 用來儲存刪除的過程
        choiceListNow       = game_fuctions.genChoice(layer)    # 產生可以刪除的各種可能
        vicChessList_temp   = vicChessList.copy()
        failChessList_temp  = failChessList.copy()

        # 進度顯示
        if i_game % (gameNum / 10) == 0: 
            print("algorithm2_vs_com: " + str(100.0 * i_game/gameNum) + " %")

        # 開始遊戲(電腦自行對弈)
        for i in range(0, totalCircle):

            # 電腦決定刪除圈圈號碼
            if  i % 2 == 0 :  
                deleteNum, readyToDeleteSet  = game_fuctions.algo2_Round(choiceListNow, vicChessList_temp, failChessList_temp, deleteOrder)
            else:  
                deleteNum, readyToDeleteSet  = game_fuctions.computerRound(choiceListNow)

            # 將要刪除的圈圈記錄下來
            deleteOrder.append(readyToDeleteSet)

            # 抽出勝利棋譜
            vicChessList_temp = game_fuctions.vicChessExtract(vicChessList_temp, deleteOrder)

            # 抽出失敗棋譜
            failChessList_temp = game_fuctions.failChessExtract(failChessList_temp, deleteOrder)

            # 抽出刪除圈圈的號碼
            choiceListNow = game_fuctions.choiceExtract(deleteNum, readyToDeleteSet, choiceListNow)

            # 計算目前刪除的圈圈數
            deleteTotal += deleteNum

            # 刪完15個圈圈後停止
            if deleteTotal == totalCircle: break

        if len(deleteOrder) % 2 == 0: vicNum += 1

    print("AI獲勝次數: " + str(vicNum))
    print("AI獲勝勝率: " + str(float(vicNum)/gameNum))

    vicNum          = 0
    # continue_str    = input("是否再分析一次(繼續:1;跳出:2):")
    # continue_flag   = int(continue_str)