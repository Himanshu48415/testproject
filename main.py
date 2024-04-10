import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.db1.user import User,Base
from settings import MYSQL_URL_1,MYSQL_URL_2 ,LOG_FILE_PATH_1,LOG_FILE_PATH_2

engine_1 = create_engine(MYSQL_URL_1)
engine_2 = create_engine(MYSQL_URL_2)

# Base.metadata.create_all(bind=engine_1)
# Base.metadata.create_all(bind=engine_2)
session_object = sessionmaker(bind=engine_1)
#current running engine 
current_engine = engine_1
#log file selection logic
if current_engine == engine_1:
    LOG_FILE_PATH = LOG_FILE_PATH_1
elif(current_engine == engine_2):
    LOG_FILE_PATH = LOG_FILE_PATH_2

logging.basicConfig(level=logging.INFO , filename= LOG_FILE_PATH, filemode="a",
format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(lineno)s - %(message)s ', datefmt='%m/%d/%Y %I:%M:%S %p') 
logger = logging.getLogger(__name__)

def add_user(name, email):
    session = session_object()
    existing_user_name = get_user_by_name(name)
    if existing_user_name:
        logging.error(f"Error: User with name '{name}' already exists.")
        return
    
    existing_user_email = get_user_by_email(email)
    if existing_user_email:
        logging.error(f"Error: User with email '{email}' already exists.")
        return

    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    logging.info(f"User '{name}' added successfully.")


def get_user_by_name(name):
    try:
        session = session_object()
        user = session.query(User).filter_by(name=name).first()
        if user:
            logging.info(f"Retrieved user by name: Name='{name}', Email='{user.email}'")
        else:
            logging.warning(f"User with name '{name}' not found")
        return user
    except Exception as e:
        logging.error(f"An error occurred while retrieving user by name '{name}': {e}")
        return None


def get_user_by_email(email):
    try:
        session = session_object()
        user = session.query(User).filter_by(email=email).first()
        if user:
            logging.info(f"Retrieved user by email: Name='{user.name}', Email='{email}'")
        else:
            logging.warning(f"User with email '{email}' not found")
        return user
    except Exception as e:
        logging.error(f"An error occurred while retrieving user by email '{email}': {e}")
        return None

def update_user_email(name, new_email):
    try:
        session = session_object()
        user = session.query(User).filter_by(name=name).first()
        if user:
            user.email = new_email
            session.commit()
            logging.info(f"Updated user email: Name='{name}', New Email='{new_email}'")
        else:
            logging.warning(f"User with name '{name}' not found")
    except Exception as e:
        logging.error(f"An error occurred while updating user email for '{name}': {e}")

def upsert_user(name, email):
    try:
        session = session_object()
        user = session.query(User).filter_by(name=name).first()
        if user:
            user.email = email
            logging.info(f"Already Existing User: {user.name}")
        else:
            new_user = User(name=name, email=email)
            session.add(new_user)
            session.commit()
            logging.info(f"Created new user: Name='{name}', Email='{email}'")
    except Exception as e:
        logging.error(f"An error occurred during upsert for user '{name}': {e}")


if __name__ == "__main__":
    add_user("Mukesh", "mukesh1@example.com")
    user = get_user_by_email("mukesh@example.com")
    if user:
        print(f"Found user: {user.name}, Email: {user.email}")
    # update_user_email("Krishna", "krishna.new@example.com")
    # print(f'Updated email: {user.email}')
