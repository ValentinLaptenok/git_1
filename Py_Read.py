
def user_info(email, user_emails, user_storage):

    if email in user_emails:
        print('User_info:', user_storage[email])
    else:
        print('No user with email:', email)


def all_user_info(user_storage):
    for k, v in user_storage.items():
        user_email = 'User email: ' + k
        user_info_1 = 'User info: ', v
        print(user_email, '\n', user_info_1)