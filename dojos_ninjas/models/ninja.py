# importar la función que devolverá una instancia de una conexión
from config.mysqlconnection import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('dojos_ninjas').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de users
        ninjas = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def newninja(cls, data ):
        query = "INSERT INTO ninjas ( first_name , last_name, age , dojo_id, created_at, updated_at ) VALUES ( %(first_name)s ,%(last_name)s,  %(age)s, %(dojo_id)s, NOW() , NOW() );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('dojos_ninjas').query_db( query, data )        


 