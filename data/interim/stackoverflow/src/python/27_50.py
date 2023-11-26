class User(db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, index=True)
    username = db.Column(db.String(20), unique=True, index=True)
    hash_passwrd = db.Column(db.String(200))



    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.hash_passwrd = generate_password_hash(password)


adams = user('adams@email.com', 'adams', 'adams@1')
ben= user('ben@email.com', 'ben', 'ben@1')
poolo= user('poolo@email.com', 'poolo', 'poolo@1')
