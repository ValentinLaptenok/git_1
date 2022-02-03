
def delete_user(email, user_emails, user_storage):
    if email in user_emails:
        del user_storage[email]
        user_emails.remove(email)
        print('Delete user', email)
    else:
        print('No user with email:', email)
