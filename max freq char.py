''' This is the simple program for getting maximum occurence of a number in a list '''

home='Maximum frequency number'
print(home.center(50))

#defining func for getting count of each character
def each_count(count_dict,words):
  for character in words:
    if character in count_dict:
        count_dict[character]+=1
    else:
        count_dict[character]=1
  return count_dict

#defining func for getting maximum frequency character from the given string
def max_freq_char(count_dict,max_count,max_char):
  for character,count in count_dict.items():
      if count>max_count:
          max_count=count
          max_char=character
  # print(count_dict)
  print('The maximum frequency charcter is', max_char,' with the frequency of',max_count)

#defining function for splitting the string
def split_string(str):
  words=[]
  for i in str:
      if i != ' ':
        words.append(i)
  return words
#defining variables    
count=0
max_count=0
max_char=' '
count_dict={}

#__main__
str=input('Enter the string:')
words=split_string(str)
 # print(words)
count_dict=each_count(count_dict,words)
 # print(count_dict)
max_freq_char(count_dict,max_count,max_char)

