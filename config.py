def create_config(app):
    app.config["SECRET_KEY"] = "12345"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///nossa_casa_db.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False