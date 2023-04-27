company_users = {}

while True:
    line = input()
    if line == "End":
        break
    user, id_code = line.split(" -> ")
    if user not in company_users:
        company_users[user] = []

    if id_code not in company_users[user]:
        company_users[user].append(id_code)


for company, employees in company_users.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")


