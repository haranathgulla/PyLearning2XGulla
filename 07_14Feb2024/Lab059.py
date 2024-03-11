# def make_pizza(*topings):
#     for toping in topings:
#         print(toping,end=" ")
#
# pramod = make_pizza("mushroom","onion","tomato")
# santosh = make_pizza("mushroom","Pineapple","Paneer")
# hari = make_pizza("kiwi","apple","tomato")
#
def make_pizza_base(*topings,base):
    print(topings,base)
    for toping in topings:
        print(toping)

amit = make_pizza_base("kiwi","onion","tomato",base="thin")
