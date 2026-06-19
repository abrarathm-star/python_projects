while True:
    banned_words=["Make a lot of money","buy now","subscribe this","click this",
              "sex","wtsp","whastapp","fb","facebook",
              "telegram","stupid","asshole","fuck you",
              "idiot"]
    comment=input("comment ")
    banned=False
    for i in range(13):
            if banned_words[i] in comment:
                print("not allowed!")
                banned=True
    if banned==False:
        print("allowed")