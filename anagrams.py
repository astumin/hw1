#import
import requests
import itertools

diclist=[]
ScoreDic={"j":3,"k":3,"q":3,"x":3,"z":3,"c":2,"f":2,"h":2,"l":2,"m":2,"p":2,"v":2,"w":2,"y":2,"a":1,"b":1,"d":1,"e":1,"g":1,"i":1,"n":1,"o":1,"r":1,"s":1,"t":1,"u":1}
dicsurl = 'http://icanhazwordz.appspot.com/dictionary.words'
anag_dics={}
myset=set()
#辞書を受け取る(list type)

def ReadDics(url):
    try:
        r = requests.get(url)
        diclist = sorted(r.text.split())
        for k in diclist:
            myset.add("".join(sorted(k.lower())))
            anag_dics["".join(sorted(k.lower()))] = k

        
    except requests.exceptions.RequestException as err:
        print(err)


def Matching(wordL):
    answer = set(wordL) & myset
    if answer != set() :
        maxscore=0
        print("------answer------")
        for l in answer:
            val = anag_dics[l]
            print(val)
            score = 1
            for n in val:
                score += ScoreDic[n.lower()]
            if maxscore < score:
                maxscore = score
                maxanswer = val
            print(score*score)
        print("MAX!!!!!!!!!!")
        print(maxanswer,maxscore)
        return 1


def Combi(word ,num):
    combiwordlist=[]
    for i in list(itertools.combinations(word, len(word)-num)):
        combiwordlist.append("".join(i))
    return combiwordlist

#main
#辞書を開く
ReadDics(dicsurl)
#print(myset)       #辞書が開いているか確認

while(1):
    #標準入力から単語を受け取る
    print("--INPUT--")
    str=input()
    if str == "QQQ":
        break
    str = str.lower()
    #入力値をソートする
    #print(sorted(str))
    sortword = "".join(sorted(str))

    for j in range(len(sortword)):
        #print(Combi(sortword,j))
        if Matching(Combi(sortword,j))==1:
            break



#終了
print("FINISH")