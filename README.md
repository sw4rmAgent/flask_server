# flask_server
simple flask server handling HTTP requests from client

## Install
- clone this repo :
```
git clone https://github.com/sw4rmAgent/flask_server.git
```
- copy/paste files in your server (i.e. pythonanywhere) and make sure it is running :
	* Make an account or sign in @ www.eu.pythonanywhere.com
	* Once signed in, from the top-right menu go to Files -> mysite folder
	* In this folder, create copies of http_req_app.py and database.json (both from this repo).
	* Go to Files -> mysite -> templates and copy/paste all the files from of this repo's template folder to yours
	* Go back to the home page www.eu.pythonanywhere.com. Then in the dashboard menu -> Web -> click the reload green button
- test requests using Postman

## Tools
- verify validity of JSON files @ https://jsonformatter.curiousconcept.com/

## Clarifications

![Server-to-Client Framework](http://github.com/sw4rmAgent/flask_server/img/client-server-framework.png)

### DFN class
Data Fusion Nodes (DFNs) are responsible for fusing the data from multiple sensors on the server. They can be created, deleted, or modified by the user via HTTP requests, which should preferably require an authentication header (to be discussed). Here below are the requests responsible of instanciating/deleting the DFN objects, or modify their setup :

#### HTTP request to create DFN
Below, the variables of each DFN that are setup via an HTTP request :
- input variables : [file_name (str), client_name (str), var_name(str)]
- output variables : [file_name (str), output_var_name (str), output_value (float)]
- operation : "a**2+b/3" (str)
- frequency : 3600 (float)

#### HTTP request to delete DFN
This request will delete the DFN to free server CPU time
- delete : True/False (bool)

#### HTTP request to modify DFN parameters
This section depends on the level of interoperability between the user and the DFNs (to be discussed). Modify inputs/outputs/operation/frequency of the DFN all at once or separately (if only one field is filled in the request).

