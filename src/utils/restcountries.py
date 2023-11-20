import requests

class RestCountriesAPI:
    def __init__(self):
        self.base_url = "https://restcountries.com/v3.1/"

    def _get(self, endpoint):
        response = requests.get(f'{self.base_url}{endpoint}')
        
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def by_name(self, name):
        return self._get(f"name/{name}")

    def by_language(self, language):
        return self._get(f"lang/{language}")

    def get_percentage_population_by_language(self, language):
        data = self.by_language(language)
        
        countries = [{"name":n['name']['common'], "population":n['population']}
         for n in data]

        total_population = sum(country['population'] for country in countries)
        
        for country in countries:
            country['percentage'] = f"{round((country['population'] / total_population) * 100, 4)}%"

        return countries




    