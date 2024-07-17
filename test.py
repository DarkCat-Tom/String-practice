import re

def stringPractice(intputString):
  numberString = re.sub('[a-zA-Z]','',intputString)
  indexof = numberString.find('.')
  length = len(numberString)
  if indexof == -1 :
    return numberString + ".00"
  elif len(numberString[indexof:length]) == 1 :
    return numberString + "00"
  elif len(numberString[indexof:length]) == 2 :
    return numberString + "0"
  else :
    return numberString[:indexof+3]


if __name__ == "__main__":
  print(stringPractice('abcd'))
  print(stringPractice('abcd123'))
  print(stringPractice('abcd123.'))
  print(stringPractice('abcd123.4'))
  print(stringPractice('abcd123.45'))
  print(stringPractice('abcd123.456'))
  print(stringPractice('abcd123.4567'))