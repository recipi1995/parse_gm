PLACE_TYPE = ['restaurants', 'cafes', 'museums', 'cinemas', 'theaters', 'attractions', 'restaurant', 'bar', 'cafe', 'canteen', 'diner', 'bistro', 'pancakes' ,
        'burger', 'vegan + cafe', 'vegetarian + cafe', 'wine + restaurant', 'grill bars', 'lagmanny', 'noodle', 'dumplings', 'beer + restaurant', 'donut', 'raskarni',
        'fish + establishments', 'steak house', 'steak house', 'khinkalny', 'cheburek', 'shaverm', 'barbecue', 'temples', 'cathedrals', 'churches', 'mosques', 'religious + goods', 'monasteries',
        'religious + organizations', 'synagogue', 'chapels', 'spiritual + educational + institutions', 'parishes', 'monuments', 'places + historical + events', 'zoos', 'museums', 'galleries',
        'botanical + gardens',' libraries', 'castles',' bridges', 'skyscrapers',' shopping malls', 'parks',' national + parks', 'historic + parks',' manors', 'parks + entertainment ',
        'reserves', 'carnivals', 'fairs', 'houses + cultural + figures', 'monuments + architecture', 'monuments + urban planning', 'monuments + archeology', 'monuments + arts',
        'cinema attractions', 'fish + restaurant', 'cheese + restaurant', 'restaurants + national + cuisine', 'restaurants + cuisines + foreign + countries',
        'club', 'sushi bar', 'pub bar', 'sports bar', 'ice cream cafe', 'pastry cafe', 'milk cafe', 'pizzeria cafe', 'pizzeria', 'art cafe', 'internet cafe', 'cafe-club',
        'student-cafe', 'anti-cafe', 'canteen', 'diner', 'galleries', 'Art + center', 'art + quarter', 'hookah']

BINARY_LOCATION = "./chrome-win/chrome.exe"

BROWSER = './chromium.exe'

