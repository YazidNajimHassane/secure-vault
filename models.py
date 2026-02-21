from flask_sqlalchemy import SQLAlchemy
from  werkzeug.security import check_password_hash , generate_password_hash


db=SQLAlchemy()

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(25),nullable=False)
    password_master=db.Column(db.String(150),nullable=False)

    #the link to the Password table 
    passwords = db.relationship('Password',backref='user' , lazy=True)
    
    def set_password(self, password):
        self.password_master=generate_password_hash(password)

    def check_password(self , password):
        return check_password_hash(self.password_master,password)
    

class Password(db.Model):
    id=db.Column(db.Integer , primary_key=True)
    site_name=db.Column(db.String(100),nullable=False)
    encrypted_password=db.Column(db.String(100),nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
