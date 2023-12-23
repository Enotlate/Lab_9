import requests
import pytest
import time

payload_1 = {
    "version": "1.0",
    "filter": {
        "fgit": {
            "hasGit": True
        }
    }
}

payload_2 = {
    "version": "1.0",
    "filter": {
        "fgit": {
            "hasGit": False
        }
    }
}

payload_3 = {
    "version": "1.0",
    "filter": {
        "fgit": {
            "hasGit": True
        },
        "fcontact": {
            "hasContact": True
        }
    }
}

payload_4 = {
    "version": "1.0",
    "filter": {
        "fgit": {
            "hasGit": False
        },
        "fcontact": {
            "hasContact": False
        }
    }
}

payload_5 = {
    "version": "1.0",
    "filter": {
        "fgit": {
            "hasGit": True
        },
        "fcontact": {
            "hasContact": False
        }
    }
}

payload_6 = {
    "version": "1.0",
    "filter": {
        "fgit": {
            "hasGit": False
        },
        "fcontact": {
            "hasContact": True
        }
    }
}

BASE_URL = 'http://192.168.0.16:8080/students/general/get-student-list'

def test_hasGit_true():
    start_time = time.time()
    response = requests.post(f'{BASE_URL}', json=payload_1)
    response_body = response.json()
    end_time = time.time()
    assert response.status_code == 200
    for student in response_body["info"]:
        assert student["fgit"]["hasGit"] == True, "Поле git пустое"
    print("test_hasGit_true completed successfully in", end_time-start_time, "seconds")
    print(end_time - start_time)

def test_hasGit_false():
    start_time = time.time()
    response = requests.post(f'{BASE_URL}', json=payload_2)
    response_body = response.json()
    end_time = time.time()
    assert response.status_code == 200
    for student in response_body["info"]:
        assert student["fgit"]["hasGit"] == False, "Поле git не пустое"
    print("test_hasGit_false completed successfully in", end_time-start_time, "seconds")

def test_hasGit_true_and_hasContact_true():
    start_time = time.time()
    response = requests.post(f'{BASE_URL}', json=payload_3)
    response_body = response.json()
    end_time = time.time()
    assert response.status_code == 200
    for student in response_body["info"]:
        assert student["fgit"]["hasGit"] == True, "Поле git пустое"
        assert student["fcontact"]["hasContact"] == True, "Поле контакты пустое"
    print("test_hasGit_true_and_hasContact_true completed successfully in", end_time-start_time, "seconds")

def test_hasGit_false_and_hasContact_false():
    start_time = time.time()
    response = requests.post(f'{BASE_URL}', json=payload_4)
    response_body = response.json()
    end_time = time.time()
    assert response.status_code == 200
    for student in response_body["info"]:
        assert student["fgit"]["hasGit"] == False, "Поле git не пустое"
        assert student["fcontact"]["hasContact"] == False, "Поле контакты не пустое"
    print("test_hasGit_false_and_hasContact_false completed successfully in", end_time-start_time, "seconds")

def test_hasGit_true_and_hasContact_false():
    start_time = time.time()
    response = requests.post(f'{BASE_URL}', json=payload_5)
    response_body = response.json()
    end_time = time.time()
    assert response.status_code == 200
    for student in response_body["info"]:
        assert student["fgit"]["hasGit"] == True, "Поле git пустое"
        assert student["fcontact"]["hasContact"] == False, "Поле контакты не пустое"
    print("test_hasGit_true_and_hasContact_false completed successfully in", end_time-start_time, "seconds")

def test_hasGit_false_and_hasContact_true():
    start_time = time.time()
    response = requests.post(f'{BASE_URL}', json=payload_6)
    response_body = response.json()
    end_time = time.time()
    assert response.status_code == 200
    for student in response_body["info"]:
        assert student["fgit"]["hasGit"] == False, "Поле git не пустое"
        assert student["fcontact"]["hasContact"] == True, "Поле контакты пустое"
    print("test_hasGit_false_and_hasContact_true completed successfully in", end_time-start_time, "seconds")

if __name__ == "__main__":
    pytest.main([__file__])
    test_hasGit_true()
    test_hasGit_false()
    test_hasGit_true_and_hasContact_true()
    test_hasGit_false_and_hasContact_false()
    test_hasGit_true_and_hasContact_false()
    test_hasGit_false_and_hasContact_true()