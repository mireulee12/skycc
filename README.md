# skycc
2023 skycc pairing

![Web App Reference Architecture](https://github.com/mireulee12/skycc/assets/60784366/b0bdee8f-d4c3-457c-8778-5939e3268f30)

- easteregg_bots.py: 이스터에그 슬랙 봇
- lambda_function.py: 연세대학교 홈페이지 장학금 공지에서 크롤링해서 DB에 적재
- slack-scholarship.py: slack message를 쿼리로 사용해 DB를 스캔, 해당하는 item들을 slack message로 전송
