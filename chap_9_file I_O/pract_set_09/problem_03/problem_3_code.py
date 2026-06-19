
for n in range(2,21):
    w=open(f"table of {n}.txt","w")
    # print(f"table of {n}")
    print()
    for i in range(1,11):
        new_table=f"{n} x {i} ={n*i}\n"
        w.write(new_table)
    w.close()