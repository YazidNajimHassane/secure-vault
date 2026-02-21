from flask import render_template , redirect , url_for , request , session
from werkzeug.security import check_password_hash , generate_password_hash
from app import app , db 
from  models import User , Password
from encryption import encrypt_password , decrypt_password

#home page
@app.route('/')
def home():
    return render_template("home.html")


#register page 
@app.route('/register' , methods=["POST"])
def register():
    username = request.form.get("username")
    password_master = request.form.get("password")

    #check if user already exists
    user = User.query.filter_by(username=username).first()
    if user:
        return "Username already exists"
    
    #create new user
    new_user=User()
    new_user.username=username
    new_user.set_password(password_master)

    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for('login'))



@app.route('/login' , methods=["POST" , "GET"])
def login():
    if request.method=="POST":
        username = request.form.get("username")
        password_master = request.form.get("password")

        #check if user already exists
        user = User.query.filter_by(username=username).first()

        if not user or not user.check_password(password_master):
            return "Invalid username or password"
        
        session['user_id']=user.id

        return redirect(url_for("dashboard"))
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for("login"))
    user=User.query.get(session['user_id'])
    passwords= Password.query.filter_by(user_id=user.id).all()
    return render_template("dashboard.html" , passwords=passwords)

