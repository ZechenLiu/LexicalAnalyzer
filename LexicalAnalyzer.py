import re
import os
patternID=re.compile(r'(^[a-zA-Z])(([a-zA-Z0-9]*)$)')
patternNUM=re.compile(r'(^[0-9])(([0-9]*)$)')
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
def Analyzer(document):
      string = " "
      try:
            f = open(document, 'r',encoding='gb18030',errors='ignore')
            ls = f.read()
            ls += string
            token = ''
            for i in ls:
                  # 出现换行符
                  if i == '\n' or i == '\t' or i == '\t\n':
                        i = " "
                  # 无歧义一元运算符
                  if token in rwopt11:
                        print('(' + str(dict[token]) + ',' + token + ')')
                        token = ''
                  # 二元运算符左半边
                  elif token in rwopt12:
                        # 访问的元素是否为二元运算符右半边
                        if i not in rwopt13:
                              print('(' + str(dict[token]) + ',' + token + ')')
                              token = ''
                  token += i
                  # print(token)

                  # #遍历差最后一项就全部结束
                  # if i == ls[-1]:
                  #       if token in rwopt11:
                  #             print('(' + str(dict[token]) + ',' + token + ')')
                  #       elif token in rwopt2:
                  #             print('(' + str(dict[token]) + ',' + token + ')')
                  #       elif patternID.match(token):
                  #             if token in rwtab:
                  #                   print('('+str(dict[token])+','+token+')')
                  #             else:
                  #                   print('(' + str(dict['ID']) + ',' + token + ')')
                  #       elif patternNUM.match(token):
                  #             print('('+str(dict['NUM'])+','+token+')')
                  # else:

                  # 二元运算符
                  if token in rwopt2:
                        print('(' + str(dict[token]) + ',' + token + ')')
                        token = ''
                  # 结尾匹配到空格
                  elif token[-1] == " ":
                        token = token[:-1]
                        if patternID.match(token):
                              if token in rwtab:
                                    print('(' + str(dict[token]) + ',' + token + ')')
                                    token = ''
                              else:
                                    print('(' + str(dict['ID']) + ',' + token + ')')
                                    token = ''
                        elif patternNUM.match(token):
                              print('(' + str(dict['NUM']) + ',' + token + ')')
                              token = ''
                        else:
                              if token == '':
                                    pass
                              else:
                                    print('(' + dict['error'] + ',' + token + ')')
                              token = ''
                  # 结尾匹配到标点符号
                  elif token[-1] in rwopt1:
                        token_operator = token[-1]
                        token = token[:-1]
                        if patternID.match(token):
                              if token in rwtab:
                                    print('(' + str(dict[token]) + ',' + token + ')')
                                    token = token_operator
                              else:
                                    print('(' + str(dict['ID']) + ',' + token + ')')
                                    token = token_operator
                        elif patternNUM.match(token):
                              print('(' + str(dict['NUM']) + ',' + token + ')')
                              token = token_operator
                        else:
                              if token == '':
                                    pass
                              else:
                                    print('(' + dict['error'] + ',' + token + ')')
                              token = token_operator
                  # 结尾匹配到错误符号
                  elif token[-1] not in rwopt1 and re.match(patternID, token[-1]) == None and re.match(patternNUM,token[-1]) == None:
                        token_error = token[-1]
                        token = token[:-1]
                        if patternID.match(token):
                              if token in rwtab:
                                    print('(' + str(dict[token]) + ',' + token + ')')
                                    token = ''
                              else:
                                    print('(' + str(dict['ID']) + ',' + token + ')')
                                    token = ''
                        elif patternNUM.match(token):
                              print('(' + str(dict['NUM']) + ',' + token + ')')
                              token = ''
                        else:
                              if token == '':
                                    pass
                              else:
                                    print('(' + dict['error'] + ',' + token + ')')
                              token = ''
                        print('(' + dict['error'] + ',' + token_error + ')')
            f.close()
      except Exception:
            while True:
                  choose=input("文件无法打开。是否重新输入?(Y/N)")
                  if choose.upper()!='Y' and choose.upper()!='N':
                        print("输入错误!请重新输入。")
                  elif choose.upper()=='Y':
                        document=input("""请输入文件绝对路径。格式形如'C:\\Users\\lenovo\\Desktop\\test.txt'
""")
                        document=document.replace('\\','\\\\')
                        document=document.replace('"','')
                        Analyzer(document)
                        break
                  elif choose.upper()=='N':
                        break
b = True
while b:
      while True:
            choose=input("""该词法分析器有如下功能。请选择功能所对应的序号。
1:手动输入文件
2:输入已写好的文件路径
3:退出
""")
            if choose!='1' and choose!='2' and choose!='3':
                  print("选择错误！请重新输入。")
            elif choose=='1':
                  print('请输入文件。换行输入"结束"代表文件输入完毕。')
                  f=open('test.txt','w')
                  while True:
                        f_line = input()
                        if f_line == '结束':
                              break
                        f.write(f_line+'\n')
                  f.close()
                  Analyzer('test.txt')
                  break
            elif choose=='2':
                  document=input("""请输入文件绝对路径。格式形如'C:\\Users\\lenovo\\Desktop\\test.txt'
""")
                  document=document.replace('\\','\\\\')
                  document=document.replace('"','')
                  Analyzer(document)
                  break
            elif choose=='3':
                  exit()
      while True:
            a=input("是否继续分析词法？(Y/N):")
            if a.upper()!='Y' and a.upper()!='N':
                  print("输入错误！请重新输入。")
            elif a.upper()=='Y':
                  break
            else:
                  b=False
                  break
os.system('pause')






