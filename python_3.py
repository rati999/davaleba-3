import requests

movie_data_cache = {}

def get_name_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['result']['properties']['name']
    return "Name not found"

def get_movie_info(movie_id):
    
    if movie_id in movie_data_cache:
        return movie_data_cache[movie_id]

    url = f'https://www.swapi.tech/api/films/{movie_id}'
    response = requests.get(url)

    if response.status_code == 200:
        movie_data = response.json()['result']['properties']

        characters = [get_name_from_url(character) for character in movie_data['characters']]
        planets = [get_name_from_url(planet) for planet in movie_data['planets']]
        species = [get_name_from_url(specie) for specie in movie_data['species']]

        movie_data['characters'] = characters
        movie_data['planets'] = planets
        movie_data['species'] = species

        movie_data_cache[movie_id] = movie_data

        return movie_data
    else:
        return None

def print_movie_info(movie_info):
    if movie_info:
        print(f"Title: {movie_info['title']}")
        print(f"Episode ID: {movie_info['episode_id']}")
        print(f"Opening Crawl: {movie_info['opening_crawl']}")
        print(f"Director(s): {''.join(movie_info['director'])}")
        print(f"Producer(s): {''.join(movie_info['producer'])}")
        print(f"Release Date: {movie_info['release_date']}")
        
        print("\nCharacters:")
        for character in movie_info['characters']:
            print(f"        *  {character}")

        print("\nPlanets:")
        for planet in movie_info['planets']:
            print(f"        *  {planet}")

        print("\nSpecies:")
        for specie in movie_info['species']:
            print(f"        *  {specie}")

def main():
    while True:
        print("1 - A New Hope")
        print("2 - The Empire Strikes Back")
        print("3 - Return of the Jedi")
        print("4 - The Phantom Menace")
        print("5 - Attack of the Clones")
        print("6 - Revenge of the Sith")
        movie_id = input("Enter film ID to get information about it (in case of any other symbol(s) the program will close): ")
        print("")
        if movie_id.isdigit() and 1 <= int(movie_id) <= 6:
            movie_info = get_movie_info(int(movie_id))
            print_movie_info(movie_info)
        else:
            break 
        print("")

if __name__ == "__main__":
    main()
