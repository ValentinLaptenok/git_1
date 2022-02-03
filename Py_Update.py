
def update_user(email, user_emails, user_storage):
    if email in user_emails:
        print('Old user_info:', user_storage[email], '\nEnter new user_info:')
        name = input('New name: ')
        pasword = input('New pasword: ')
        phone = input('New phone: ')
        user_storage[email] = {
            'name': name,
            'password': pasword,
            'phone': phone
        }
        print('New user_info: Email', email, 'Storage', user_storage[email])
    else:
        print('No user with email:', email)


