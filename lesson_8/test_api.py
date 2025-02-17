import requests

base_url = "https://yougile.com"

## Авторизация
my_login = 'olga27.skypro@gmail.com'
my_password = 'Olga27sky'

# Получить список компаний
def test_auth():
    creds = {
        'login': my_login,
        'password': my_password
    }
    resp = requests.post(base_url + '/api-v2/auth/companies', json=creds)
    response_body = resp.json()["content"][0]
    first_company = response_body["id"]
    assert resp.status_code == 200
    assert len(response_body) > 0
    return first_company

# Создать ключ
def test_key():
     creds = {
        'login': my_login,
        'password': my_password,
        'companyId': test_auth()
     }
     resp = requests.post(base_url + '/api-v2/auth/keys', json=creds)
     response_body = resp.json()["key"]
     assert resp.status_code == 201
     return response_body

# получить токен 
def test_token():
    my_token = {
        'Authorization': ("Bearer " + test_key())
    }
    return my_token

# Получить ИД сотрудника
def test_ID_worker():
     resp = requests.get(base_url+'/api-v2/users', headers=test_token())
     response_body = resp.json()["content"][0]
     worker = response_body["id"]
     assert resp.status_code == 200
     return worker

## Позитивные проверки
# Получить список проектов (надо исп полученный ключ в запросе)
def test_get_project():
    resp = requests.get(base_url+'/api-v2/projects', headers=test_token())
    assert resp.status_code == 200

# создать проект (надо получить ид сотрудника) 
def test_new_project():
    project = {
        "title": "Новый проект",
        "users": {
             test_ID_worker(): "admin"
        }
    }
    resp = requests.post(base_url+'/api-v2/projects', json=project, headers=test_token())
    response_body = resp.json()["id"]
    assert resp.status_code == 201
    return response_body

# Получить по ID проект
def test_id_project():
    id_project = test_new_project()
    resp = requests.get(base_url+'/api-v2/projects/'+id_project, headers=test_token())
    response_body = resp.json()["id"]
    assert id_project == response_body
    assert resp.status_code == 200

# изменить проект 
def test_change_project():
    id_project = test_new_project()
    creds = {
        "title": "Очень новый проект"
        }
    resp = requests.put(base_url+'/api-v2/projects/'+id_project, json=creds, headers=test_token())
    assert resp.status_code == 200


## Негативные проверки
# Получить список проектов без авторизации
def test_noget_project():
    resp = requests.get(base_url+'/api-v2/projects')
    assert resp.status_code == 401

# создать проект без ИД сотрудника
def test_nonew_project():
    project = {
        "title": "Новый проект",
        "users": {
             test_ID_worker(): ""
        }
    }
    resp = requests.post(base_url+'/api-v2/projects', json=project, headers=test_token())
    assert resp.status_code == 400

# Получить проект по несуществующему ID 
def test_noid_project():
    resp = requests.get(base_url+'/api-v2/projects/'+"4567899", headers=test_token())
    assert resp.status_code == 404

# изменить не существующий проект 
def test_nochange_project():
    creds = {
        "title": "Очень новый проект"
        }
    resp = requests.put(base_url+'/api-v2/projects/'+"4567899", json=creds, headers=test_token())
    assert resp.status_code == 404