# -*- coding:utf-8 -*-

from flask import Flask
from exts import db
from flask_migrate import Migrate
from blueprints.auth import auth_blueprint
from blueprints.user import user_blueprint


app = Flask(__name__)
# 绑定配置文件
app.config.from_pyfile('config.py')

# 把db与app绑定
db.init_app(app)

# 上传数据库
migrate = Migrate(app, db)

## 注册蓝图
app.register_blueprint(auth_blueprint)
app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run(debug=True,port=8000)