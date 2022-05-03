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
- `Add an OAuth Scope`를 통해 필요한 scope 등록 ( Slack API Methods에서 여러 API 확인 가능 )
-  `Install Workspace`
-  토큰 복사
#### bolt 사용?
#### ref
[slack 메시지 알림 slacker사용함 (이용 X)](https://yganalyst.github.io/web/slackbot1/)  
[slack 특정 메시지 찾아서 댓글 달기](https://wooiljeong.github.io/python/slack-bot/)  
[slack_sdk](https://sooftware.io/slack_bot/)  
[slack_sdk2](https://cosmosproject.tistory.com/393)  
[chat.postMessage](https://13akstjq.github.io/api/2019/09/07/Slack-API-%EC%A0%95%EB%A6%AC%ED%95%98%EA%B8%B0.html)
[webhook 이용](https://ai-creator.tistory.com/298)