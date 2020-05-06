from app import app
from flask import render_template,request
import sys
import os
sys.path.append('examples')
sys.path.append('data')
sys.path.append('src')
print('routes.py')
import testrun
@app.route('/')
@app.route('/index')
#def index():
#    return render_template('index.html', title='请您输入')
@app.route('/index',methods=['GET','POST'])
def index():
    print('routes.py')
    print('当前目录为：',os.getcwd())
    print('sys.path',sys.path)
    input_text=''
    output_text=''
    if request.method == 'POST':
        print('post')
        # 接收数据
        input_text=request.form.get('input_text')
        if input_text != "":
            with open('data/test_news.txt', 'w', encoding='utf=8') as f:
                f.writelines(input_text)
        output_text=testrun.test( )
        print(output_text)
    return render_template('index.html',title='文本摘要结果', input_text=input_text,abstract_text=output_text)
