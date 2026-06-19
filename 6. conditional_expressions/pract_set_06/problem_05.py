while True:
    family=["abrar", "ashir", "stefan", "jason", 
           "walter", "ahmed", "urooj", "shabana",
           "sadia", "rashida", "saira", "ali",
           "nasir", "zaid", "zarrar", "junaid",
           "afia", "anusha", "hayyan", "aisha"]
    name=input("enter name: ")
    n=False
    for i in range(len(family)):
        if family[i] in name:
            print("present")
            n=True
    if n==False:
        print("not found")