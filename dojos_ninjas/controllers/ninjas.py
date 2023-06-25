from flask import render_template, request, redirect, url_for
from __init__ import app
from models.dojo import Dojo
from models.ninja import Ninja


@app.route("/ninjas", methods=["GET"])
def get_new_ninjas():
    # llamar al método de clase get all para obtener todos los amigos
    dojos = Dojo.get_all_dojo()
    return render_template("new_ninjas.html", dojos = dojos)


@app.route('/ninjas', methods=["POST"])
def post_new_ninjas():
    data = {
        "first_name": request.form["first_name"],  
        "last_name": request.form["last_name"], 
        "age": request.form["age"], 
        "dojo_id": request.form["dojo_id"]
    }
    
    ninja_id  = Ninja.newninja(data)
    
    return redirect(url_for('get_dojo_ninjas', id=data['dojo_id']))

# @app.route("/users/<int:id>", methods=['GET'])
# def get_user_by_id(id):
   
#     # llamar al método de clase get all para obtener todos los amigos
#     userone = User.get_one(id)
#     return render_template("show_users.html", one_users = userone)
    


