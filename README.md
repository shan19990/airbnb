# airbnb<br>
A api for a replica of airbnb<br>

Accounts -
http://127.0.0.1:3000/api/accounts/users/ - Method = GET - Gets details of all user	<br>
http://127.0.0.1:3000/api/accounts/user/{user_id}/ - Method = GET,PATCH,PUT,DELETE - Gets detail of a single user	<br>
http://127.0.0.1:3000/api/accounts/user/password/{user_id}/ - Method = PATCH,PUT - Update password of a user	<br>
http://127.0.0.1:3000/api/accounts/login/ - Method = POST - Login a user with correct credentials it will give status code 200 and jwt token as response	<br>
http://127.0.0.1:3000/api/accounts/register/ - Method = POST - Register a user with correct credentials it will give a status code 201	<be>

Houses -
http://127.0.0.1:3000/api/listings/house/ - Method = GET - Gets details of all houses	<br>
http://127.0.0.1:3000/api/listings/house/add/ - Method = POST - Add a house 	<br>
http://127.0.0.1:3000/api/accounts/listings/house/{house_id}/ - Method = GET,PATCH,PUT,DELETE - Gets detail of a single house	<br>


path('house/', HouseListView.as_view(), name="houses"),
path('house/add/', HouseCreateView.as_view(), name="addhouse"),
path('house/<int:id>/', HouseDetailView.as_view(), name="edithouse"),
