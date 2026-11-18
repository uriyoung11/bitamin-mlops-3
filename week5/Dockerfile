
# STEP 2: week5/README.md를 보고 FastAPI 실행 이미지를 완성하세요.
# 1. Python 3.13 slim 베이스 이미지
# 2. 작업 디렉터리 /app
# 3. week4/requirements.txt 복사 및 설치
# 4. week4/ 폴더 복사 (모델 포함)
# 5. 8000 포트 안내 및 Uvicorn 실행 (0.0.0.0에 바인딩)
# 빌드 컨텍스트는 저장소 루트(.)입니다.

FROM python:3.13-slim

WORKDIR /app

COPY week4/requirements.txt /app/requirements.txt
RUN python -m pip install --no-cache-dir -r /app/requirements.txt

COPY week4/ /app/week4/

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "week4.main:app", "--host", "0.0.0.0", "--port", "8000"]
