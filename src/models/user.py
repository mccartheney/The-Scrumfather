from pydantic import BaseModel

# model to register user
class User_register_model (BaseModel) :
  username : str
  password : str

# model to login
class User_login_model (BaseModel) :
  username : str
  password : str
