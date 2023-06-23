from flask_app.config.mysqlconnection import connectToMySQL



class Ninja:
    DB = 'dojos_and_ninjas_schema'
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def get_all(cls):
        query = '''
            SELECT *
            FROM ninjas;
        '''

        results = connectToMySQL(cls.DB).query_db(query)

        all_ninjas=[]

        for ninja in results:
            all_ninjas.append( cls(ninja) )

        return all_ninjas
    
    @classmethod
    def add_ninja(cls,data):
        query="""
        INSERT 
        INTO ninjas (first_name, last_name, age, dojo_id)
        VALUES( %(first_name)s , %(last_name)s , %(age)s , %(dojo_id)s );
        """

        results = connectToMySQL(cls.DB).query_db(query,data)

        return results
    
    @classmethod
    def update_ninja(cls,data):
        query="""
        UPDATE ninjas
        SET name = %(first_name)s , %(last_name)s , %(age)s , %(dojo_id)s
        WHERE ninjas.id = %(ninja_id)s ;
        """

        results = connectToMySQL(cls.DB).query_db(query, data)

        return results