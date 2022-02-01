user_input = None
info_db = []
user_commands = [
    ('add', 'add info in db'), 
    ('show', 'show db list'), 
    ('delete', 'delete an info from db'), 
    ('exit', 'exit the program'), 
    ('help', 'get help for the program')
]

print("Welcome to simple python db! With this program you can add, remove and list your contact info. Type 'help' to see available commands")

#add info to db
def add_info():
    global info_db
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    phone = input('Enter your phone: ')
    info_db.append((name, email, phone))
    print('Thank you! Your information has saved.')

#show available commands
def show_available_commands():
    print('-' * 20)
    for command, command_desc in user_commands:
        print(command + ' - ' + command_desc)
    print('-' * 20)

#show info from db
def show_info_db():
    if not len(info_db):
        print('No info found')
        return
    id = 1
    for name, email, phone in info_db:
        print('-'* 20)
        print(f'Id: {id}\nName: {name}\nEmail: {email}\nPhone: {phone}')
        id += 1

#remove info from db
def remove_info():
    global info_db
    info_id = int(input('Enter info id: '))
    info_db.pop(info_id - 1)
    print(f'Info #{info_id} removed successfully!')

while user_input != 'exit':
    user_input = input('Enter your command: ')
    
    if len(list(filter(lambda command:user_input in command, user_commands))) < 1:
        print("Invalid command! Type 'help' to see available commands")
    if user_input == 'add':
        add_info()
    if user_input == 'show':
        show_info_db()
    if user_input == 'help':
        show_available_commands()
    if user_input == 'delete':
        remove_info()