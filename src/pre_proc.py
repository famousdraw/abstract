import re  #需要使用正则表达式
def token(string):
    # we will learn the regular expression next course.
    return re.findall('\w+', string.replace('\\n','\n'))  #所有的Words
    #return re.findall('\w+', string)  #所有的Words

def write_to_file(key):
    k=key
    filename='input_articles.txt' 
    outfile =open(filename,'w',encoding='utf-8') # Open file for writing
    for i in range(k):
        if not pd.isnull(articles[i]):      
            for line in token(articles[i]):
                #line=line.replace("\\n", "\n")
                #line=line.replace('\u3000','')
                outfile.write(line+"\n")
    outfile.flush()
    outfile.close( )
