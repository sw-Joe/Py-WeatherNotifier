# import logging as log

from auth import issue_token, request_auth_code
from io_func import Path
import logconfig
# from send_msg import send_message
from value import PATH_TOKEN



def main():
    request_auth_code()
    # f_token: Path = Path(PATH_TOKEN)
    # issue_token(f_token.search_json("authorization_code"))
    # log.debug(send_message(f_token.search_json("access_token")))


if __name__ == "__main__":
    main()