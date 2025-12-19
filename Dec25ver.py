import os
while True:
    id = input("Paste ID list or type \"exit\" to end")
    if id=="exit":
        break
    else:
        id = id.strip().split()

    print(id)
    imgs = os.listdir()
    print(imgs)
