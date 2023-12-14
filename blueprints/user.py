# -*- coding:utf-8 -*-
from flask import Blueprint,request,jsonify,flash,render_template
from modles import User
from exts import db

user_blueprint = Blueprint("user", __name__, url_prefix="/user")

@user_blueprint.route('/<username>', methods=['GET'])
def get_user_info(username):
    user = User.query.filter_by(username=username).first()
    if user:
        user_info = {
            'id': user.id,
            'username': user.username,
            'password': user.password
        }
        return jsonify(user_info)
    else:
        return jsonify({'error': 'User not found'}), 404
    
@user_blueprint.route('/add', methods=['POST','GET'])
def add():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user != None:
            flash('用户已存在', 'danger')
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            # 提交事务
            db.session.commit()
            flash('用户新增成功', 'success')
        return render_template('user-add.html')            
    return render_template('user-add.html')            
