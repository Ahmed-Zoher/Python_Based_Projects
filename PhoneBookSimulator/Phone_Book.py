import os


def calc():
  print("Welcome to Contact Manager...\n")
  Selection1=0;
  while(True):
    if Selection1==0:
      print('-------------------------------------------')
      print('Please Select one of the following options:')
      print('-------------------------------------------\n')
      print("  1) Add Contact\n")
      print("  2) Remove Contact\n")
      print("  3) View Contact List\n")
      print("  4) Exit \n")
      Selection1 = input()
      print(Selection1)
    elif Selection1==1:
      os.system('cls')
    elif Selection1==2:
      None
    elif Selection1==3:
      None
    elif Selection1==4: 
      break
    else:
      None


def main():
  calc()

if __name__ == '__main__':
  main()  