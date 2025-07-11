import requests

def test_add():
    res = requests.get("http://127.0.0.1:5001/add?a=1&b=2")
    print(res.json())
    assert res.status_code == 200
    assert res.json()['result'] == 3
