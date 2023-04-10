#Installez cx_Oracle d'abord via Pip
import cx_Oracle

# Définir les détails de connexion Oracle Remplacez les 3 valeurs de paramètres avec les votres
data = cx_Oracle.makedsn('hostnameXXXX', 'portXXX', nom_db='nom_dbXXXX')
connection = cx_Oracle.connect(user='usernameXXX', password='passwordXXX', dsn=data)

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
