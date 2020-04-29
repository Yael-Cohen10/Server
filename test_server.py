import requests
import json

def test_post_return_correct_status_code():
    url = 'http://127.0.0.1:5000/AddMessage'
    headers = {'Content-Type': 'application/json'} 
    payload = {
        "application_id":1,
        "session_id": 2,
        "message_id": 3,
        "participants": ["avi aviv", "moshe cohen"],
        "content":"hi!"} 
    resp = requests.post(url, headers=headers, data=json.dumps(payload,indent=4))       
    assert resp.status_code == 200
    assert resp.text=='The message was received'

 
def test_Get_return_correct_status_code():
    post_message()#post message with application_id=1
    url = 'http://127.0.0.1:5000//GetMessage?application_id=1'    
    resp = requests.get(url)           
    assert resp.status_code == 200


def test_Delete_return_correct_status_code():
    post_message() #post message with application_id=1
    url = 'http://127.0.0.1:5000//DeleteMessage?application_id=1'    
    resp = requests.delete(url)           
    assert resp.status_code == 200  



def test_Request_a_message_that_not_found():
    delete_message() #Deletes all messages whose id is equal to 1
    url = 'http://127.0.0.1:5000//GetMessage?application_id=1'    
    resp = requests.get(url)           
    assert resp.status_code == 400
    assert resp.text=='No matching messages found'


def test_Missing_necessary_details(): 
    url = 'http://127.0.0.1:5000/AddMessage'
    headers = {'Content-Type': 'application/json'} 
    payload = {
        #"application_id":"1",
        "session_id": "aaaa",
        "message_id": "bbbb",
        "participants": "[‘avi aviv’, ‘moshe cohen’]",
        "content":"hi!"} 
    resp = requests.post(url, headers=headers, data=json.dumps(payload,indent=4))       
    assert resp.status_code == 400
    assert resp.text=='you need to enter session_id, application_id and message_id'

def test_illegal_type(): 
    url = 'http://127.0.0.1:5000/AddMessage'
    headers = {'Content-Type': 'application/json'} 
    payload = {
        "application_id":"abc", #application_id must be of type integer
        "session_id": "aaaa",
        "message_id": "bbbb",
        "participants": "[‘avi aviv’, ‘moshe cohen’]",
        "content":"hi!"} 
    resp = requests.post(url, headers=headers, data=json.dumps(payload,indent=4))       
    assert resp.status_code == 400
    assert resp.text=='application_id should be Integer'


def test_The_Delete_deletes_all_messages_with_the_required_data():
    post_message()  #post message with application_id=1
    post_message()  #post message with application_id=1
    delete_message()#delete all messages with application_id=1
    url = 'http://127.0.0.1:5000//GetMessage?application_id=1'    
    resp = requests.get(url)           
    assert resp.status_code == 400
    assert resp.text=='No matching messages found'


def post_message():
    url = 'http://127.0.0.1:5000/AddMessage'
    headers = {'Content-Type': 'application/json'} 
    payload = {
        "application_id":1,
        "session_id": "AAA",
        "message_id": "BBB",
        "participants":["avi avi", "moshe cohen"],
        "content":"hello!"
    }
    resp = requests.post(url, headers=headers, data=json.dumps(payload,indent=4)) 
    

def delete_message():
    url = 'http://127.0.0.1:5000//DeleteMessage?application_id=1' 
    resp = requests.delete(url)

def get_message():
    url = 'http://127.0.0.1:5000//GetMessage?application_id=1'    
    resp = requests.get(url)           
    assert resp.status_code == 200

    