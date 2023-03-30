import os
import requests
import json
import subprocess

# Collecte des données de surveillance système à partir des fichiers journaux
logs_dir = '/var/log'
system_logs = os.listdir(logs_dir)

# Collecte des données de surveillance système à partir des API REST (vous devez adapter)
api_urls = ['http://api1.example.com/metrics', 'http://api2.example.com/metrics']
api_metrics = []
for url in api_urls:
    response = requests.get(url)
    if response.status_code == 200:
        api_metrics.append(response.json())

# Agrégation des données de surveillance système à partir des bases de données (mysql)
db_metrics = []
db_query = 'SELECT * FROM metrics_table'
db_output = subprocess.check_output(['mysql', '-u', 'username', '-p', 'password', '-e', db_query])
db_metrics = json.loads(db_output)

# Agrégation des données de surveillance système à partir des métriques système
system_metrics = {}
cpu_metrics = subprocess.check_output(['top', '-n', '1', '-b'])
system_metrics['cpu'] = cpu_metrics.decode('utf-8')
memory_metrics = subprocess.check_output(['free', '-h'])
system_metrics['memory'] = memory_metrics.decode('utf-8')

# Génération de rapports et d'alertes
report = {}
report['system_logs'] = system_logs
report['api_metrics'] = api_metrics
report['db_metrics'] = db_metrics
report['system_metrics'] = system_metrics

# Envoi de l'alerte par email
if report['system_metrics']['cpu'] > 90 or report['system_metrics']['memory'] < '1G':
    email_body = json.dumps(report)
    subprocess.Popen(['mail', '-s', 'Alerte de surveillance système', 'admin@example.com'], stdin=subprocess.PIPE).communicate(input=email_body.encode('utf-8'))
