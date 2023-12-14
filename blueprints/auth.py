# -*- coding:utf-8 -*-
from flask import Blueprint,request,redirect,render_template,url_for, flash
from modles import User


auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")

    
@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            flash(username, 'success')
            return render_template('home.html')            
        else:
            flash('登录失败，请检查用户名和密码', 'danger')
    return render_template('login.html')