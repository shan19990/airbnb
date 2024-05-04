# airbnb<br>
A api for a replica of airbnb<br>

Accounts - <br>
http://127.0.0.1:3000/api/accounts/users/ - Method = GET - Gets details of all user	<br>
http://127.0.0.1:3000/api/accounts/user/{user_id}/ - Method = GET,PATCH,PUT,DELETE - Gets detail of a single user	<br>
http://127.0.0.1:3000/api/accounts/user/password/{user_id}/ - Method = PATCH,PUT - Update password of a user	<br>
http://127.0.0.1:3000/api/accounts/login/ - Method = POST - Login a user with correct credentials it will give status code 200 and jwt token as response	<br>
http://127.0.0.1:3000/api/accounts/register/ - Method = POST - Register a user with correct credentials it will give a status code 201	<be>

Houses - <br>
http://127.0.0.1:3000/api/listings/house/ - Method = GET - Gets details of all houses	<br>
http://127.0.0.1:3000/api/listings/house/add/ - Method = POST - Add a house <br>
http://127.0.0.1:3000/api/listings/house/{house_id}/ - Method = GET,PATCH,PUT,DELETE - Gets detail of a single house	<br>
http://127.0.0.1:3000/api/listings/house/image/add/ - Method = POST - Put images for the house	<br>
http://127.0.0.1:3000/api/listings/house/image/edit/{id}/ - Method = GET,PATCH,PUT,DELETE - Gets detail of a single image for the house <br>
http://127.0.0.1:3000/api/listings/review/add/ - Method = GET - Put reviews for the house	<br>
http://127.0.0.1:3000/api/listings/house/review/edit/{id}/ - Method = GET,PATCH,PUT,DELETE - Gets detail of a single review for the house	<be>

Bookings - <br>
http://127.0.0.1:3000/api/bookings/add/ - Method = POST - Add a booking	<br> 
http://127.0.0.1:3000/api/bookings/find/user/{user_id}/ - Method = GET - fetch all booking details of a user <br>
http://127.0.0.1:3000/api/bookings/find/ - Method = GET,PATCH,PUT,DELETE - Gets detail of a single Booking	<br>
