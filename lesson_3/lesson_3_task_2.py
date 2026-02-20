from smartphone import Smartphone

catalog =[
    Smartphone("Sumsung", "S20", "+79554536789"),
    Smartphone("SUMSUNG", "Q21", "+78986545555"),
    Smartphone("Honor", "I25", "+79996545559"),
    Smartphone("Iphone", "17 Pro", "+76479922444"),
    Smartphone("Redme", "Note8T", "+79526677888"),
]
for smartphone in catalog:
    print(f"{smartphone.name} - {smartphone.model}. {smartphone.number}")