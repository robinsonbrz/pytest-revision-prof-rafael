import pytest
import requests


ENDPOINT = "https://todo.pixegami.io/"

'''
Baseado no tutorial
https://www.youtube.com/watch?v=7dgQRVqF1N0

Swagger
https://todo.pixegami.io/docs/


'''

response = requests.get(ENDPOINT)
print(response)

data = response.json()
print(data)

status_code = response.status_code
print(status_code)

def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_can_create_task():
    payload = new_task_payload()
    create_task_response = requests.put(ENDPOINT + "/create-task", json=payload)
    assert create_task_response.status_code == 200
    data = create_task_response.json()

    task_id = data["task"]["task_id"]
    get_task_response = requests.get(ENDPOINT + f"/get-task/{task_id}")

    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert payload["content"] == get_task_data["content"]
    assert payload["user_id"] == get_task_data["user_id"]

    # delete created teask test
    delete_task(task_id)



def test_can_update_task():
    '''
    create a task
    update the task
    get and validate the changes
    '''
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]

    # update the task
    new_payload = {
        "user_id": payload["user_id"],
        "task_id": task_id,
        "content": "my updated content",
        "is_done": True,
    }
    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200

    # get task and validate the changes
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["is_done"] == new_payload["is_done"]

    # delete created teask test
    delete_task(task_id)

    
def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)

def get_task(task_id):
    response = requests.get(ENDPOINT + f"/get-task/{task_id}")
    print(f"\n\nMethod get_task: {response.json()}")
    return response

def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)


def new_task_payload():
    return {
        "content": "my test content",
        "user_id": "test_user_rob2",
        "task_id": "test_task_id",
        "is_done": False
    }

@pytest.mark.rob
def test_can_list_tasks():
    '''create N tasks'''
    number_of_tasks = 3
    for _ in range(number_of_tasks):
        payload = new_task_payload()
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200

    # list tasks, and check that there are N items
    list_tasks_response = list_tasks("test_user_rob2")
    assert list_tasks_response.status_code == 200
    data = list_tasks_response.json()

    assert len(data["tasks"]) == number_of_tasks

    # Dont leave test data in the database
    # Delete created data after the test
    for i in data["tasks"]:
        delete_task(i["task_id"])

def test_can_delete_task():
    # Create the task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    created_task = create_task_response.json()
    print(created_task["task"]["task_id"])
    task_id = created_task["task"]["task_id"]
    assert create_task_response.status_code == 200

    # get_task - Confirm creation of the task
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200

    # delete
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200
    deleted_data = delete_task_response.json()
    assert task_id == deleted_data["deleted_task_id"]


    # get_task - Confirm creation of the task
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404
    get_task_data = get_task_response.json()
    assert f"Task {task_id} not found" == get_task_data["detail"]

def delete_task(task_id):
    return requests.delete(ENDPOINT + f"/delete-task/{task_id}")

def list_tasks(user_id):
    return requests.get(ENDPOINT + f"/list-tasks/{user_id}")




