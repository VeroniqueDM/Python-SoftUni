import json

from auth_service import get_current_user

PRODUCTS_FILE = './db/products.txt'
def get_all_products():
    with open(PRODUCTS_FILE, 'r') as file:
        return [json.loads(x.strip()) for x in file]
        # for product_line in file:
        #     product = json.loads(product_line.strip())

def buy_product(product_id):
    with open(PRODUCTS_FILE, 'r+') as product_file:
        result = []
        for product_line in product_file:
            current_product = json.loads(product_line.strip())
            if current_product['id'] == product_id:
                current_product['count'] -= 1
                result.append(json.dumps(current_product) + '\n')
            else:
                result.append(product_line)

        product_file.seek(0)
        product_file.truncate()
        product_file.writelines(result)
