#Installer cx_Oracle d'abord via Pip
import cx_Oracle

# Définir les détails de connexion Oracle
data = cx_Oracle.makedsn('hostname', 'port', nom_db='nom_db')
connection = cx_Oracle.connect(user='username', password='password', dsn=data)

# Créer un curseur
cursor = connection.cursor()

# Exécuter une requête SELECT
query = "SELECT * FROM table exemple"
cursor.execute(query)

# Parcourir les résultats de la requête
for row in cursor:
    print(row)

# Fermer le curseur et la connexion à la base de données
cursor.close()
connection.close()
