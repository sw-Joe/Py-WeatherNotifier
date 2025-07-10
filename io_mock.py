import json
"""
개요

파일의 I/O를 처리하는 과정의 경우 반드시 파일을 읽고(r mode), 
그 후 쓰는 것이 가능하기에 --> X

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


@IO.file_scan
def read(keyword: str, file) -> str:
    return file[keyword]

@IO.file_scan
def write(self, keyword: str, value: str, **kwargs) -> None:
    kwargs[keyword] = value

    # override previous file
    with open(self.path, "w", encoding="utf-8") as file:
        json.dump(file, file, indent="\t")