DICT_CITIES = {
    'Italy': ['Venice', 'Verona', 'Messina', 'Padua', 'Trieste', 'Taranto', 
            'Brescia', 'Prato', 'Parma', 'Modena'],
    'Russia': ['Saint-Petersburg', 'Moscow', 'Novosibirsk', 'Ekaterinburg', 'Kazan', 'Nizhniy-Novgorod', 'Chelyabinsk', 'Samara', 'Omsk', 'Rostov-on-Don', 'Krasnoyarsk', 
            'Voronezh', 'Perm', 'Volgograd', 'Krasnodar', 'Saratov', 'Tyumen', 'Togliatti', 'Izhevsk', 'Kaliningrad', 'Ufa']
}
"""dict_cities = {
    'Turkey': ['Istanbul', 'Ankara', 'Izmir', 'Bursa', 'Adana', 'Gaziantep', 'Konya', 'Cankaya', 'Antalya', 'Bagcilar', 'Diyarbakir', 'Kayseri', 'UEskuedar', 'Bahcelievler', 'Umraniye', 'Mersin', 
            'Esenler', 'Eskisehir', 'Karabaglar', 'Muratpasa'],
    'Egypt': ['Cairo', 'Alexandria', 'Giza', 'Port Said', 'Suez', 'Al Mahallah al Kubra', 'Luxor', 'Asyut', 'Al Mansurah', 'Tanda', 'Al Fayyum', 
            'Zagazig', 'Ismailia', 'Kafr ad Dawwar', 'Aswan', 'Qina', 'Halwan', 'Damanhur', 'Al Minya', 'Idku', 'Sohag']
}
dict_cities = {
    'Georgia': ['Tbilisi', 'Batumi', 'Kutaisi', 'Rustavi', 'Gori', 'Zugdidi', 'Poti', 'Kobuleti', 'Khashuri', 'Samtredia', 'Senaki', 'Zestafoni', 'Marneuli', 'Telavi', 'Akhaltsikhe', 'Ozurgeti', 
            'Kaspi', 'Chiatura', 'Tsqaltubo', 'Sagarejo'],
    'Abkhazia': ['Saint-Petersburg', 'Moscow', 'Novosibirsk', 'Ekaterinburg', 'Kazan', 'Nizhniy-Novgorod', 'Chelyabinsk', 'Samara', 'Omsk', 'Rostov-on-Don', 'Krasnoyarsk', 
            'Voronezh', 'Perm', 'Volgograd', 'Krasnodar', 'Saratov', 'Tyumen', 'Togliatti', 'Izhevsk', 'Kaliningrad', 'Ufa']
}
dict_cities = {
    'Italy': ['Rome', 'Milan', 'Naples', 'Turin', 'Palermo', 'Genoa', 'Bologna', 'Florence', 'Bari', 'Catania', 'Venice', 'Verona', 'Messina', 'Padua', 'Trieste', 'Taranto', 
        'Brescia', 'Prato', 'Parma', 'Modena'],
    'Russia': ['Saint-Petersburg', 'Moscow', 'Novosibirsk', 'Ekaterinburg', 'Kazan', 'Nizhniy-Novgorod', 'Chelyabinsk', 'Samara', 'Omsk', 'Rostov-on-Don', 'Krasnoyarsk', 
        'Voronezh', 'Perm', 'Volgograd', 'Krasnodar', 'Saratov', 'Tyumen', 'Togliatti', 'Izhevsk', 'Kaliningrad', 'Ufa']
}
dict_cities = {
    'Italy': ['Rome', 'Milan', 'Naples', 'Turin', 'Palermo', 'Genoa', 'Bologna', 'Florence', 'Bari', 'Catania', 'Venice', 'Verona', 'Messina', 'Padua', 'Trieste', 'Taranto', 
        'Brescia', 'Prato', 'Parma', 'Modena'],
    'Russia': ['Saint-Petersburg', 'Moscow', 'Novosibirsk', 'Ekaterinburg', 'Kazan', 'Nizhniy-Novgorod', 'Chelyabinsk', 'Samara', 'Omsk', 'Rostov-on-Don', 'Krasnoyarsk', 
        'Voronezh', 'Perm', 'Volgograd', 'Krasnodar', 'Saratov', 'Tyumen', 'Togliatti', 'Izhevsk', 'Kaliningrad', 'Ufa']
}
dict_cities = {
    'Italy': ['Rome', 'Milan', 'Naples', 'Turin', 'Palermo', 'Genoa', 'Bologna', 'Florence', 'Bari', 'Catania', 'Venice', 'Verona', 'Messina', 'Padua', 'Trieste', 'Taranto', 
        'Brescia', 'Prato', 'Parma', 'Modena'],
    'Russia': ['Saint-Petersburg', 'Moscow', 'Novosibirsk', 'Ekaterinburg', 'Kazan', 'Nizhniy-Novgorod', 'Chelyabinsk', 'Samara', 'Omsk', 'Rostov-on-Don', 'Krasnoyarsk', 
        'Voronezh', 'Perm', 'Volgograd', 'Krasnodar', 'Saratov', 'Tyumen', 'Togliatti', 'Izhevsk', 'Kaliningrad', 'Ufa']
}
dict_cities = {
    'Italy': ['Rome', 'Milan', 'Naples', 'Turin', 'Palermo', 'Genoa', 'Bologna', 'Florence', 'Bari', 'Catania', 'Venice', 'Verona', 'Messina', 'Padua', 'Trieste', 'Taranto', 
        'Brescia', 'Prato', 'Parma', 'Modena'],
    'Russia': ['Saint-Petersburg', 'Moscow', 'Novosibirsk', 'Ekaterinburg', 'Kazan', 'Nizhniy-Novgorod', 'Chelyabinsk', 'Samara', 'Omsk', 'Rostov-on-Don', 'Krasnoyarsk', 
        'Voronezh', 'Perm', 'Volgograd', 'Krasnodar', 'Saratov', 'Tyumen', 'Togliatti', 'Izhevsk', 'Kaliningrad', 'Ufa']
}
dict_cities = {
    'Italy': ['Rome', 'Milan', 'Naples', 'Turin', 'Palermo', 'Genoa', 'Bologna', 'Florence', 'Bari', 'Catania', 'Venice', 'Verona', 'Messina', 'Padua', 'Trieste', 'Taranto', 
        'Brescia', 'Prato', 'Parma', 'Modena'],
    'Russia': ['Saint-Petersburg', 'Moscow', 'Novosibirsk', 'Ekaterinburg', 'Kazan', 'Nizhniy-Novgorod', 'Chelyabinsk', 'Samara', 'Omsk', 'Rostov-on-Don', 'Krasnoyarsk', 
        'Voronezh', 'Perm', 'Volgograd', 'Krasnodar', 'Saratov', 'Tyumen', 'Togliatti', 'Izhevsk', 'Kaliningrad', 'Ufa']
}"""


"""dict_cities = {
        'Italy': ['Rome', 'Milan', 'Naples', 'Turin', 'Palermo', 'Genoa', 'Bologna', 'Florence', 'Bari', 'Catania', 'Venice', 'Verona', 'Messina', 'Padua', 'Trieste', 'Taranto', 
        'Brescia', 'Prato', 'Parma', 'Modena'],
        'Russia': ['Saint-Petersburg', 'Moscow', 'Novosibirsk', 'Ekaterinburg', 'Kazan', 'Nizhniy-Novgorod', 'Chelyabinsk', 'Samara', 'Omsk', 'Rostov-on-Don', 'Krasnoyarsk', 
        'Voronezh', 'Perm', 'Volgograd', 'Krasnodar', 'Saratov', 'Tyumen', 'Togliatti', 'Izhevsk', 'Kaliningrad', 'Ufa']
}"""