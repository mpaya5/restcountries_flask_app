# RestCountries FastAPI APP

## Setup

Create a `.env` file and define those parametrs:
```
MYSQL_DATABASE=
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_ROOT_PASSWORD=
ADMIN_PASS=
```

Save the `ADMIN_PASS` carefully because you will need to be able to generate tokens jwt to interact with the platform. 


## TEST

For testing the routes you can use this class:
```
import requests

class MakeRequest:
    def __init__(self):
        self.base_url = "http://127.0.0.1:8080"

    def _post(self, endpoint, data, headers=None):
        headers = {} if headers is None else headers

        response = requests.post(
            url=f'{self.base_url}{endpoint}',
            json=data,
            headers = headers
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.status_code, "message": response.text}


    def _get(self, endpoint, headers=None):
        headers = {} if headers is None else headers

        response = requests.get(
            url=f'{self.base_url}{endpoint}',
            headers = headers
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.status_code, "message": response.text}


    def _delete(self, endpoint, headers=None):
        headers = {} if headers is None else headers    

        response = requests.delete(
            url=f'{self.base_url}{endpoint}',
            headers = headers
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.status_code, "message": response.text}

    
    def _put(self, endpoint, data, headers=None):
        headers = {} if headers is None else headers

        response = requests.put(
            url=f'{self.base_url}{endpoint}',
            json=data,
            headers=headers
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.status_code, "message": response.text}
```