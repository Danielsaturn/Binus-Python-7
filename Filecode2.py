def writefile():
    filename = input("Please enter the file name: ")
    inputName = input("Please enter your name: ")
    inputAge = input("Please enter your age: ")
    inputAdress = input("Please enter your adress: ")
    inputEmail = input("Please input your email: ")

    filewrite = open(filename +".txt", "w")
    filewrite.write("FileName: " + filename + "\nName: " + inputName + "\nAge: " + inputAge + "\nAdress: " + inputAdress + "\nEmail: " + inputEmail)
    filewrite.close()

def readfile():
    filename = input("Please enter the file name: ")
    fileread = open(filename + ".txt", "r")
    text= fileread.read()
    print("This is the data that was saved")
    print(text)
    fileread.close()

def addtext():
    filename = input("Please enter the file name: ")
    inputName = input("Please enter your name: ")
    inputAge = input("Please enter your age: ")
    inputAdress = input("Please enter your adress: ")
    inputEmail = input("Please input your email: ")

    filewrite = open(filename +".txt", "a")
    filewrite.write("FileName: " + filename + "\nName: " + inputName + "\nAge: " + inputAge + "\nAdress: " + inputAdress + "\nEmail: " + inputEmail)
    filewrite.close()


while(True):
  print("""===== OOP Program =====
    1. Membuat file
    2. Membaca file
    3. Menambah file
    4. Keluar Dari Program""")
  numbermenu = input("Please enter the number in accordance to what options that are available above: ")

  if (numbermenu == "1"):

    writefile()
    print("The file has been successfully saved")

  elif(numbermenu == "2"):
      print("\n")
      readfile()

  elif(numbermenu == "3"):

    addtext()
    print("The file has been successfully saved")

  elif(numbermenu == "4"):

    print("Thank you for using this program :-)")
    break

  else:
      print("Please enter the correct number!")
