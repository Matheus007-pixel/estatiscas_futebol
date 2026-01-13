import requests

class FootballAPI:
    def __init__(self,api_key):
        self.base_url = "https://v3.football.api-sports.io"
        self.headers = {
            "x-apisports-key": api_key
        }

    def buscar_escudo_time(self,nome_time):
        url = f"{self.base_url}/teams"
        params = {
            "search": nome_time
        }
        response = requests.get(url, headers=self.headers,params=params)

        if response.status_code !=200:
            return None

        data = response.json()

        if data.get("response"):
            return data["response"][0]["team"]["logo"]

        return None