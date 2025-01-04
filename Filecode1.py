def writefile():
  inputName = input("Please enter your name: ")
  inputAge = input("Please enter your age: ")
  inputAdress = input("Please enter your adress: ")
  inputEmail = input("Please input your email: ")

  filewrite = open("Biodata.txt", "w")
  filewrite.write("Name: " + inputName + "\nAge: " + inputAge + "\nAdress: " + inputAdress + "\nEmail: " + inputEmail)
  filewrite.close()

def readfile():
  fileread = open("Biodata.txt", "r")
  text= fileread.read()
  print("This is the data that was saved")
  print(text)
  fileread.close()

writefile()
print("\n")
readfile()
