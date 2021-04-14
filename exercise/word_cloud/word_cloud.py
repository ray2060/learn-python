from wordcloud import WordCloud


f = open('word_cloud.txt')
txt = f.read()

wc = WordCloud(width=800, height=600, background_color='white').generate(txt)
wc.to_file('word_cloud.png')
