import json

from auth_service import get_current_user

USERS_PATH = './db/users.txt'

def purchase_product(product_id):
    with open(USERS_PATH, 'r+') as file:
        result = []
        current_username = get_current_user()
        for user_line in file:
            user_obj = json.loads(user_line.strip())
            if user_obj['username'] == current_username:
                user_obj['products'].append(product_id)
                result.append(json.dumps(user_obj) + '\n')
            else:
                result.append(user_line)
        file.seek(0)
        file.truncate()
        file.writelines(result)