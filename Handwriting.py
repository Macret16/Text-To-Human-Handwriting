from pywhatkit import text_to_handwriting as th

def tth():
    print()
    print("Hello Welcome To This Program!")
    print("-------------------------------")
    print("Write Here Or Copy And Paste Your Work Here To Convert It Into Handwriting!")
    print("-------------------------------")
    print("""Note : Write Your File Name Always Different Otherwise Your Same
File Will Overwrite The Data You Saved Previously.""")
    print("-------------------------------")
    write = input("Write Work Here : ")
    print("Your Data Written!")
    print("-------------------------------")
    print("""Note : Always Use Extension .png
File Name Example : example.png""")
    image = input("Write Your File Name : ")
    th(string=write, save_to=image, rgb=(0,0,139))
    print("Data Written Successfully!")


def menu():
    print("""1. Write Again
2. Save And Exit Program""")
    n = int(input("Enter Your Choice : "))
    if n==1:
        tth()
    elif n==2:
        print("\nThanks For Using This Program!\nMade by - Karan jaswani\n")
        print("Press Enter To Close Window.")
    else:
        print("Wrong Choice Try Again!")
        menu()

tth()
menu()