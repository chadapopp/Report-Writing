from flask_app.config.mysqlconnection import connectToMySQL

class Equipment:
    DB = 'report_schema'

    def __init__(self, equipment_data):
        self.id =  equipment_data['id']
        self.user_id =  equipment_data['user_id']
        self.equipment_type =  equipment_data['equipment_type']
        self.equipment_number =  equipment_data['equipment_number']
        self.equipment_name =  equipment_data['equipment_name']
        self.created_at =  equipment_data['created_at']
        self.updated_at =  equipment_data['updated_at']

    @classmethod
    def equipment_save(cls, data):
        query = "INSERT INTO equipment (user_id, equipment_type, equipment_number, equipment_name) VALUES (%(user_id)s, %(equipment_type)s, %(equipment_name)s, %(equipment_number)s)"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def equipment_update(cls, data):
        query = "UPDATE equipment SET equipment_type = %(equipment_type)s, equipment_number = %(equipment_number)s, equipment_name = %(equipment_name)s WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_one_equipment(cls, data):
        query = "SELECT * FROM equipment WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def delete_equipment(cls, data):
        query = "DELETE FROM equipment WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all_equipment_per_user(cls, data):
        query = "SELECT * FROM equipment WHERE user_id = %(user_id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        equipment = []
        for row in results:
            equipment.append(cls(row))
        return equipment
    
    @classmethod
    def get_all_exchangers_per_user(cls, user_id):
        query = "SELECT * FROM equipment WHERE user_id = %(user_id)s AND equipment_type = 'Exchanger';"
        results = connectToMySQL(cls.DB).query_db(query, user_id)
        exchangers = []
        for row in results:
            exchangers.append(cls(row))
            print(exchangers)
        return exchangers
    
    @classmethod
    def get_all_drums_per_user(cls, user_id):
        query = "SELECT * FROM equipment WHERE user_id = %(user_id)s AND equipment_type = 'Drum';"
        results = connectToMySQL(cls.DB).query_db(query, user_id)
        drums = []
        for row in results:
            drums.append(cls(row))
            print()
        return drums
    
    @classmethod
    def get_all_towers_reactors_per_user(cls, user_id):
        query = "SELECT * FROM equipment WHERE user_id = %(user_id)s AND equipment_type = 'Tower' OR equipment_type = 'Reactor';"
        results = connectToMySQL(cls.DB).query_db(query, user_id)
        towers_reactors = []
        for row in results:
            towers_reactors.append(cls(row))
            print(towers_reactors)
        return towers_reactors
    
    @classmethod
    def get_all_heaters_per_user(cls, user_id):
        query = "SELECT * FROM equipment WHERE user_id = %(user_id)s AND equipment_type = 'Heater';"
        results = connectToMySQL(cls.DB).query_db(query, user_id)
        heaters = []
        for row in results:
            heaters.append(cls(row))
            print()
        return heaters
        

