# 文本分析与写作
from urllib.request import urlopen
from random import randint
def wordListSum(wordList):
    sum = 0
    for word,value in wordList.items():
        sum +=value
    return sum

def retrieveRandomWord(wordList):
    randIndex = randint(1,wordListSum(wordList))
    for word,value in wordList.items():
        randIndex -= value
        if randIndex < 0:
            return word
    return -1

def buildWordDict(text):
    #删除换行符和引号
    text = text.replace("\n"," ")
    text = text.replace('\"',"")
    text = text.replace("--",'')
    #保证每个标点符号都和前面的单词在一起
    #这样不会被剔除，保留在马尔科夫链中
    punctuation = [',','.',';',':']
    for symbol in punctuation:
        text = text.replace(symbol," "+symbol+" ")
    words = text.split(" ")
    #过滤空单词
    words = [word for word in words if word != ""]
    wordDict = {}
    for i in range(1,len(words)):
        if words[i-1] not in wordDict:
            #为单词新建一个字典
            wordDict[words[i-1]]={}
        if words[i] not in wordDict[words[i-1]]:
            wordDict[words[i-1]][words[i]] = 0  #这两句不是很能理解
        wordDict[words[i-1]][words[i]] = wordDict[words[i-1]][words[i]] + 1 
    return wordDict

text = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(),'utf-8')
# text = 'I am a good boy.I like banana.'
wordDict = buildWordDict(text)
#生成链长为１００的马尔科夫链
length = 10
chain = ""
currentWord = "like"
for i in range(0,length):
    chain += str(currentWord)
    print(wordDict[currentWord])
    currentWord = retrieveRandomWord(wordDict[currentWord])
    if currentWord == -1:
        break
    chain += ' '
print(chain)