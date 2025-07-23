import json



class Path:
    def __init__(self, path):
        self.path = path
        # 파일 경로로 하여금 Path 객체를 생성하면 일단 읽기모드로 파일을 열어 전체를 읽는다.
        self.r_mode = open(self.path, "r")
        self.json_parse = json.load(self.r_mode)


    def search_json(self, keyword: str) -> str:
        """
        JSON 파일에서 원하는 값을 찾기
        @params:
            keyword : str - json 파일에서 검색할 value의 key값에 해당하는 문자열
        @return
            :str - params keyword(json key)값에 맞는 값
        """

        finding: str = self.json_parse[keyword]
        self.r_mode.close()
        return finding


    def write_jsons(self, keyword: str, value: str) -> None:
        """
        JSON 파일 쓰기
        @params:
            keyword : str - 파일에서 찾을 value의 key값에 해당하는 문자열
            value   : str - 수정할 내용의 문자열
        @return:
            None
        """

        # 데이터 수정
        self.json_parse[keyword] = value
        self.r_mode.close()

        # 기존 파일 덮어쓰기
        with open(self.path, "w", encoding="utf-8") as w_mode:
            json.dump(self.json_parse, w_mode, indent="\t")

'''
# test code
if __name__ == "__main__":
    PATH_TEST = "./plaintext/test.json"
    f: Path = Path(PATH_TEST)
    f.write_jsons("authorization_code", "test_value_this_is_authcode")
    print(f.search_json("authorization_code"))
'''


"""
io 코드 개선 개요

JSON 파일을 처리하는 경우 반드시 파일을 읽고 
그 후 쓰는 것이 가능하기에 --> 파일 직렬화 후 파일을 전체 다시 쓰기

파일에서 값을 불러올 때 사용할 읽는 메서드와
파일을 수정할 때 쓸 읽고 쓰기 메서드를 만들어 두었었다.
다만 이 과정에서 읽는 부분의 코드가 중복되기에 이 부분을 수정하기 위해
리펙토링
"""
'''
class IO:
    def __init__(self, path):
        self.path = path

    
    def file_scan(self, func):
        def wrapper():
            file = open(self.path, "r")
            json_parse = json.load(file)
            # file 변수를 func 내부로 전달하는 방법
            f = func(file)
            file.close()
            # del로 인스턴스 제거 필요?
            return f
        return wrapper

    
    def __del__(self):
        print("IO Object has been successfully Deleted.")
'''