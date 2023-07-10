from textblob import TextBlob



def sentiment(phase):
    positive=0
    negitive=0
    phase=phase.split('.')
    print(phase)

    for i in phase:
        tb_phase=TextBlob(i)

        tb_phase.correct()
        #print(tb_phase.sentiment)

        print(tb_phase.sentiment[0])

        if tb_phase.sentiment[0]<0.00000:
            print("negitive review")
            negitive+=1
            
        elif tb_phase.sentiment[0]>0.00000:
            print("good review")
            positive+=1

    if negitive>positive:
        return 0
    elif positive>=negitive:
        return 1
        