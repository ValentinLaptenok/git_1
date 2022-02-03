
def create_user(email, name, pasword, phone, user_emails, user_storage):
    user_info = [email, name, pasword, phone]
    user_emails.append(email)
    user_storage[email] = {
        'name':name,
        'password':pasword,
        'phone':phone
    }
    print('create_user_f =', user_info)
