from flask import render_template, request, flash, redirect, url_for
from models import create_models


def create_views(app, db):
    User, Apartment = create_models(db)

    @app.route("/")
    def index():
        apartments = Apartment.query.all()
        return render_template("index.html", apartments = apartments)
    
    @app.route("/pesquisar", methods = ["POST"])
    def pesquisar():
        topologia = request.form.getlist("topologia")[0]
        apartments = Apartment.query.filter_by(topologia=topologia)
        return render_template("index.html", apartments = apartments)

    @app.route("/login")
    def login():
        return render_template("login.html")
    
    @app.route("/arrendar/<id>", methods=["GET", "POST"])
    def arrendar(id):
        id = int(id)

        if request.method == "POST":
            nome = request.form["nome"]
            bi = request.form["bi"]
            email = request.form["email"]
            telefone = request.form["telefone"]
                
            user = User(nome, bi, email, telefone)
            apartment = Apartment.query.filter_by(id = id).first()
            apartment.estado = "Ocupado"
                
            db.session.add(user)
            db.session.commit()

            flash("Arrendamento feito com êxito")

            return render_template("form_arrendamento.html")
        
        apartment = Apartment.query.filter_by(id=id).first()

        if apartment.estado == "Ocupado":
            flash("Este apartamento não se encontra disponível")
            return redirect(url_for("index"))
        
        return render_template("form_arrendamento.html", id = id)
