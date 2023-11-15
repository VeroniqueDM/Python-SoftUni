import json
USERS_FILE_PATH = './db/users.txt'
SESSION_PATH = './db/current_user.txt'
def register(username, email, password):
    user_object = {
        'username': username,
        'email': email,
        'password': password,
        'products': [],
    }
    user_json = json.dumps(user_object)
    with open(USERS_FILE_PATH, 'r+') as file:
        for user_line in file:
            existing_user = json.loads(user_line.strip())
            if existing_user['username'] == username:
                return False
        file.write(user_json + '\n')
        return True

def login_user(username, password):
    # user_object = {
    #     'username': username,
    #     'password': password,
    # }
    # user_json = json.dumps(user_object)
    with open(USERS_FILE_PATH, 'r') as file, open(SESSION_PATH, 'w') as session_file:
        for user_line in file:
            existing_user = json.loads(user_line.strip())
            if existing_user['username'] == username and existing_user['password'] == password:
                session_file.write(username)
                return True
        return False


def get_current_user():
    with open(SESSION_PATH, 'r') as file:
        return file.read().strip()
