def generate_template(name, age):
    return f'Name: {name}, Age: {age}'

def generate_template_html(name,age):
    return '''
    <h1>{name}</h1>
    <h2>{age}</h2>
    '''