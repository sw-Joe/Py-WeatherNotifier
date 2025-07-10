# from auth import issue_token, request_auth_code
# from io_func import j_read
# from send_msg import send_message
from value import PATH_TOKEN


# request_auth_code()

# issue_token(j_read(PATH_TOKEN, "authorization_code"))

# print(send_message(j_read(PATH_TOKEN, "access_token")))


from io_mock import IO, read, write


io = IO(PATH_TOKEN)

read_val = io.file_scan(read("authorization_code"))

print(read_val)
