data = {
    "01" : {"département" : "Ain", "chef-lieu" : "Bourg-en-Bresse","région" : "Auvergne-Rhône-Alpes"},
    "02" : {"département" : "Aisne", "chef-lieu" : "Laon", "région" : "Hauts-de-France"},
    "03" : {"département" : "Allier", "chef-lieu" : "Moulin", "région" : "Auvergne-Rhône-Alpes"},
    "04" : {"département" : "Alpes-de-Haute-Provence", "chef-lieu" : "Digne", "région" : "Provence-Alpes-Côte d'Azur"},
    "05" : {"département" : "Hautes-Alpes", "chef-lieu" : "Gap", "région" : "Provence-Alpes-Côte d'Azur"},
    "06" : {"département" : "Alpes-Maritimes", "chef-lieu" : "Nice", "région" : "Provence-Alpes-Côte d'Azur"},
    "07" : {"département" : "Ardèche", "chef-lieu" : "Privas", "région" : "Auvergne-Rhône-Alpes"},
    "08" : {"département" : "Ardennes", "chef-lieu" : "Charleville-Mézières", "région" : "Grand Est"},
    "09" : {"département" : "Ariège", "chef-lieu" : "Foix", "région" : "Occitanie"},
    "10" : {"département" : "Aube", "chef-lieu" : "Troyes", "région" : "Grand Est"}
}
label = input()
number = input()

if number in data and label in data[number]:
    print(f"{data[number][label]}")

else:
    print("KO")
