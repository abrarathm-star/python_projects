for n in range(2,21):
    with open(f"table of {n}.txt","w") as w:
        for i in range (1,11):
            w.write(f"{n} x {i} = {n*i}\n")