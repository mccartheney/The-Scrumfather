from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

# necessary thing to construct token
SECRET_KEY = "5ac33eeff0dbcdc4831e30cccc99bdf8a36ef79f5b9edefeff6ae61d700d8656"
ALGORITHM = "HS256"
expire_time_minutes = 1
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# function to hash the password
def hash_password(password):
    return pwd_context.hash(password)

# function to hash password
def verify_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)

# funtion to create token
def create_token(data: dict):
    copie = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expire_time_minutes)
    copie.update({"exp": expire})
    return jwt.encode(copie, SECRET_KEY, algorithm=ALGORITHM)


# function to verify token
def verify_token(token: str):
    try:
        # uncrypt the token, get and return username
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise JWTError()
        return username
    except JWTError:
        return None
