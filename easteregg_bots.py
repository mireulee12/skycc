import compile
import re
SLACK_BOT_TOKEN= 
SLACK_APP_TOKEN=
import os
import random
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
import random
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Set the bot token for your Slack bot
bot_token = SLACK_BOT_TOKEN

# Initialize a Slack Bolt app
app = App(token=bot_token)
phrase=["저는 항상 당신 곁에 있어요! 지켜드릴게요. 절대 죽으면 안돼요!🤗","그런 생각 마세요!가족들을 생각하세요!","제가 꼭 안아줄게요!(づ｡◕‿‿◕｡)づ","맘껏 울어요! 아무도 뭐라고 안해요.🥰"]
phrase2=["세상에서 가장 못생긴 새는?:우리 생김새","높은 곳에서 아기를 낳으면?:하이에나",
         "서울이 추우면?:서울시립대","땅이 어떻게 울까?:흙흙","11월에 뱀이랑 벌이 없는 이유는?:노뱀벌","미국에 비가 내리면?: USB",
         "살찐 사람들이 많은 동네는?: 개포동",'피카츄가 담배 피고 싶을 때 하는 말은?: 피까','수소가 암소의 발을 밟았을 때 하는 말은?: 암소쏘리','물리치료가 물리치료인 이유는?: 병을 물리치려고']
food=['백암순대국','정정아식당','고삼이','배바위양곱창','맨도롱식당','영심이네 감자탕','신촌 수제비','별당김치찜','공복','조선의 육개장칼국수','소신이쏘','또보겠지떡볶이','엄마손닭한마리칼국수','군삼겹',
      '더도이 축산직영점','제주상회','참이맛감자탕','행복은간장밥','정통집','담산','도토리칼국수','홍미닭발','the연세김치찌개','대포찜닭','꼬꼬아찌',
      '고냉지','유채우','한림돈가','기꾸스시','스시미세기','여우골','육구덮밥','텐동미세기','하꾸야','야바이','94단','미분당', '맘맘테이블', '방콕 익스프레스', '타코로코', '키친봄날', '오빠네옛날떡볶이', '크리스터 치킨', '폼프리츠', '포석정', '라구식당', '소담식당', '롤링파스타', '니뽕내뽕', '반서울', '비아37', '피자보이시나',
'미스터서왕만두', '완차이', '연경', '가화만사성', '박가네짬뽕', '라이라이', '정육면체', '라장훠궈', '타이완소야', '훗카이도부타동스미레', '가마마루이', '부탄츄', '카라멘야', '하루돈까스', '꼬숑돈까스', '카츠업', '엠브로돈까스',
'가문의우동', '윤오므라이스']
# Define a function to repeat whatever the user says
@app.message("힘들어")
def ask_who(message, say):
    random_int=random.randint(0,3)
    say(phrase[random_int])
@app.message("아재개그")
def ask_whose(message,say):
    random_int=random.randint(0,9)
    say(phrase2[random_int])
@app.message(re.compile("점심"))
def ask_lunch(message,say):
    random_int=random.randint(0,70)
    say(f'{food[random_int]}에 가시는건 어떤가요?')
# Start the Socket Mode handler
if __name__ == "__main__":
    handler = SocketModeHandler(app_token=SLACK_APP_TOKEN,app=app)
    handler.start() 
