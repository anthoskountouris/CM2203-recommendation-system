from application import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(50), nullable=False)
    post = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    level = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    function = db.Column(db.String(50), nullable=False)
    industry = db.Column(db.String(100), nullable=False)

    #def __repr__(self):
     #   return f"Jobs('{self.company_name}', '{self.post}', '{self.location}', '{self.post}', '{self.level}', '{self.type}', '{self.function}', '{self.industry}')"
