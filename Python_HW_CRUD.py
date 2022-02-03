
from Py_Create import create_user
from Py_Read import user_info, all_user_info
from Py_Update import update_user
from Py_Delete import delete_user

user_emails = []
user_storage = {}

while True:
    action = input('Please enter [create], or [read_user], or [read_all], or [update], or [delete] or [help] actions: ')

    if action == 'create':                      # ================ create =====================
        print('action =', action)
        email = input('Email: ')
        if email in user_emails:
            print('This Email exists')  # уже есть
        else:
            name = input('Name: ')
            pasword = input('Pasword: ')
            phone = input('Phone: ')
            create_user(email, name, pasword, phone, user_emails, user_storage)

    elif action == 'read_all':                      # ================ read_all =====================
        print('action =', action)
        all_user_info(user_storage)

    elif action == 'read_user':                     # ================ read_user =====================
        print('action =', action)
        user_e = input('Enter user email: ')
        user_info(user_e, user_emails, user_storage)

    elif action == 'update':                    # ================ update =====================
        print('action =', action)
        email = input('Enter user email: ')
        update_user(email, user_emails, user_storage)

    elif action == 'delete':                # ================ delete =====================
        print('action =', action)
        email = input('Enter user email: ')
        delete_user(email, user_emails, user_storage)

    elif action == 'help':                   # ================ help =====================
        print('action =', action)
        print('Actions:\ncreate - create new user\nread_user - read user info\nread_all - read all user info')
        print('update - update user info\ndelete - delete user')
    else:
        print('Сommand not found')

    print('--------------------------------------------------------------------------')