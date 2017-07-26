# -*- coding: utf-8 -*-

import jieba
import logging

def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    # jieba custom setting.
    # jieba.set_dictionary('jieba_dict/dict.txt.big')

    # load stopwords set
    #stopwordset = set()
    #with open('jieba_dict/stopwords.txt','r',encoding='utf-8') as sw:
    #    for line in sw:
    #        stopwordset.add(line.strip('\n'))

    output = open('zhwiki/wiki_seg.txt','w')
    
    texts_num = 0
    
    with open('zhwiki/zh_wiki.txt','r') as content :
        for line in content:
            words = jieba.cut(line, cut_all=False)
            for word in words:
                output.write(word +' ')
            texts_num += 1
            if texts_num % 10000 == 0:
                logging.info("已完成前 %d 行的斷詞" % texts_num)
    output.close()
    
if __name__ == '__main__':
	main()
