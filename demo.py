# @Time : 2019/10/21 10:26 
# @Author : zhang_san_jin
# @File : demo.py 
# @Software: PyCharm
# x = 0o1010
# print(x)

# for s in "HelloWorld":
#     if s=="W":
#         continue
#     print(s,end="")
# x=10
# y=3
# print(divmod(x,y))
# import jieba
# s = "中华人民共和国是一个伟大的国家"
# print(jieba.lcut(s))    #jieba,lcut 精确模式，返回列表
# print(jieba.lcut(s,cut_all=True))   #cut_all=True全模式 ，返回列表
# print(jieba.lcut_for_search(s))  #搜索引擎模式
# import time
# import turtle
# d = 0
# for i in range(3):
#     turtle.fd(200)
# #     # turtle.circle(200, extent=None)
# #     time.sleep(2)
# #     d = d + 120
# #     turtle.seth(d)
# ls = ["综合", "理工", "综合", "综合", "综合", "综合", "综合", "综合", "综合", "综合",
#       "师范", "理工", "综合", "理工", "综合", "综合", "综合", "综合", "综合","理工",
#       "理工", "理工", "理工", "师范", "综合", "农林", "理工", "综合", "理工", "理工",
#       "理工", "综合", "理工", "综合", "综合", "理工", "农林", "民族", "军事"]
# d = {}
# for i in ls:
#     d[i] = d.get(i,0)+1
#     print(d[i])
# for k in d:
#     print("{}:{}".format(k, d[k]))

# ls = ["综合", "理工", "综合", "综合", "综合", "综合", "综合", "综合", \
#       "综合", "综合", "师范", "理工", "综合", "理工", "综合", "综合", \
#       "综合", "综合", "综合", "理工", "理工", "理工", "理工", "师范", \
#       "综合", "农林", "理工", "综合", "理工", "理工", "理工", "综合", \
#       "理工", "综合", "综合", "理工", "农林", "民族", "军事"]
# d = {}
# for word in ls:
#     d[word] = d.get(word, 0) + 1
# for k in d:
#     print("{}:{}".format(k, d[k]))

dict = {"a":[1,2],"b":{"c":"12","d":"dd"},"e":(1,2,3),"d":0}
print(dict.get("a"))
print(dict.get("d",4)+1)
print(dict)