import requests


def test_user_api_docker_connection():
    usr_dict = requests.get("http://user_api:5000/user").json()
    assert usr_dict 
    
def test_docker_api():
    usr_dict = requests.get("http://user_api:5000/user").json()
    assert len(usr_dict) == 6
 