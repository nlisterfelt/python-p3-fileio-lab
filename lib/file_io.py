def write_file(file_name, file_content):
    new_name=str(file_name)+'.txt'
    with open(new_name, mode='w', encoding='utf-8') as text_file:
        text_file.write(file_content)

def append_file(file_name, append_content):
    new_name=str(file_name)+'.txt'
    with open(new_name, mode='a', encoding='utf-8') as text_file:
        text_file.write(append_content)

def read_file(file_name):
    new_name=str(file_name)+'.txt'
    with open(new_name, encoding='utf-8') as text_file:
        return text_file.read()
