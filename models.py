def create_models(db):
    class User(db.Model):
        __tablename__ = "users"
        id = db.Column(db.Integer, primary_key=True)
        nome = db.Column(db.String(256))
        bi = db.Column(db.String(30), unique=True)
        email = db.Column(db.String(100), unique=True)
        telefone = db.Column(db.String(30), unique=True)

        def __init__(self, nome, bi, email, telefone) -> None:
            self.nome = nome
            self.bi = bi
            self.email = email
            self.telefone = telefone
    
    
    class Apartment(db.Model):
        __tablename__ = "apartments"
        id = db.Column(db.Integer, primary_key=True)
        topologia = db.Column(db.String(5))
        provincia = db.Column(db.String(30))
        estado = db.Column(db.String(50))
        user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
        usuario = db.relationship('User', backref=db.backref('apartments'), lazy=True)

        def __init__(self, topologia, provincia, user_id) -> None:
            self.topologia = topologia
            self.provincia = provincia
            self.estado = "Desocupado"
            self.user_id = user_id

    return User, Apartment
