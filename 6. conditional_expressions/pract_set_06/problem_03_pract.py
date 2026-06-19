# while True:
#     even = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40]
#     odd  = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41]

#     number=int(input("number: "))
#     e=False
#     o=False
#     for i in range(len(even)):
#         if even[i] ==number:
#             print("even number")
#             e=True
#         elif odd[i] ==number:
#             print("odd number")
#             o=True
    
#     if e==False and o==False:
#         print("neither even nor odd")

while True:
    number=int(input("number: "))
    if number%2==0:
        print("even")
    else:
        print("odd")

        """sortest best way"""