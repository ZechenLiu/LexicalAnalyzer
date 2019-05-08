import os
dict={'begin':1,'if':2,'then':3,'while':4,'do':5,'end':6,'ID':10,'NUM':11,'+':13,'-':14,'*':15,'/':16,':':17,':=':18,'<':20,
      '<>':21,'<=':22,'>':23,'>=':24,'=':25,';':26,'(':27,')':28,'#':0,'error':'error'}
#关键字
rwtab=["begin","if","then","while","do","end"]
#二元运算符
rwopt2=[':=','<>','<=','>=']
#无歧义的一元运算符
rwopt11= ['+','-','*','/','=',';','(',')','#']
#二元运算符左半边
rwopt12=['<','>',':']
#二元运算符右半边
rwopt13=['>','=']
#全部一元运算符
rwopt1=[':','=','+','-','*','/','<','>',';','(',')','#']
b=True
while b:
    print('请输入文件。换行输入"结束"代表文件输入完毕。')
    f=open('test.txt','w')
    while True:
          f_line = input()
          if f_line == '结束':
                break
          f.write(f_line+'\n')
    f.close()
    string=" "
    f=open('test.txt','r')
    ls=f.read()
    ls+=string
    token=''
    for i in ls:
          #出现换行符
          if i== '\n' or i=='\t' or i=='\t\n':
                i=" "
          #无歧义一元运算符
          if token in rwopt11:
                print('(' + str(dict[token]) + ',' + token + ')')
                token = ''
          # 二元运算符左半边
          elif token in rwopt12:
                #访问的元素是否为二元运算符右半边
                if i not in rwopt13:
                      print('(' + str(dict[token]) + ',' + token + ')')
                      token=''
          token += i
          # print(token)
          #二元运算符
          if token in rwopt2:
                print('(' + str(dict[token]) + ',' + token + ')')
                token = ''
          #结尾匹配到空格
          elif token[-1] == " ":
                token = token[:-1]
                token1=token+' '
                if (ord('z') >= ord(token1[0]) >= ord('a')) or (ord('A') <= ord(token1[0]) <= ord('Z')):
                    if token in rwtab:
                        print('(' + str(dict[token]) + ',', token + ')')
                        token=''
                    else:
                        token1 = token1[1:]
                        for i in token1:
                            if (ord('z') >= ord(i) >= ord('a')) or (ord('A') <= ord(i) <= ord('Z')) or i in '0123456789':
                                pass
                            elif i == ' ':
                                print('(' + str(dict['ID']) + ',', token + ')')
                            else:
                                print('(' + dict['error'] + ',' + token + ')')
                        token=''
                elif token1[0] in '0123456789':
                    token1 = token1[1:]
                    for i in token1:
                        if i in '0123456789':
                            pass
                        elif i == ' ':
                            print('(' + str(dict['NUM']) + ','+ token + ')')
                        else:
                            print('(' + dict['error'] + ','+ token + ')')
                            break
                    token=''
                else:
                    if token=='':
                        pass
                    else:
                        print('(' + dict['error'] + ',' + token + ')')
                    token=''
          #结尾匹配到标点符号
          elif token[-1] in rwopt1:
                token_operator=token[-1]
                token = token[:-1]
                token1=token+' '
                if (ord('z') >= ord(token1[0]) >= ord('a')) or (ord('A') <= ord(token1[0]) <= ord('Z')):
                    if token in rwtab:
                        print('(' + str(dict[token]) + ',', token + ')')
                        token=token_operator
                    else:
                        token1 = token1[1:]
                        for i in token1:
                            if (ord('z') >= ord(i) >= ord('a')) or (ord('A') <= ord(i) <= ord('Z')) or i in '0123456789':
                                pass
                            elif i == ' ':
                                print('(' + str(dict['ID']) + ',', token + ')')
                                token=token_operator
                            else:
                                print('(' + dict['error'] + ',' + token + ')')
                        token=token_operator
                elif token1[0] in '0123456789':
                    token1 = token1[1:]
                    for i in token1:
                        if i in '0123456789':
                            pass
                        elif i == ' ':
                            print('(' + str(dict['NUM']) + ',', token + ')')
                    token=token_operator
                else:
                    if token == '':
                        pass
                    else:
                        print('(' + dict['error'] + ',' + token + ')')
                    token=token_operator
          #结尾匹配到错误符号
          elif token[-1] not in rwopt1 and token[-1] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
                token_error=token[-1]
                token=token[:-1]
                token1=token+' '
                if (ord('z') >= ord(token1[0]) >= ord('a')) or (ord('A') <= ord(token1[0]) <= ord('Z')):
                    if token in rwtab:
                        print('(' + str(dict[token]) + ',', token + ')')
                        token=''
                    else:
                        token1 = token1[1:]
                        for i in token1:
                            if (ord('z') >= ord(i) >= ord('a')) or (ord('A') <= ord(i) <= ord('Z')) or i in '0123456789':
                                pass
                            elif i == ' ':
                                print('(' + str(dict['ID']) + ',', token + ')')
                            else:
                                print('(' + dict['error'] + ',' + token + ')')
                        token=''
                elif token1[0] in '0123456789':
                    token1 = token1[1:]
                    for i in token1:
                        if i in '0123456789':
                            pass
                        elif i == ' ':
                            print('(' + str(dict['NUM']) + ',', token + ')')
                    token=''
                else:
                    if token == '':
                        pass
                    else:
                        print('(' + dict['error'] + ',' + token + ')')
                    token=''
                print('('+dict['error']+','+token_error+')')
    while True:
        a = input("是否继续分析词法？(Y/N):")
        if a.upper() != 'Y' and a.upper() != 'N':
            print("输入错误！请重新输入。")
        elif a.upper() == 'Y':
            break
        else:
            b = False
            break
os.system('pause')
