import sys
import os
import platform
import locale
import datetime
from importlib.metadata import distributions

def get_system_info():
    return {
        "OS_System": platform.system(),
        "OS_Release": platform.release(),
        "OS_Version": platform.version(),
        "Architecture": platform.machine(),
        "Processor": platform.processor(),
    }

def get_python_info():
    return {
        "Python_Version": sys.version.split('\n')[0],
        "Python_Implementation": platform.python_implementation(),
        "Python_Compiler": platform.python_compiler(),
        "Architecture_Bits": platform.architecture()[0],
    }

def get_execution_context():
    return {
        "Executable_Path": sys.executable,
        "Script_Path": os.path.abspath(sys.argv[0]) if sys.argv else "N/A",
        "Current_Working_Dir": os.getcwd(),
        "Sys_Args": sys.argv,
        "Sys_Path": sys.path,
    }

def get_encoding_and_locale():
    loc, enc = locale.getlocale()
    return {
        "Default_Encoding": sys.getdefaultencoding(),
        "FileSystem_Encoding": sys.getfilesystemencoding(),
        "Locale": f"{loc}.{enc}" if loc else "Unknown",
        "System_Time_UTC": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }

def get_environment_variables():
    return dict(os.environ)

def get_installed_packages():
    return {dist.metadata['Name']: dist.version for dist in distributions()}

# 수정됨: 매개변수 output_path 추가
def print_environment_summary(output_path=None):
    sections = {
        "1. OS & Hardware Info": get_system_info(), #OS 및 아키텍처별 호환성 결정
        "2. Python Interpreter Info": get_python_info(), #파이썬 버전별 문법 및 기능 지원
        "3. Execution Context & Paths": get_execution_context(), #모듈 탐색 및 파일 접근 경로 결정
        "4. Encoding, Locale & Time": get_encoding_and_locale(), #입출력 인코딩 및 시간 기준 설정
        "5. Environment Variables": get_environment_variables(), #외부 환경 설정 및 동적 변수 제어
        "6. Installed Packages": get_installed_packages(), #의존성 패키지 버전별 기능 제어
    }

    output_lines = []
    output_lines.append("="*50)
    output_lines.append(" PYTHON ENVIRONMENT DIAGNOSTIC REPORT ")
    output_lines.append("="*50)

    for section_name, data in sections.items():
        output_lines.append(f"\n[{section_name}]")
        if isinstance(data, dict):
            for key, value in data.items():
                output_lines.append(f"{key}: {value}")
        elif isinstance(data, list):
            for item in data:
                output_lines.append(f"- {item}")
    
    output_lines.append("\n" + "="*50)
    
    for line in output_lines:
        print(line)

    # 지정된 절대 경로에 파일 저장 수행
    if output_path:
        try:
            dir_name = os.path.dirname(output_path)
            if dir_name:
                os.makedirs(dir_name, exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write("\n".join(output_lines))
            print(f"\n[SUCCESS] 파일 저장 완료: {output_path}")
        except Exception as e:
            print(f"\n[ERROR] 파일 저장 실패: {e}")

if __name__ == "__main__":
    print("결과를 저장할 절대 경로와 파일명을 입력하세요")
    user_input = input(r""
    "(ex)C:\Users\사용자명\Documents\env_summary.json 또는 /Users/사용자명/Documents/env_summary.json 등 / 엔터 입력 시 콘솔 출력만 수행): ").strip()
    
    target_absolute_path = user_input if user_input else None  
    
    print_environment_summary(target_absolute_path)