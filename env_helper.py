import os
from google import genai
from google.genai import types

def read_files(file_paths):
    content = ""
    for path in file_paths:
        path = path.strip()
        if not path:
            continue
        if not os.path.exists(path):
            print(f"[경고] 파일을 찾을 수 없음: {path}")
            continue
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content += f"--- 파일 시작: {path} ---\n"
                content += f.read() + "\n"
                content += f"--- 파일 종료: {path} ---\n\n"
        except Exception as e:
            print(f"[오류] 파일 읽기 실패 ({path}): {e}")
    return content

def analyze_environment_and_code():
    # 1. API 키 설정 및 클라이언트 초기화
    api_key = input("Google Gemini API Key를 입력: ").strip()
    if not api_key:
        print("[오류] API Key가 입력되지 않음.")
        return

    # 최신 SDK의 Client 객체 생성 방식 적용
    client = genai.Client(api_key=api_key)

    # 2. 파일 경로 입력받기 (다중 파일 지원)
    env_files_input = input("환경 요약 파일 경로를 입력 (쉼표로 구분하여 여러 개 입력 가능): ")
    code_files_input = input("분석할 프로그램 코드 파일 경로를 입력 (쉼표로 구분하여 여러 개 입력 가능): ")

    env_file_paths = env_files_input.split(',')
    code_file_paths = code_files_input.split(',')

    # 3. 파일 내용 병합
    print("\n파일을 읽는 중...")
    env_content = read_files(env_file_paths)
    code_content = read_files(code_file_paths)

    if not env_content or not code_content:
        print("[오류] 분석할 환경 데이터 또는 코드 데이터가 부족함.")
        return

    # 4. Gemini API를 사용하여 분석 요청
    prompt = f"""
    당신은 파이썬 개발 환경 최적화 및 디버깅 전문가입니다.
    아래 제공된 '실행 환경 요약 데이터'와 '실행할 파이썬 소스 코드'를 분석하십시오.

    [분석 목표]
    제공된 환경에서 해당 코드를 실행할 때 발생할 수 있는 환경 종속적인 에러(예: 모듈 누락, 버전 호환성 문제, 인코딩 에러, 경로 문제, OS 한정 기능 등)를 예측하고, 각각에 대한 구체적인 해결 방법을 제시하십시오.

    [데이터]
    1. 실행 환경 요약 데이터:
    {env_content}

    2. 실행할 파이썬 소스 코드:
    {code_content}
    """

    print("Gemini API에 분석을 요청하는 중...\n")
    try:
        # gemini-2.5-flash 모델 사용 (최신 권장 모델)
        response = client.models.generate_content(
            model='gemini-2.5-flash', #필요에 따라 model 변경
            contents=prompt,
        )
        
        print("="*50)
        print(" AI 환경 및 코드 분석 결과 ")
        print("="*50)
        print(response.text)
        print("="*50)

    except Exception as e:
        print(f"[오류] API 호출 중 문제 발생: {e}")

if __name__ == "__main__":
    analyze_environment_and_code()