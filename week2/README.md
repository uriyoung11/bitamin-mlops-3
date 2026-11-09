# Week 2 체크포인트 진행

추적 Issue: [#3](https://github.com/uriyoung11/bitamin-mlops-3/issues/3)

이 문서는 2026-09-26에 확인한 상태와 남은 진행 절차를 기록한다. 원래의 결과 화면은 루트 README에 유지한다. 완료 체크는 실제 조원별 GitHub 기록과 실행 결과를 확인한 뒤 한다.

## 확인한 상태

| 항목 | 확인 내용 | 남은 확인 |
|---|---|---|
| 저장소 및 Push | Public, 1주차 파일과 이력 존재 | 완료 |
| 조원별 Branch 작업 | main + 기능 브랜치 4개 존재; RF 담당 0jin03의 4e8a951 Push | 평가 브랜치의 작업 커밋 |
| PR 및 Review | 전처리 #1, LR #2 병합; RF #6 생성 및 리뷰 요청; 0jin03의 #2 코드 리뷰 제출 | 평가 PR과 다른 조원의 코드 줄 리뷰 |
| 모든 기능 PR Merge | #1, #2 병합 | #4·#5·#6 및 평가 PR 리뷰·병합 |
| Conflict 해결 | ccba95e에 마커가 포함됐고 ff27c8a에서 제거 | LR 설정이 덮어써지는 병합 오류를 수정 PR #4에서 보완 |
| Issue 및 Convention | Issue #3 Timeline에 RF 커밋 4e8a951 연결 확인 | CONTRIBUTING main 반영 |
| PR Template | 이 변경에 템플릿 추가 | main 반영 후 새 PR 작성 화면에서 자동 표시 |
| Branch Protection | 확인 당시 Ruleset 없음 | 관리자 설정 및 타 조원 승인 전후 동작 확인 |

브랜치 이름이 있다는 사실만으로 조원별 작업이 완료된 것은 아니다. PR #1, #2에 있던 일반 대화 댓글은 Files changed에서 제출한 코드 리뷰와 구분한다. 병합 후 리뷰를 작성해도 이전 Merge가 리뷰 후 수행된 것으로 소급하지 않는다.

## 남은 역할별 진행

RF 담당은 `0jin03`이며 [PR #6](https://github.com/uriyoung11/bitamin-mlops-3/pull/6)을 제출했다. RF 200개 트리, balanced 가중치, random_state 42를 사용한다. 실제 테스트 데이터 1,409건에서 Accuracy 0.7963을 확인했다. 학습 데이터 median과 imputer 통계 일치, 미지 범주·결측값 예측, LR/RF 전처리 객체 분리도 검증했다. `uriyoung11`에게 코드 리뷰를 요청한 상태다.

평가 담당자는 자신의 계정으로 기존 작업 브랜치를 가져오고 최신 main을 병합한 뒤 작업한다. 이미 본인 작업이 있는 경우 반드시 보존한다.

```bash
git fetch origin
git switch feature/evaluation-metrics
git merge origin/main
# 본인 역할의 코드 변경 후 실행
python app.py
git add app.py
git commit -m "feat: add evaluation metrics (#3)"
git push origin HEAD
```

RF는 기존 LR와 같은 학습/평가 분할을 사용하고 전처리가 학습 데이터에만 fit되게 한다. 평가 지표는 현재 타깃이 Yes/No 문자열이라는 점을 고려하여 이탈 고객 `Yes`를 양성으로 처리한다.

각자 base main으로 PR을 생성하고 변경 이유·실행 결과를 기록한다. 조원 전원이 다른 조원의 PR에서 코드 줄에 코멘트를 작성한 뒤 Submit review하고, 각 PR에도 최소 1건의 리뷰가 남도록 역할을 배분한다. 본인 PR은 본인이 승인할 수 없다.

## 충돌과 기능 보존

기존 충돌 해결 기록:

- [ccba95e: 병합 중 마커가 남아 있던 커밋](https://github.com/uriyoung11/bitamin-mlops-3/commit/ccba95e4c7ea6c357abc1e48be9204039cdb61bc)
- [ff27c8a: 마커 제거](https://github.com/uriyoung11/bitamin-mlops-3/commit/ff27c8a34bbfed5a377925ae2005e0bf45ede1c8)
- [PR #4: LR 설정 보존 수정](https://github.com/uriyoung11/bitamin-mlops-3/pull/4)

충돌 마커 제거 후에도 한쪽 기능이 무시될 수 있으므로 학습 객체와 평가 출력을 검증한다. 충돌이 다시 생기면 충돌 전 화면을 먼저 기록하고 필요한 코드를 합친다.

```bash
git fetch origin
git merge origin/main
# 충돌 마커가 보이는 화면을 기록한 뒤 편집
python app.py
git diff --check
git add app.py
git commit -m "fix: resolve merge conflict (#3)"
git push
```

## 심화 체크포인트 검증

### Issue와 커밋

`CONTRIBUTING.md`의 형식을 따른다. 같은 저장소의 커밋은 `(#3)`, fork에서 작성하는 커밋은 `(uriyoung11/bitamin-mlops-3#3)`처럼 원본 Issue를 명시한다. Issue #3의 Timeline에서 실제 커밋 링크를 확인한다. 각 항목이 아직 남아 있으므로 추적 Issue를 조기에 닫지 않는다.

### PR 템플릿

`.github/pull_request_template.md`가 main에 병합된 후 새 PR 작성 화면에서 본문 항목이 자동으로 나타나는지 확인한다. 이 파일 자체를 처음 추가하는 PR은 자동 표시 검증 대상이 아니다.

### main Ruleset

관리자는 Settings → Rules → Rulesets에서 main을 대상으로 Active, Require a pull request before merging, Required approvals 1을 설정한다. 우회 사용자를 추가하지 않아 승인 전 제한을 검증한다.

`.github/main-ruleset.json`은 위 설정의 적용안이다. 파일을 커밋하는 것만으로 GitHub 설정이 활성화되지는 않는다. 기존 Ruleset이 있는지 확인하고 있으면 중복 생성하지 말고 수정한다.

1. 설정 저장 후 main의 Ruleset 화면을 기록한다.
2. 별도 문서 변경 PR에서 승인 전 Merge 제한 화면을 기록한다.
3. 쓰기 권한이 있는 다른 조원이 내용을 검토하고 Approve한다.
4. 승인 뒤 Merge 가능 화면을 기록하고 해당 PR도 Merge한다.

설정 화면만 확인하거나 단일 계정의 PR만 생성한 상태는 승인 전후 동작 검증 완료로 표시하지 않는다.

## 최종 점검

- [x] Public Repository 및 1주차 파일 Push
- [ ] 조원 전원이 각자 Branch에서 실제 작업
- [ ] 조원 전원이 PR 생성 및 다른 조원의 변경에 코드 리뷰 제출
- [ ] 모든 기능 PR과 보완 PR을 리뷰 후 Merge
- [ ] 충돌 전후 증빙과 기능이 보존된 실행 결과 확인
- [ ] Issue Timeline 및 커밋 규칙 확인
- [ ] main의 PR 템플릿과 새 PR의 자동 표시 확인
- [ ] Ruleset 활성화 및 타 조원 승인 전후 Merge 동작 확인

## 공식 참고

- [PR 템플릿 만들기](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)
- [Ruleset 규칙](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)
