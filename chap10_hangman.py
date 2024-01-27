def hangman(word):
    wrong = 0
    stages = ["",
              "_________        ",
              "|                ",
              "|        |       ",
              "|        O       ",
              "|       /|\      ",
              "|       / \      ",
              "|                "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンにようこそ！")

    """
    hangman(word)のwordという引数は当ててほしい言葉を入れる引数
    wrong はプレイヤーが何回間違えたかをカウントする変数、初期値は０に設定している
    変数stages は文字列のリストを使って、吊られている人の絵を表現している。この８つの要素が全て出力されたらプレイヤーの負け
    変数rletters は答えの言葉を、一つ一つの要素にリストにしたもの。
    変数boardは文字列のリストで、プレイヤーに見せるヒントに使う、例えば答えの言葉が"cat"でプレイヤーが"c"と"t"を当てたら、"c_t"と表現する為に使う。
    その式の["_"] * len(word)は答えの言葉が"cat"なら初期の表示は,["_","_","_"]になる。
    変数win はこのゲームの勝敗を記録する場所。初期状態はFalseに設定
    そして最後に "ハングマンにようこそと表示する"
    """

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))

hangman("cat")