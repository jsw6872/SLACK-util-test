# python으로 슬랙봇 만들기
## SLACK  특정 채널 글 올리기
- python slacker 라이브러리 사용불가
  - requests 라이브러리 설치 후 request.post 메소드 이용해 slack api 이용한다.
  - 이 때, scope 설정은 안 해도 되는 듯?
### slack api 앱 만들기
- slack api 접속 후 `Your apps` 클릭 -> creeate an app
- `From scratch` 클릭
- `Bots` 클릭
### 앱 관련 scope(권한) 설정
- `review scopes to add` 클릭
- `Add an OAuth Scope`를 통해 필요한 scope 등록 ( Slack API Methods에서 여러 API 확인 가능 ) - bot : write 권한 필요
-  `Install Workspace`

### 채널에 메시지 게시
- 토큰 복사
- 해당 채널의 봇 토큰을 사용할 경우 게시물을 올리고 싶은 채널의 id로 접근할 경우 게시가 가능
### dm
-  토큰 복사
- 해당 채널의 봇 토큰을 사용할 경우 유저멤버의 Id로 날리면 디엠이 가능, but 일일이 수집이 필요
  - conversations.members를 통해 멤버 id 접근이 가능?? -> 테스트 해볼 필요 있음(권한 설정 등)
      - 채널 권한 설정이 필요해서 수기로 수집할 필요가 있어보임

### corntab을 통해 매일 실행
- 가상환경에서 실행시 가상환경 경로 설정 필요
`* * * * * /usr/local/Caskroom/miniconda/base/envs/da/bin/python /Users/joseong-u/workspace/SLACK-util-test/__main__.py >> ~/workspace/SLACK-util-test/test_log.sh.log 2>&1`
#### bolt 사용?
#### ref
[slack 메시지 알림 slacker사용함 (이용 X)](https://yganalyst.github.io/web/slackbot1/)  
[slack 특정 메시지 찾아서 댓글 달기](https://wooiljeong.github.io/python/slack-bot/)  
[slack_sdk](https://sooftware.io/slack_bot/)  
[slack_sdk2](https://cosmosproject.tistory.com/393)  
[chat.postMessage](https://13akstjq.github.io/api/2019/09/07/Slack-API-%EC%A0%95%EB%A6%AC%ED%95%98%EA%B8%B0.html)  
[webhook 이용](https://ai-creator.tistory.com/298)  
[dm 관련](https://nanchachaa.tistory.com/44)  
[dm 관련-2](https://dosundosun.tistory.com/109)
