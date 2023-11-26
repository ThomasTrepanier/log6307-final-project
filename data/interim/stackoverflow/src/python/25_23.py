class Company(db.Model):

    __tablename__ = "company"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    addressLine1 = db.Column(db.String(250), nullable=False)
    addressLine2 = db.Column(db.String(250), nullable=True)
    city = db.Column(db.String(250), nullable=False)
    state = db.Column(db.String(250), nullable=False)
    zipCode = db.Column(db.String(10), nullable=False)
    logo = db.Column(db.String(250), nullable=True)
    website = db.Column(db.String(250), nullable=False)
    recognition = db.Column(db.String(250), nullable=True)
    vision = db.Column(db.String(250), nullable=True)
    history = db.Column(db.String(250), nullable=True)
    mission = db.Column(db.String(250), nullable=True)
    jobs = relationship("Job", cascade="all, delete-orphan")

    def save_to_db(self):
        print("=====inside save_to_db=======")
        db.session.add(self)
        db.session.commit()
