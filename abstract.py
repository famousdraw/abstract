from app import app
from flask_script import Manager
#app.debug=true
#使用终端脚本工具启动和管理flask
manager=Manager(app)
if __name__ == '__main__':
    import os
    import sys
    sys.path.append('examples')
    sys.path.append('data')
    sys.path.append('src')
    print('abstract.py')
    print('当前目录为：',os.getcwd())
    manager.run()
else:
    print("package_abstract 初始化")