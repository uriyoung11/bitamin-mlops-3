# 협업 규칙

## 역할과 브랜치

| 역할 | 브랜치 | 변경 범위 |
|---|---|---|
| 전처리 | `feature/preprocessing` | 학습 데이터로만 fit, 결측치 대체, One-Hot, 표준화 |
| Logistic Regression | `feature/logistic-regression` | `class_weight`, `random_state` |
| Random Forest | `feature/random-forest` | 모델 학습 및 Accuracy 출력 |
| 평가 | `feature/evaluation-metrics` | Precision, Recall, F1 및 공통 평가 함수 |

각자 자신의 GitHub 계정과 Git 작성자 정보로 커밋하고 PR을 생성한다.
브랜치를 모두 같은 시작 커밋에서 만든 후 작업하면 병합 충돌 실습이 가능하다.

## 커밋 메시지

형식: `<type>: <summary> (#실제이슈번호)`

- `feat`: 기능 추가 또는 개선
- `fix`: 오류 수정
- `docs`: 문서 수정
- `refactor`: 코드 구조 개선
- `chore`: 설정 및 기타 작업

예: `feat: add random forest classifier (#3)`
위 번호는 예시다. 이 저장소에 실제로 생성된 관련 Issue 번호를 사용한다.
진행 중에는 `Refs #번호`로 연결하고, 작업을 마무리하는 PR 본문에는 `Closes #번호`를 쓴다.

## PR 및 리뷰

1. `base: main`, `compare: 본인 브랜치`로 PR을 연다.
2. 변경 이유와 실행 결과를 PR 템플릿에 기록한다.
3. 다른 조원의 PR에서 `Files changed` → 코드 줄의 `+` → `Start a review`로 코멘트를 작성한다.
4. 변경사항을 검토한 뒤 `Submit review`로 리뷰를 제출한다. 제출 전 Pending 상태는 완료가 아니다.
5. 모든 조원이 다른 사람의 PR에 최소 1건의 코드 리뷰 코멘트를 남기고, 모든 PR도 최소 1건의 리뷰를 받는다.
6. 승인 필요 규칙을 사용하는 경우 권한 있는 다른 조원이 `Approve`한다.
7. 리뷰 후 Merge한다. 실습 증빙을 확인할 때까지 기능 브랜치를 유지한다.

일반 PR 대화 코멘트와 `Files changed`의 코드 리뷰 코멘트를 구분한다.
본인의 PR은 본인이 승인할 수 없다.

## 충돌 해결

본인 브랜치에서 `git fetch origin` 후 `git merge origin/main`을 실행한다.
충돌 발생 화면과 `<<<<<<<`, `=======`, `>>>>>>>`가 있는 파일을 먼저 기록한다.
양쪽 변경 의도를 확인하여 필요한 코드를 합친 뒤 마커를 모두 제거한다.
`python app.py`로 실행을 확인하고, `git add app.py` → `git commit` → `git push`한다.
충돌을 해결하는 과정에서 다른 모델이나 평가 지표가 삭제되지 않았는지 리뷰한다.
