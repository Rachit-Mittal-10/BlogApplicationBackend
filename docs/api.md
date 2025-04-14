# APIs

1. POST /api/auth/register: This would register the user and create the user instance in user model in db
Body Parameters:
- username
- password
- first_name
- last_name
- phone_number
- bio
- profile_picture
- email
Returns:
- 200 and message would be "User created successfully"

2. POST /api/auth/login: This would login the user to get the access tokens.
Body Parameters:
- username
- password
Returns:
- 404 if user is not authenticated
- 200 if users is authenticated with access and refresh tokens

3. POST /api/auth/refresh: This would get the access token based on refresh token.
Body Parameters:
- refresh_token
Returns:
- access_token with status code 200
- if refresh token is expired then 404.

4. GET /api/users: This would returns all the users in the db.
Parameters: None
Returns:
- list of users with status code 200

5. GET /api/users/{userId}: This would return the user details based on the user Id.
Query Parameters:
- userId
Returns:
- user details

6. PUT /api/users/{userId}: This will update the user detail of particular user id.
Query Parameters:
- userId
Returns:

7. PATCH /api/users/{userId}: This will partially update the user detail of particular user id.

8. DELETE /api/users/{userId}: This will delete the user details of particular user id.

9. POST /api/roles: This will create the role.

10. GET /api/roles: This will get all the roles.

11. GET /api/roles/{rolesId}: This will get the role with particular role id.

12. PUT /api/roles/{rolesId}: This will update the role with particular role id.

13. PATCH /api/roles/{rolesId}: This will partially update the role with particular role id.

14. DELETE /api/roles/{rolesId}: This will delete the role with particular role id.

15. POST /api/users/{authorId}/blogs: This will create the new blog linked to user and this will give the role of author to user.

16. GET /api/users/{authorId}/blogs: This will get all the blogs linked to user where he is author.

17. GET /api/users/{authorId}/blogs/{blogId}: This will get the particular blog linked to user.

18. PUT /api/users/{authorId}/blogs/{blogId}: This will be used to update the particular blog linked to user.

19. PATCH /api/users/{authorId}/blogs/{blogId}: This will be used to partially update the particular blog linked to user.

20. DELETE /api/users/{authorId}/blogs/{blogId}: This will be used to delete the particular blog linked to user.

21. GET /api/blogs/{blogId}/members: This will list all the members(authors, co-authors, editors etc) with particular blog.

22. POST /api/blogs/{blogId}/members: This will add the contributor with userId to blog id.
Parameters:
- userId
- roleId

23. PUT /api/blogs/{blogId}/members: This will update the role of user.

24. DELETE /api/blogs/{blogId}/members/users/{userId}: This will delete the user associated with blog. A User cannot delete himself. Only Author can delete the users from blogs.
