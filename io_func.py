import json


def read_json(path: str, keyword: str) -> str:
    """
    JSON 파일 읽기
    @params:
        path    : str - json 파일의 경로
        keyword : str - json 파일에서 검색할 value의 key값에 해당하는 문자열
    @return
        :str - params keyword(json key)값에 맞는 값
    """

    with open(path, "r") as file:
        json_parse = json.load(file)
        return json_parse[keyword]


class Write:
    def __init__(self, path):
        self.path = path

    def write_jsons(self, keyword: str, value: str) -> None:
        """
        JSON 파일 쓰기
        @params:
            keyword : str - 파일에서 찾을 value의 key값에 해당하는 문자열
            value   : str - 수정할 내용의 문자열
        @return:
            None
        """

        with open(self.path, "r") as file:
            json_parse = json.load(file)
            # 데이터 수정
            json_parse[keyword] = value

        # 기존 파일 덮어쓰기
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(json_parse, file, indent="\t")


"""
io 코드 개선 개요

JSON 파일을 처리하는 경우 반드시 파일을 읽고 
그 후 쓰는 것이 가능하기에 --> 파일 직렬화 후 파일을 전체 다시 쓰기

파일에서 값을 불러올 때 사용할 읽는 메서드와
파일을 수정할 때 쓸 읽고 쓰기 메서드를 만들어 두었었다.
다만 이 과정에서 읽는 부분의 코드가 중복되기에 이 부분을 수정하기 위해
리펙토링
"""
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


# 데코레이터를 사용하는 것은 적절하지 않음
@IO.file_scan
def read(keyword: str, file) -> str:
    return file[keyword]

@IO.file_scan
def write(self, keyword: str, value: str, **kwargs) -> None:
    kwargs[keyword] = value

    # override previous file
    with open(self.path, "w", encoding="utf-8") as file:
        json.dump(file, file, indent="\t")