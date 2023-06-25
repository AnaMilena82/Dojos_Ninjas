from flask import render_template, request, redirect
from __init__ import app
from models.dojo import Dojo
from models.ninja import Ninja


@app.route("/dojos", methods=["GET"])
def get_dojos():
    # llamar al método de clase get all para obtener todos los amigos
    dojos = Dojo.get_all_dojo()
    print(dojos)
    return render_template("dojos.html", dojos = dojos)


@app.route('/dojos', methods=["POST"])
def post_newdojos():
    data = {
        "name": request.form["name"]        
    }
    
    Dojo.newdojo(data)
    
    return redirect('/dojos')

@app.route('/dojos/<int:id>', methods=["GET"])
def get_dojo_ninjas(id):
    dojo, ninjas = Dojo.get_dojo_with_ninjas({"id": id})
    return render_template("show_dojos.html", dojo=dojo, ninjas=ninjas)

