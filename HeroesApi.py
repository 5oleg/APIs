import requests

heroes = ("Hulk", "Captain America", "Thanos")

heroes_results = []

for hero in heroes:
    result = requests.get(f"https://superheroapi.com/api/2619421814940190/search/{hero}").json()

    if result['response'] != 'error':
        for item in result['results']:
            if item["name"] == hero:
                current = int(item["powerstats"]["intelligence"])
                heroes_results.append((current, item['name']))
                break
    else:
        print(f"Супер-герой {hero} не найден!\n")

heroes_results.sort(reverse=True)

for result in heroes_results:
    value, name = result
    print(f'{name}: {value}')

print(f"\nСамый умный: {heroes_results[0][1]}")
