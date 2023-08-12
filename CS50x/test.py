
Number_text = ['', 'one', 'two', 'three', 'four',
           'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'therthen', 'fourteen',
                      'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
list10 = ['twenty', 'therty', 'fourty', 'fifty',
           'sixty', 'seventy', 'eighty', 'ninety']
hugeamount = ['hundered','', 'thousend', 'million', 'billion' ,' trillion ' ,' quadrillion ' ,' quintillion ' ,' sextillion ' ,' septillion ' ,' octillion ' ,' nonillion ' ,' decillion ' ,' undecillion ' ,' duodecillion ' ,' tredecillion ' ,' quattuordecillion ' ,' quindecillion ' ,' sexdecillion ' ,' septendecillion ' ,' octodecillion ' ,' novemdecillion ' ,' vigintillion ' ,' unvigintillion ' ,' duovigintillion ' ,' trevigintillion ' ,' quattuorvigintillion ' ,' quinvigintillion ' ,' sexvigintillion ' ,' septenvigintillion ' ,' octovigintillion ' ,' novemvigintillion ' ,' trigintillion ' ,' untrigintillion ' ,' duotrigintillion ' ,' tretrigintillion ' ,' quattuortrigintillion ' ,' quintrigintillion ' ,' sextrigintillion ' ,' septentrigintillion ' ,' octotrigintillion ' ,' novemtrigintillion ' ,' quadragintillion ' ,' unquadragintillion ' ,' duoquadragintillion ' ,' trequadragintillion ' ,' quattuorquadragintillion ' ,' quinquadragintillion ' ,' sexquadragintillion ' ,' septenquadragintillion ' ,' octoquadragintillion ' ,' novemquadragintillion ' ,' quinquagintillion ' ,' unquinquagintillion ' ,' duoquinquagintillion ' ,' trequinquagintillion ' ,' quattuorquinquagintillion ' ,' quinquinquagintillion ' ,' sexquinquagintillion ' ,' septenquinquagintillion ' ,' octoquinquagintillion ' ,' novemquinquagintillion ' ,' sexagintillion ' ,' unsexagintillion ' ,' duosexagintillion ' ,' tresexagintillion ' ,' quattuorsexagintillion ' ,' quinsexagintillion ' ,' sexsexagintillion ' ,' septensexagintillion ' ,' octosexagintillion ' ,' novemsexagintillion ' ,' septuagintillion ' ,' unseptuagintillion ' ,' duoseptuagintillion ' ,' treseptuagintillion ' ,' quattuorseptuagintillion ' ,' quinseptuagintillion ' ,' sexseptuagintillion ' ,' septenseptuagintillion ' ,' octoseptuagintillion ' ,' novemseptuagintillion ' ,' octogintillion ' ,' unoctogintillion ' ,' duooctogintillion ' ,' treoctogintillion ' ,' quattuoroctogintillion ' ,' quinoctogintillion ' ,' sexoctogintillion ' ,' septenoctogintillion ' ,' octooctogintillion ' ,' novemoctogintillion ' ,' nonagintillion ' ,' unnonagintillion ' ,' duononagintillion ' ,' trenonagintillion ' ,' quattuornonagintillion ' ,' quinnonagintillion ' ,' sexnonagintillion ' ,' septennonagintillion ' ,' octononagintillion ' ,' novemnonagintillion ' ,' centillion ']# Complete more items !

while 
i = int(input("Please enter a number: "))



def numtotext100(Number_text, list10, hugeamount, i):
    out = None

    number_list = list(str(i))
    size = len(number_list)  # count members

    if(size == 1):
        if i == 0:
            pass
        else:
            out = Number_text[i]

    elif(size == 2):
        ab = int(number_list[-2]+number_list[-1])
        if ab >= 10 and ab < 20:
            out = Number_text[ab]
        else:
            out = list10[int(number_list[-2])-2]+" "+Number_text[int(number_list[-1])]

    elif(size == 3):
        out = Number_text[int(number_list[-3])]+" "+hugeamount[0]+" "
        bc = int(number_list[-2]+number_list[-1])
        if bc < 20:
            out += Number_text[bc]
        else:
            out += list10[int(number_list[-2])-2]+" "+Number_text[int(number_list[-1])]
    if out==None:
        out=""
    return out


string_num=str(i)
list_num=[]
s=''
reversednum=[number for number in string_num]
reversednum.reverse()

string_num=''
for w in reversednum:
    string_num+=w

for n in string_num:
    if len(s)<3:
        s+=n
    else:
        list_num.insert(0,s)
        s=''
        s+=n

list_num.insert(0,s)
newlist=[]
for item in list_num:
    k=[d for d in item]
    k.reverse()
    text=''
    for items in k:
        text+=items
    newlist.append(text)
list_num=newlist

list_num=[int(n) for n in list_num]

out=""
if len(list_num)==1:
    out=numtotext100(Number_text, list10, hugeamount, list_num[0])
else:
    n=1
    s=len(list_num)
    while n<=len(list_num):

        if numtotext100(Number_text, list10, hugeamount, list_num[n-1])!="":
            out+=numtotext100(Number_text, list10, hugeamount, list_num[n-1])+" "+hugeamount[s]+" "
        n=n+1
        s=s-1

if(out==""):
    out='Zero'
print(f'The number is : {out}')
input()