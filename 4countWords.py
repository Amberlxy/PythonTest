# coding = utf-8
from collections import Counter
import string

def getText():
    filepath = '/Users/amber/Desktop/Adjust.txt'
    try:
        f = open(filepath)
        filetext = f.read()
        return filetext
    except:
        print("文件错误，请检查")

def textWords():
    example = string.ascii_letters + string.whitespace + "[^\']" + "[\-]"
    text = getText()
    # text = "Deeplinks improve user experience by taking users directly to in-app content. Use them throughout your marketing funnel to improve user acquisition, engagement, anded. "
    for i in range(0,len(text)):
        if text[i] not in example:
            text = text.replace(text[i],' ')
        else:
            continue
    str1 = text.strip(' ').split(' ')
    mytest = [i for i in str1 if i != '']
    return mytest

def countWords():
    d2 = Counter(textWords())
    sorted_x = sorted(d2.items(), key=lambda x: x[1], reverse=True)
    print("该文本中各单词出现次数统计如下：")
    for j in range(0,len(sorted_x)):
        key = sorted_x[j][0]
        print(sorted_x[j][0] + ' : ' + str(sorted_x[j][1]))

if __name__ == "__main__":
    countWords()