from flask import Blueprint, render_template, request
auth = Blueprint('auth', __name__)

@auth.route('/sign_in', methods = ['GET', 'POST'])
def sign_in():
    return render_template('sign_in.html', user = 'kim')

@auth.route('/logout')
def logout():
    return render_template('logout.html')

@auth.route('/sign_up', methods = ['GET','POST'])
def sign_up():
    # 데이터 확인
    if request.method == 'POST':
        nickname = request.form.get('nickname')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 5:
            pass
        elif len(nickname) < 2:
            pass
        elif password1 != password2 :
            pass
        elif len(password1) < 7:
            pass
        else:
            pass  # Create User -> DB
    data = request.form
    print(data) # POST로 요청할때만 값나옴
    return render_template('sign_up.html')