#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("fish.txt", 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0

  for line in textFile:
    lineCount += 1
    words = line.split()
    for w in words:
      wordCount += 1
      letterCount += len(w)

  print("Lines:", lineCount)
  print("Words:", wordCount)
  print("Letter:", letterCount)
  

if __name__ == '__main__':
  main()
