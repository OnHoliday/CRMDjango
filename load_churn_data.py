from clients.models import Client
import csv

reader = csv.reader(open('churn_data.csv', 'r'))

for client in reader:
	client = Client(
					client_id = client[1],
					client_name = client[2],
					credit_score = client[3],
					geography = client[4],
					gender = client[5],
					age = client[6],
					tenure = client[7],
					balance = client[8],
					num_of_products = client[9],
					has_credit_card = client[10],
					is_active_member = client[11],
					estimated_salary = client[12],
					exited = client[13]
					)
	client.save()
