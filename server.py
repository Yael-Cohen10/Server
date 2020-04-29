from flask import Flask, jsonify, request,Response
from db import *
import json


app = Flask(__name__)

'''function AddMessage: POST
the function Receives a json message from the user
and saves the message on the server side '''

@app.route('/AddMessage',methods=['post'])
def AddMessage():
    data=request.get_json()

    #Check for all necessary details:
    if "session_id" in data and "application_id" in data and "message_id" in data: 
        application_id = data['application_id']
        if type(application_id) != int:
            return Response('application_id should be Integer',status=400, mimetype='application/json')
        session_id = data['session_id']
        message_id = data['message_id']
        if "participants" in data:
            participants = data['participants']
        else:
            participants = "none"  
        if "content" in data:
            content = data['content']
        else:
            content = "none"
        participantsList = ','.join(participants)
        insert(application_id,session_id,message_id,participantsList,content)
        return 'The message was received'

    #Warns of error if missing details are needed:    
    else:
        return Response('you need to enter session_id, application_id and message_id',status=400, mimetype='application/json')    


'''function GetMessage: GET
the function returns data from the database 
in a json format, according to the url parameters '''

@app.route('/GetMessage', methods=['GET'])
def GetMessage():

    if "application_id" in request.args:
        application=request.args["application_id"]
        The_message=read_from_db('application_id',application)
        return messages_if_found(The_message)
      
    elif "session_id" in request.args: 
        session=request.args["session_id"] 
        The_message=read_from_db('session_id',str(session))
        return messages_if_found(The_message)

    elif "message_id" in request.args: 
        messages=request.args["message_id"] 
        The_message=read_from_db('message_id',messages)
        return messages_if_found(The_message)
             
    else:
       return Response('you need to enter session_id, application_id or message_id',status=400, mimetype='application/json')    
        

'''function DeleteMessage: DELETE
the function deletes certain messages 
according to the requested id ''' 

@app.route('/DeleteMessage', methods=['DELETE'])
def DeleteMessage():

    if "application_id" in request.args:
        application=request.args["application_id"]
        delete_from_db('application_id',application)
        return 'Message deleted' 

    elif "session_id" in request.args: 
        session=request.args["session_id"] 
        delete_from_db('session_id',session)
        return 'Message deleted'

    elif "message_id" in request.args: 
        messages=request.args["message_id"] 
        delete_from_db('message_id',messages)
        return 'Message deleted'   

    else:
        return Response('you need to enter session_id, application_id or message_id',status=400, mimetype='application/json')    
         
    
def messages_if_found(The_message):
    if not The_message:
        return no_messages()
    else:
        return as_json(The_message)

def as_json(data):
    resp = Response(status=400, mimetype='application/json') 
    print("data is", data[0][0])
    list_msg = []
    for msg in data:
        list_msg.append({"application_id":msg[0], 'session_id': msg[1],'message_id':msg[2], "participants":msg[3].split(','),"content":msg[4]})
    return jsonify(list_msg)

def no_messages():
    return Response('No matching messages found',status=400, mimetype='application/json')

if __name__ == "__main__":
    creaet_db()
    app.run() 