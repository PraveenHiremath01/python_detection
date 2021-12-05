# importing package
from better_profanity import profanity
file = open("F:\All web\Chapter4\pythgon\words.txt", "rt")
data = file.read()
words = data.split()
length = len(words)
#print(length)
count=0

#check=False
#for i in range(length):
count=0
no=0
#check=False
for i in range(length): 
 check = profanity.contains_profanity(words[i])
 #print(words[i])
 if check==True:
  count = count + 1
 elif check == False:
  no=no+1
print(" There are ", count, " numbers of profanity(bad) words in the given file")
print("and rest of",no, "are normal words" )

    





 