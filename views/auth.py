from flask import Blueprint,render_template,url_for,flash,request,redirect,jsonify
from flask_jwt_extended import jwt_required, unset_jwt_cookies, set_access_cookies, get_jwt_identity
from controllers import createUser,getUser,login_user,getUserById,getRoutineCount


auth_views=Blueprint('auth_views',__name__,template_folder='../Templates')


@auth_views.route('/',methods=['GET'])
def login_page():
    return render_template('login.html')

@auth_views.route('/signup',methods=['GET'])
def signup_page():
    return render_template('signup.html')

@auth_views.route('/login',methods=['POST'])
def login():
    data=request.form
    user=login_user(data['username'],data['password'])
    response=None
    if user:
        flash('Login Successful','success') # Flash message (message,category)
        print("Success")
        response=redirect('/home')
        set_access_cookies(response,user)
    else:
        flash('Login Failed','error')
        print("Fail")
        response=redirect(request.referrer)
    return response

@auth_views.route('/logout',methods=['GET'])
@jwt_required()
def logout():
    response=redirect(url_for('auth_views.login_page'))
    unset_jwt_cookies(response)
    return response


@auth_views.route('/register',methods=['POST'])
def register():
    data=request.form
    user=getUser(data['username'])
    if user:
      flash('Username already exists','error')
      print("Username already exists")
      return redirect(request.referrer)
    else:
      createUser(data['username'],data['password'])
      flash('User created successfully','success')
      print("User created successfully")
      return redirect(url_for('auth_views.login_page'))
    

@auth_views.route('/account',methods=['GET'])
@jwt_required()
def account_page():
    username=getUserById(get_jwt_identity())
    routines=getRoutineCount(get_jwt_identity())
    return render_template('accounts.html',username=username,routines=routines)