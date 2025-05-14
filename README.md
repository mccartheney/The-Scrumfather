CURL Commands for The Scrumfather API
1. User Registration
Registers a new user by providing a username and password.

curl -X POST "http://127.0.0.1:8000/auth/register" \
-H "Content-Type: application/json" \
-d '{
  "username": "new_user",
  "password": "secure_password"
}'
1 vulnerability
2. User Login
Logs in an existing user and retrieves a JWT token.

curl -X POST "http://127.0.0.1:8000/auth/login" \
-H "Content-Type: application/json" \
-d '{
  "username": "new_user",
  "password": "secure_password"
}'
Response Example:

{
  "access_token": "your_jwt_token_here",
  "token_type": "bearer"
}
3. Create a Project
Creates a new project for the authenticated user.

curl -X POST "http://127.0.0.1:8000/projects/create" \
-H "Authorization: Bearer <your_token>" \
-H "Content-Type: application/json" \
-d '{
  "name": "My New Project",
  "idea": "An app to manage personal finances"
}'
4. Get All Projects
Retrieves all projects belonging to the authenticated user.

curl -X GET "http://127.0.0.1:8000/projects" \
-H "Authorization: Bearer <your_token>"
5. Get Project Details
Retrieves details of a specific project by its ID.

curl -X GET "http://127.0.0.1:8000/projects/<project_id>" \
-H "Authorization: Bearer <your_token>"
Replace <project_id> with the ID of the project you want to retrieve.

6. Delete a Project
Deletes a specific project by its ID.

curl -X DELETE "http://127.0.0.1:8000/projects/<project_id>" \
-H "Authorization: Bearer <your_token>"
Replace <project_id> with the ID of the project you want to delete.

7. Download Project Data
Downloads all data of a specific project as a JSON file.

curl -X GET "http://127.0.0.1:8000/projects/<project_id>/download" \
-H "Authorization: Bearer <your_token>" \
-o project_<project_id>_data.json
Replace <project_id> with the ID of the project. The -o flag saves the JSON file locally.
