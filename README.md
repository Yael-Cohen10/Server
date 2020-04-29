By Yael Cohen
id: 207485483‏
Server Using Flask Implementation
The program implements server using “flask” microframework.
The server includes the following API’s:
POST:
Receives a json message from the user and saves the message on the server side - in a database (using sqlite). Post is done by 'AddMessage', The message contains application id, session id, message id, participants list and content, in the following json format: 
{
        application_id: {application id}
        session_id: {unique session id}
        message_id: {unique message id}
        participants: [list of participant names]
        content: {message}
} 
GET:
Returns data from the server side (that is stored in sqlite database) in a json format, according to the url parameters, which should be one of the following: 
•	Application id = x : 
•	Session id = x
•	Message id = x
The program will return the filtered data that corresponds to the requested parameters. Get is done by 'GetMessage'.
Get request for example: http://127.0.0.1:5000//GetMessage?application_id=2

DELETE:
deletes certain messages according to the requested id from the server side according to the url parameters, which should be one of the following: 
•	Application id = x : 
•	Session id = x
•	Message id = x
Delete request for example: http://127.0.0.1:5000//DeleteMessage?application_id=5

