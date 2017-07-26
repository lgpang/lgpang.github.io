python3 wiki_to_text.py zhwiki/zhwiki-latest-pages-articles.xml.bz2
brew install opencc
opencc -i wiki_texts.txt -o zhwiki/zh_wiki.txt -c t2s.json
pip3 install jieba
python3 jieba_fenci.py
python3 train.py
