import game_fuctions

################################
###   電腦 VS 人類            ###
################################
# 相關變數(可以調整)
layer       = 5             # 2 < layer < 7 ,除非genChoice()中有建置7層以上的刪除選擇
gameNum     = 1000         # 遊戲次數

# 相關變數(不要調整)
vicNum      = 0             # 儲存電腦獲勝次數

# 只進行一個回合
if gameNum == 1:

    deleteOrder = game_fuctions.com_vs_com(layer)
    
    print(deleteOrder)
    if len(deleteOrder) % 2 == 0    : print("先手獲勝")
    else                            : print("後手獲勝")

# 要進行多個回合
else:
    for i_game in range(0, gameNum):

        # 進度顯示
        if i_game % (gameNum / 10) == 0: 
            print("com_vs_com: " + str(100.0 * i_game/gameNum) + " %")

        deleteOrder = game_fuctions.com_vs_com(layer)

        if len(deleteOrder) % 2 == 0 : vicNum += 1

    print("先手獲勝次數: " + str(vicNum))
    print("先手獲勝勝率: " + str(float(vicNum)/gameNum))