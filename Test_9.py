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

payload_7 = {
    "version": "1.0",
    "filter": {
        "fgit": {
            "hasGit": True
        }
    },
    "pagination" : {
        "count" : 20,
        "number" : 1,
        "random" : "false",
        "sort" : "lastname",
        "orderDesc": "false"
        }
}

payload_8 = {
    "version": "1.0",
        "filter": {
            "fgit": {
                "hasGit": False
        }
    },
    "pagination" : {
        "count" : 20,
        "number" : 1,
        "random" : "false",
        "sort" : "lastname",
        "orderDesc": "false"
        }
}

payload_9 = {
    "version": "1.0",
    "filter": {
        "fgit": {
            "hasGit": True
        },
        "fcontact": {
            "hasContact": True
        }
    },
        "pagination" : {
            "count" : 20,
            "number" : 1,
            "random" : "false",
            "sort" : "lastname",
            "orderDesc": "false"
        }
}

payload_10 = {
    "version": "1.0",
    "filter": {
        "fgit": {
            "hasGit": False
        },
        "fcontact": {
            "hasContact": False
        }
    },
        "pagination" : {
            "count" : 20,
            "number" : 1,
            "random" : "false",
            "sort" : "lastname",
            "orderDesc": "false"
        }
}

payload_11 = {
    "version": "1.0",
    "filter": {
        "fgit": {
            "hasGit": True
        },
        "fcontact": {
            "hasContact": False
        }
    },
        "pagination" : {
            "count" : 20,
            "number" : 1,
            "random" : "false",
            "sort" : "lastname",
            "orderDesc": "false"
        }
}

payload_12 = {
    "version": "1.0",
    "filter": {
        "fgit": {
            "hasGit": False
        },
        "fcontact": {
            "hasContact": True
        }
    },
        "pagination" : {
            "count" : 20,
            "number" : 1,
            "random" : "false",
            "sort" : "lastname",
            "orderDesc": "false"
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

def test_hasGit_true_pagination():
    start_time = time.time()
    response = requests.post(f'{BASE_URL}', json=payload_7)
    response_body = response.json()
    end_time = time.time()
    assert response.status_code == 200
    for student in response_body["info"]:
        assert student["fgit"]["hasGit"] == True, "Поле git пустое"
    print("test_hasGit_true_pagination completed successfully in", end_time-start_time, "seconds")

def test_hasGit_false_pagination():
    start_time = time.time()
    response = requests.post(f'{BASE_URL}', json=payload_8)
    response_body = response.json()
    end_time = time.time()
    assert response.status_code == 200
    for student in response_body["info"]:
        assert student["fgit"]["hasGit"] == False, "Поле git не пустое"
    print("test_hasGit_false_pagination completed successfully in", end_time-start_time, "seconds")

def test_hasGit_true_and_hasContact_true_pagination():
    start_time = time.time()
    response = requests.post(f'{BASE_URL}', json=payload_9)
    response_body = response.json()
    end_time = time.time()
    assert response.status_code == 200
    for student in response_body["info"]:
        assert student["fgit"]["hasGit"] == True, "Поле git пустое"
        assert student["fcontact"]["hasContact"] == True, "Поле контакты пустое"
    print("test_hasGit_true_and_hasContact_true_pagination completed successfully in", end_time-start_time, "seconds")

def test_hasGit_false_and_hasContact_false_pagination():
    start_time = time.time()
    response = requests.post(f'{BASE_URL}', json=payload_10)
    response_body = response.json()
    end_time = time.time()
    assert response.status_code == 200
    for student in response_body["info"]:
        assert student["fgit"]["hasGit"] == False, "Поле git не пустое"
        assert student["fcontact"]["hasContact"] == False, "Поле контакты не пустое"
    print("test_hasGit_false_and_hasContact_false_pagination completed successfully in", end_time-start_time, "seconds")

def test_hasGit_true_and_hasContact_false_pagination():
    start_time = time.time()
    response = requests.post(f'{BASE_URL}', json=payload_11)
    response_body = response.json()
    end_time = time.time()
    assert response.status_code == 200
    for student in response_body["info"]:
        assert student["fgit"]["hasGit"] == True, "Поле git пустое"
        assert student["fcontact"]["hasContact"] == False, "Поле контакты не пустое"
    print("test_hasGit_true_and_hasContact_false_pagination completed successfully in", end_time-start_time, "seconds")

def test_hasGit_false_and_hasContact_true_pagination():
    start_time = time.time()
    response = requests.post(f'{BASE_URL}', json=payload_12)
    response_body = response.json()
    end_time = time.time()
    assert response.status_code == 200
    for student in response_body["info"]:
        assert student["fgit"]["hasGit"] == False, "Поле git не пустое"
        assert student["fcontact"]["hasContact"] == True, "Поле контакты пустое"
    print("test_hasGit_false_and_hasContact_true_pagination completed successfully in", end_time-start_time, "seconds")


if __name__ == "__main__":
    pytest.main([__file__])
    test_hasGit_true()
    test_hasGit_false()
    test_hasGit_true_and_hasContact_true()
    test_hasGit_false_and_hasContact_false()
    test_hasGit_true_and_hasContact_false()
    test_hasGit_false_and_hasContact_true()
    test_hasGit_true_pagination()
    test_hasGit_false_pagination()
    test_hasGit_true_and_hasContact_true_pagination()
    test_hasGit_false_and_hasContact_false_pagination()
    test_hasGit_true_and_hasContact_false_pagination()
    test_hasGit_false_and_hasContact_true_pagination()
