# airbnb
A api for a replica of airbnb

http://127.0.0.1:3000/api/accounts/users/ - Method = GET - Gets details of all user
http://127.0.0.1:3000/api/accounts/user/{user_id}/ - Method = GET,PATCH,PUT,DELETE - Gets detail of a single user
http://127.0.0.1:3000/api/accounts/user/password/{user_id}/ - Method = PATCH,PUT - Update password of a user
http://127.0.0.1:3000/api/accounts/login/ - Method = POST - Login a user with correct credentials it will give status code 200 and jwt token as reponse
http://127.0.0.1:3000/api/accounts/register/ - Method = POST - Register a user with correct credentials it will give a status code 201
