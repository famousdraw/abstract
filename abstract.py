from app import app
from flask_script import Manager
#app.debug=true
#使用终端脚本工具启动和管理flask
manager=Manager(app)
if __name__ == '__main__':
    manager.run()