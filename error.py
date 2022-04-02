# Author: Peanut
# -*- codeing = utf-8 -*-
# @Time : 2020/7/30 21:02
# @File : error.py
# @Software :PyCharm

import sqlite3
import re

text = [
    "AS soon as you trust youself, you will know how to live. You can do anything,but not everything. Either you run the day,or the day runs you. You can't find peace by avoiding life.",
    "我大学的愿望：找份不错的兼职，闲来无事逛图书馆，偶尔听听校园音乐会🎵，认真学习，认真生活，无聊找同学聊天，邂逅一个人。我会努力哒！٩( 'ω' )و",
    "how are you  ̶s̶a̶d̶,̶ ̶b̶r̶o̶k̶e̶n̶,̶ ̶d̶e̶f̶e̶a̶t̶e̶d̶,̶ ̶c̶r̶u̶s̶h̶e̶d̶,̶ ̶l̶o̶n̶e̶l̶y̶,̶ ̶f̶a̶l̶l̶i̶n̶g̶ ̶a̶p̶a̶r̶t̶ i'm fine. ",
    "What's the matter?",
    "需要我们自己静独思辨，尔后得出自己的正知结论. 少有人能确切将有关世界观价值观维度的思想传输与我们，甚者（大多人）都无心于此和谈述 so.. there's a long way we should go. keep going 🙂 ↑",
    "可我不能放弃 我一定可以的 距离期末考试还有12天 要全力以赴 加油 ٩( 'ω' )و",
    "Do you know 'Practice makes perfect.'?",
    "看了下评论果然是网抑云<')))))><",
    "知道吗，万花筒里的世界不是绚丽的，而是破碎的。 You know？The world in kaleidoscopes is not colorful，but is broken.See？It's funny，isn't it？",
    "欢迎大家来到网抑云 世界一亿抑郁症 网抑云人均抑郁症o'",
    "'今天我的输入法也忘记你的名字了'",
    "I'm so sorry.",
    "I'm in love with your body。 我就是馋你身子",
    "Cowards do that，and ain't you. You're better than that.",
    "Don't worry",
    "Today is Father's Day 老师读这句话时哭了",
    "If we can't see each other again, wish you good morning, good afternoon, good night!",
    "？？？？？it's me",
    "哇 你们故事真多。但是请相信，除了生老病死，其实并没有什么大不了的。我们，就是来世间走一遭，然后就回去了。nowhere，I don't know.",
    "就像“忧郁的日子里须要镇静'一样",
    "好人要历经九九八十一难才能成佛， 坏人只需要放下屠刀就能立地成佛。 '这又是为什么呢",
    "取消喜欢的话其实可以不说，这评论区里面有多少“受伤'的孩子靠着它来治愈自己的伤痕",
    "He doesn't like girls",
    "???I fell in love with a homosexual, he doesn't like girls, can you understand?",
    "组长，下辈子你想当什么样的人？我想当个平凡的人，出生在平凡的家庭。你的梦想，'真了不起'那么，你呢？我嘛，我想出生在出生在平凡家庭的平凡的组长的隔壁的平凡家庭。喂，你们这些幼稚鬼。那我就变成你们两个的性感邻居，玩弄过你们之后再抛弃你们",
    "I Don't know what is sad, I don't know what is sad, I don't know, what is lonely.",
    "I'm fine.And you?I love you",
    "how are you ̶s̶a̶d̶,̶ ̶b̶r̶o̶k̶e̶n̶,̶ ̶d̶e̶f̶e̶a̶t̶e̶d̶,̶ ̶c̶r̶u̶s̶h̶e̶d̶,̶ ̶l̶o̶n̶e̶l̶y̶,̶ ̶f̶a̶l̶l̶i̶n̶g̶ ̶a̶p̶a̶r̶t̶ i'm fine.",
    "I'm a girl, but I fell in love with a gay",
    "Can't get no love without sacrifice",
    "〰 how are you  ̶s̶a̶d̶,̶ ̶b̶r̶o̶k̶e̶n̶,̶ ̶d̶e̶f̶e̶a̶t̶e̶d̶,̶ ̶c̶r̶u̶s̶h̶e̶d̶,̶ ̶l̶o̶n̶e̶l̶y̶,̶ ̶f̶a̶l̶l̶i̶n̶g̶ ̶a̶p̶a̶r̶t̶ i'm fine. ",
    "Oh don't say that you're so beautiful",
    "C'est la vie ！",
    "(*'へ'*)",
    "Everyone's understanding of this song is different, because everyone's story is different.",
    "Our new foreign students are going to arrive very soon,and here are some ways to welcome them. How close do you stand when you talk to a friend? You can stend too close to Middle East but don't stand too close to North Americans! Give them more pesonal space(好难背哎~(>_<)~)",
    "You lie! It's been 10 years,but I can't release myself.If this isn't love,why it is so hurt?",
    "乖 去吃饭吧 吃饱才有力气和作业奋斗到底（ '▿ ' ）",
    "好的⌯'ㅅ'⌯",
    "Don't cry. Wipe your tears.Cheer up!",
    "There is a Crack in Everything, That's How the Light Gets in",
    "oh maybe you haven't gotten what i mean...",
    "捕捉到评论区的一位温柔的小可爱，一直在安抚其他心情有点糟糕的村民们，突然被暖到，希望听这首歌的人儿都平安喜乐，顺道分享最近的动力源泉——我可以一蹶不振，我偏要一鸣惊人。我与我周旋久，宁作我。Life is not so bad (ง •̀_•́)ง中考高考考研工作，人生必经处，you're not alone.",
    "It doesn't matter.Memories are just memories. I want time travel in Einstein's theory of relativity to be realized,but impossible. And……I don't even…… even know what's wrong with me now…… Alas……Just listen……and recollect.",
    "I hope you're here for me",
    "We'll see each other again！好！！谢谢你(*'▽'*)",
    "它说：嘿嘿你也是啊，小可爱（ '▿ ' ）",
    "You are all guardians of this city.When you meet difficulties, don't lose heart, listen to this song, and then you shout to the sky: I can refueling, I am the best.",
    "I don't love you anymore。",
    "I love you. But I don't just love you.",
    "Captain，are you sure to restart 2020？Yes，turn on the machine.Even we back to 2019，the conoravirus always infect the someone that infected in 2020，it is a destiny.Don't fell into the “hole”---2020/4/18 3：26",
    "坚持就是胜利。( '-ωก̀ )揉眼睛",
    "Are you happy? Are you happy? No, you're sad.",
    "As xorepsoume，A Little Story，ASpiral Moon，Adagio for Summer Wind，Old Memory，Away From，Aphrodite，白ゆきの独白，Before it's too late，遠い空へ",
    "how are you ̶s̶a̶d̶,̶ ̶b̶r̶o̶k̶e̶n̶,̶ ̶d̶e̶f̶e̶a̶t̶e̶d̶,̶ ̶c̶r̶u̶s̶h̶e̶d̶,̶ ̶l̶o̶n̶e̶l̶y̶,̶ ̶f̶a̶l̶l̶i̶n̶g̶ ̶a̶p̶a̶r̶t̶ i'm fine",
    "however i have nothing,i'll not be afraid of losing any more",
    "I'm coming"]
conn = sqlite3.connect('Comment.db')
cur = conn.cursor()

text2 = []

for temp in text:
    temp = re.sub("'", "\'", temp)
    text2.append(temp)


for y in text2:
    sql = '''insert into musicView (comment) values("%s");
        ''' % y

    cur.execute(sql)
    conn.commit()

cur.close()
conn.close()
