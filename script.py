import mysql.connector
import sys
from data import tables, extra_tables

def connect_db(database=None):
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="sqlwwtdd",
        database=database
    )

def create_database(database_name):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sqlwwtdd"
        )
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"Database '{database_name}' created successfully.")
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error creating database '{database_name}': {err}")

def create_tables(cursor):
    for table_name, table_data in tables.items():
        columns = table_data['columns']
        column_definitions = ', '.join([f'{name} {dtype}' for name, dtype, *constraint in columns])
        constraint_definitions = ', '.join([constraint[0] for name, dtype, *constraint in columns if constraint])
        
        create_table_query = f'CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions}'
        if constraint_definitions:
            create_table_query += f', {constraint_definitions}'
        create_table_query += ')'

        try:
            cursor.execute(create_table_query)
            print(f"Table '{table_name}' created successfully.")
        except mysql.connector.Error as err:
            print(err)  

def create_extra_tables(cursor):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS participation_evenement (
                evenement_id INT,
                monster_id INT,
                date_participation DATE NOT NULL,
                PRIMARY KEY (evenement_id, monster_id),
                FOREIGN KEY (evenement_id) REFERENCES Evenement(evenement_id),
                FOREIGN KEY (monster_id) REFERENCES Monster(monster_id)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Combat_Monster (
                combat_id INT,
                monster_id INT,
                resultat BOOLEAN NOT NULL,
                PRIMARY KEY (combat_id, monster_id),
                FOREIGN KEY (combat_id) REFERENCES Combat(combat_id),
                FOREIGN KEY (monster_id) REFERENCES Monster(monster_id)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS participation_quete (
                monster_id INT,
                quete_id INT,
                dateDebut DATE NOT NULL,
                PRIMARY KEY (monster_id, quete_id),
                FOREIGN KEY (monster_id) REFERENCES Monster(monster_id),
                FOREIGN KEY (quete_id) REFERENCES Quete(quete_id)
            );
        """)
        print("Table 'participation_evenement', Combat_Monster et participation_quete à été crée !")

def insert_extra_data(cursor):
    try:
        # Disable foreign key checks
        cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
        
        for table_name, table_data in extra_tables.items():
            columns = [col[0] for col in table_data['columns'] if not col[0].startswith("FOREIGN KEY")]
            values = table_data['values']
            
            placeholders = ', '.join(['%s'] * len(columns))
            columns_str = ', '.join(columns)
            insert_query = f'INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})'

            for value_tuple in values:
                if len(value_tuple) == len(columns):
                    # Convert 'Oui'/'Non' to True/False for BOOLEAN fields
                    converted_value_tuple = tuple(True if v == 'Oui' else False if v == 'Non' else v for v in value_tuple)
                    try:
                        cursor.execute(insert_query, converted_value_tuple)
                        print(f"Data inserted into '{table_name}' successfully.")
                    except mysql.connector.Error as err:
                        print(f"Error inserting data into '{table_name}': {err}")
                else:
                    print(f"Skipping insertion for table '{table_name}' due to parameter mismatch. Columns: {len(columns)}, Values: {len(value_tuple)}")
    
    finally:
        # Re-enable foreign key checks after inserting data
        cursor.execute("SET FOREIGN_KEY_CHECKS=1;")



def insert_data(cursor):
    try:
        # Disable foreign key checks
        cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
        
        for table_name, table_data in tables.items():
            columns = [col[0] for col in table_data['columns'] if not col[0].startswith("FOREIGN KEY")]
            values = table_data['values']
            
            placeholders = ', '.join(['%s'] * len(columns))
            columns_str = ', '.join(columns)
            insert_query = f'INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})'

            # Validate values length matches columns length
            valid_values = []
            for value_tuple in values:
                if len(value_tuple) == len(columns):
                    # Convert 'Oui'/'Non' to True/False for BOOLEAN fields
                    converted_value_tuple = tuple(True if v == 'Oui' else False if v == 'Non' else v for v in value_tuple)
                    valid_values.append(converted_value_tuple)
                else:
                    print(f"Skipping insertion for table '{table_name}' due to parameter mismatch. Columns: {len(columns)}, Values: {len(value_tuple)}")

            try:
                cursor.executemany(insert_query, valid_values)
                print(f"Data inserted into '{table_name}' successfully.")
            except mysql.connector.Error as err:
                print(f"Error inserting data into '{table_name}': {err}")
    
    finally:
        # Re-enable foreign key checks after inserting data
        cursor.execute("SET FOREIGN_KEY_CHECKS=1;")


def delete_table(cursor, table_name):
    try:
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        print(f"Table '{table_name}' deleted successfully.")
    except mysql.connector.Error as err:
        print(f"Error deleting table '{table_name}': {err}")


def drop_database(cursor, database_name):
    try:
        cursor.execute(f"DROP DATABASE {database_name}")
        print(f"Database '{database_name}' dropped successfully.")
    except mysql.connector.Error as err:
        print(f"Error dropping database '{database_name}': {err}")

def execute_queries():
    queries = [
        "SELECT monster_id, nom FROM Monster WHERE capturee = TRUE ORDER BY dateCapture DESC",
        "SELECT Type.nom AS Type, COUNT(Monster.monster_id) AS Nombre FROM Monster JOIN Type ON Monster.type_id = Type.type_id GROUP BY Type.type_id",
        "SELECT Monster.nom, CONCAT(Dresseur.nom, ' ', Dresseur.prenom) AS dresseur FROM Monster LEFT JOIN Dresseur ON Monster.idDresseur = Dresseur.dresseur_id",
        
        "SELECT Magasin.nom AS Magasin, Monster.nom AS Monster, CONCAT(Dresseur.nom, ' ', Dresseur.prenom) AS Dresseur, Vente.prix, Vente.date FROM Vente JOIN Magasin ON Vente.magasin_id = Magasin.magasin_id JOIN Monster ON Vente.monster_id = Monster.monster_id LEFT JOIN Dresseur ON Vente.dresseur_id = Dresseur.dresseur_id ORDER BY Vente.date DESC;",
    
        "SELECT Magasin.nom AS Magasin, SUM(Vente.prix) AS CA FROM Vente JOIN Magasin ON Vente.magasin_id = Magasin.magasin_id GROUP BY Magasin.magasin_id",
        "SELECT Monster.nom, participation_quete.dateDebut AS DateQuete FROM Monster LEFT JOIN participation_quete ON Monster.monster_id = participation_quete.monster_id ORDER BY participation_quete.dateDebut DESC",
        "SELECT Evenement.nom AS Evenement, COUNT(participation_evenement.monster_id) AS NombreParticipants, Arene.nom AS Arene, (SELECT COUNT(*) FROM Equipement WHERE Equipement.arene_id = Evenement.arene_id) AS EquipementsDisponibles, (SELECT COUNT(*) FROM Combat WHERE Combat.evenement_id = Evenement.evenement_id) AS CombatsEffectues FROM Evenement LEFT JOIN participation_evenement ON Evenement.evenement_id = participation_evenement.evenement_id JOIN Arene ON Evenement.arene_id = Arene.arene_id GROUP BY Evenement.evenement_id ORDER BY COUNT(participation_evenement.monster_id) ASC",
        "SELECT * FROM Monster JOIN Type ON Monster.type_id = Type.type_id WHERE Type.nom = 'feu' AND Monster.capturee = false AND Monster.niveau BETWEEN 2 AND 5 AND Monster.pointVie > 400 ORDER BY Monster.pointVie ASC",

        "SELECT Espece.nom, COUNT(Monster.monster_id) AS NombreMonsters FROM Espece JOIN Monster ON Espece.espece_id = Monster.espece_id GROUP BY Espece.espece_id HAVING COUNT(Monster.monster_id) >= 4;"
    ]

    try:
        connection = connect_db("monstermon")
        cursor = connection.cursor()
        compteur = 1
        for query in queries:
            cursor.execute(query)
            result = cursor.fetchall()
            print(f"Query: {query}")
            print("Results:",)
            print(f"Results (compteur {compteur}):")
            for row in result:
                compteur += 1
                print(row)

        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

def main(action, table_name=None, database_name=None):
    try:
        if action == 'create_database' and database_name:
            create_database(database_name)
        elif action == 'create_tables':
            create_database("monstermon")  
            connection = connect_db("monstermon")
            cursor = connection.cursor()
            create_tables(cursor)
            connection.commit()
            cursor.close()
            connection.close()
        elif action == 'create_extra_tables':
            connection = connect_db("monstermon")
            cursor = connection.cursor()
            create_extra_tables(cursor)
            connection.commit()
            cursor.close()    
        elif action == 'insert_data':
            connection = connect_db("monstermon")
            cursor = connection.cursor()
            insert_data(cursor)
            connection.commit()
            cursor.close()
            connection.close()
        elif action == 'insert_extra_data':
            connection = connect_db("monstermon")
            cursor = connection.cursor()
            insert_extra_data(cursor)
            connection.commit()
            cursor.close()    
        elif action == 'delete_table' and table_name:
            connection = connect_db("monstermon")
            cursor = connection.cursor()
            delete_table(cursor, table_name)
            connection.commit()
            cursor.close()
            connection.close()
        elif action == 'drop_database' and database_name:
            connection = connect_db("monstermon")
            cursor = connection.cursor()
            drop_database(cursor, database_name)
            connection.commit()
            cursor.close()
            connection.close()
        elif action == 'execute_queries':
            execute_queries()
        else:
            print("Invalid action or missing table name for deletion.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <action> [Actions]")
        print("Actions: create_database, create_tables, insert_data, delete_table, drop_database, execute_queries")
    else:
        action = sys.argv[1]
        table_name = sys.argv[2] if len(sys.argv) > 2 else None
        database_name = sys.argv[2] if len(sys.argv) > 2 else None
        main(action, table_name, database_name)
