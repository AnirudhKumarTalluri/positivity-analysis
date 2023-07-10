from textblob import TextBlob

while True:
    phase=input("enter the review: ")

    tb_phase=TextBlob(phase)

    tb_phase.correct()
    #print(tb_phase.sentiment)

    print(tb_phase.sentiment[0])

    if tb_phase.sentiment[0]<0.00000:
        print("negitive review")