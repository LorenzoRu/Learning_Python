inial_K = float(input("Entrez le capital initial : "))
removal_rate = float(input("Entrez les retraits effectuer tous les 5 ans : "))
interest_rate = float(input("Entrez le taux d'intérêt : "))

current_K = inial_K
year = 0
objective = 2 * inial_K

while current_K < objective:
    current_K = current_K * (1 + interest_rate / 100) 
    year += 1
    if year % 5 == 0:
        current_K = current_K - removal_rate

    if current_K >= objective:
        print("The initial capital will be doubled in {} years.".format(year))
        break
    if current_K <= 0:
        print("Imposssible")
        break