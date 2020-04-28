"""
CONTENTS:

1)Bubble Sort Algorithm
2)Selection Sort Algorithm

"""

def  my_bubble_sort(b):
  for n in range(0,len(b)-1):
    for a in range (1,len(b)-n):
      if b[a-1]>b[a]:
        temp = b[a]
        b[a]=b[a-1]
        b[a-1]=temp

def  my_selection_sort(b):
  for n in range(1,len(b)):
    for a in range (n,0,-1):
      if b[a-1]>b[a]:
        temp = b[a]
        b[a]=b[a-1]
        b[a-1]=temp


def main():
  a=[9,1,0,2,1,4,-5]
  my_bubble_sort(a);
  print(a);
  b=['z','c','b','o','t','w','y']
  my_selection_sort(b);
  print(b);

if __name__ == "__main__":
  main()