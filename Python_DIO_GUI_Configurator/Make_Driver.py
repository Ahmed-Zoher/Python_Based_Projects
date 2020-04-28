import os,sys


def main():
  Dname = input(print("Enter the Name of the Driver: \n"))
  Extension = ['program.c','register.h','private.h','inteface.h','config.h']
  Name=Dname+'_Driver' 
  os.mkdir(Name)
  os.chdir(Name)
  for i in range (0,len(Extension)):
    f=open(Extension[i],'a')
    if Extension[i][-1]=='h':
      f.write('#ifndef "'+ Extension[i]+'"')
      f.write('\n#define "'+Extension[i]+'"')
      f.write('\n#endif')
    elif Extension[i][-1]=='c':
      for i in range (1,len(Extension)):
        f.write('#include "'+Extension[i]+'"\n')
    f.close()

if __name__ == '__main__':
  main()
  