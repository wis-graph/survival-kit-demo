# survival-kit

직장인 생존 키트. Claude Code 플러그인.

## 기능

| 기능 | 언제 | 소리 / 사용법 |
|---|---|---|
| 작업 완료 알림 | Claude 응답이 끝났을 때 (`Stop`) | `sounds/done.wav` 높은음 두 개가 올라감 (0.45초) |
| 승인 대기 알림 | 도구 실행 승인을 기다릴 때 (`Notification: permission_prompt`) | `sounds/approval.wav` 같은 높은음 두 번 (0.27초) |
| 오류 알림 | API 오류로 응답이 멈췄을 때 (`StopFailure`) | `sounds/error.wav` 낮은음 두 개가 내려감 (0.60초) |
| `/survival-kit:today` | 할 일을 생각나는 대로 적으면 | 순번·등급(상/중/하)·예상 시간·이유 표 + 합계 |
| `/survival-kit:decline` | 받은 부탁 메시지를 붙여 넣으면 | 공손한 거절·단호한 거절·웃긴 거절 답장 하나씩 |
| `/survival-kit:morning-news` | 아침에 실행하면 (분야를 적으면 그 분야로) | AI·경제·비영리 분야별 서브에이전트가 동시에 최근 이틀(비영리는 일주일) 뉴스를 모아 출처 링크가 붙은 세 줄 브리핑 |
| `/survival-kit:off-work` | 언제든 (퇴근 시각을 적으면 그 시각으로) | 퇴근(기본 18:00)까지 남은 시간과 응원 한마디 한 줄 |

소리 파일은 플러그인에 들어 있어서 macOS와 Windows에서 같은 소리가 난다.

- **macOS**: `afplay`로 재생
- **Windows**: Windows PowerShell의 `Media.SoundPlayer`로 재생. Git for Windows가 있든 없든 동작하도록 hook 명령 한 줄을 bash와 PowerShell 양쪽에서 실행되게 썼다. Windows에서는 소리가 0.5초쯤 늦게 날 수 있다(PowerShell 시작 시간).
- **Linux·WSL**: 소리 없이 넘어간다.

## 설치

저장소를 받은 폴더 안에서 실행한다.

이 프로젝트에서만 계속 쓰기:

```bash
claude plugin marketplace add ./ --scope project
claude plugin install survival-kit@survival-kit-demo --scope project
```

한 번만 시험해 보기:

```bash
claude --plugin-dir .
```

## 사용 예

```
/survival-kit:today 주간보고 오늘까지, 김대리 메일 답장, 경비 정산 이번주, 책상 정리, 3시 회의 자료 준비
```

```
/survival-kit:decline 대리님~ 이번 주 금요일 저녁 회식 장소 좀 알아봐 주실 수 있을까요? 12명이에요!
```

```
/survival-kit:morning-news
/survival-kit:morning-news 반도체, 기후
```

```
/survival-kit:off-work
/survival-kit:off-work 19:30
```

## 소리 바꾸기

`sounds/make-sounds.py`에서 음 높이(Hz)와 길이(초)를 고친 뒤 다시 만든다. Python 표준 라이브러리만 쓴다.

```bash
python3 sounds/make-sounds.py sounds
```
