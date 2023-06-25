# importar la función que devolverá una instancia de una conexión
from config.mysqlconnection import connectToMySQL
from models.ninja import Ninja
# modelar la clase después de la tabla friend de nuestra base de datos
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # Creamos una lista para que luego podamos agregar todas las hamburguesas que están asociadas a un restaurante
        self.ninjas = []
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all_dojo(cls):
        query = "SELECT * FROM dojos;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('dojos_ninjas').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de users
        dojos = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def newdojo(cls, data ):
        query = "INSERT INTO dojos ( name , created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('dojos_ninjas').query_db( query, data )        

    @classmethod
    def get_dojo_with_ninjas( cls , data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_ninjas').query_db( query , data )
        # los resultados serán una lista de objetos topping (aderezo) con la hamburguesa adjunta a cada fila 
        dojo = cls( results[0] )
        ninjas = []
        for row_from_db in results:
            # ahora parseamos los datos de hamburguesa para crear instancias de hamburguesa y agregarlas a nuestra lista
            ninja_data = {
                "id" : row_from_db["id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                
                "created_at" : row_from_db["created_at"],
                "updated_at" : row_from_db["updated_at"]
            }
            ninjas.append(Ninja(ninja_data))
        dojo.ninjas = ninjas
        return dojo, ninjas

        
    