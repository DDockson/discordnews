sampletoken.json을 복사한 뒤 token.json으로 이름을 바꿔, 자신의 네이버 API client_id와 client_secret, 디스코드 봇의 토큰을 입력하여주시기 바랍니다.
# discordnews
2024년 자료구조 수행평가를 위해 제작하게 된 프로젝트입니다.
총 제작기간: 1시간 30분

![image](https://github.com/DDockson/discordnews/assets/47936955/90cd0b10-37bd-499e-bb74-6b016cd14025)

파이썬 라이브러리인 request와 네이버 뉴스 API를 활용하여, 가장 최근에 검색한 10개의 기사 자료들을 출력하는 디스코드 봇입니다.

## 작동 원리
![image](https://github.com/DDockson/discordnews/assets/47936955/33ca5551-3ed2-43bf-ac42-7d9c3918d2db)
기본적으로 이 봇은 자료구조 중 큐(Queue)의 구조를 따른다.

![image](https://github.com/DDockson/discordnews/assets/47936955/5c070405-44c4-4b68-a8cd-577499fea795)
봇에게 디미고와 관련된 기사 3개를 검색하면, 위와 같이 큐에 디미고와 관련된 기사 3개가 인큐(Enqueue)된다.

![image](https://github.com/DDockson/discordnews/assets/47936955/7ba82f7d-bf27-4e41-83d9-987e531c2e98)
이후 봇에게 선린고와 관련된 기사 5개를 검색하면, 위와 같이 큐에 선린고와 관련된 기사 5개가 인큐된다.

![image](https://github.com/DDockson/discordnews/assets/47936955/88704074-3f3d-4e6a-9e35-1adc6613a4fa)
그 상태에서 단대고와 관련된 기사 4개를 검색하면, 큐에 들어있는 값들이 10개를 넘기 때문에 자동으로 맨 앞에 있는 기사들이 디큐(Dequeue)된다.

## 주 사용 기술
- `request`: 파이썬에서 http 통신을 위한 라이브러리
- `네이버 뉴스 API`: 네이버 뉴스에서 기사를 검색하기 위한 API
- `discord.py`: 디스코드 봇을 만들기 위한 라이브러리
