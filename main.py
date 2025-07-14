from auth import issue_token, request_auth_code
from io_func import read_json
# from send_msg import send_message
from value import PATH_TOKEN



def main():
    request_auth_code()
    # issue_token(read_json(PATH_TOKEN, "authorization_code"))
    # print(send_message(j_read(PATH_TOKEN, "access_token")))


if __name__ == "__main__":
    main()