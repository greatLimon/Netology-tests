import pytest
import requests

class TestYDCreateFolder:
    def setup_method(self) -> None:
        from dotenv import load_dotenv
        import os

        load_dotenv('.env')

        TOKEN = os.environ.get('TOKEN')
        self.headers = {
            'Authorization': TOKEN
        }
        self.params = {
            'path': 'TestFolder'
        }

    def __test_YD(self):
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=self.params,
                                headers=self.headers)
        return response.status_code

    def test_create_folder(self):
        result = self.__test_YD()
        if result == 409:
            self.teardown_method()
            result = self.__test_YD()
        assert result == 201
    
    def teardown_method(self):
        response = requests.delete('https://cloud-api.yandex.net/v1/disk/resources',
                                    params=self.params,
                                    headers=self.headers)
        
        
