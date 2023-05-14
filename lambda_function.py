import json
import urllib.request
from bs4 import BeautifulSoup
import boto3

dynamodb = boto3.client('dynamodb')

url = "https://www.yonsei.ac.kr/sc/support/scholarship.jsp"
soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")

link_list = []

for i in range(0, 14):
    selector = "#jwxe_main_content > div.jwxe_board > div > ul > li:nth-child(" + str(i+1) + ") > a"
    link = "https://www.yonsei.ac.kr/sc/support/scholarship.jsp" + soup.select_one(selector)["href"]
    link_list.append(link)
    
title_list = []
info_list = []

for link in link_list:
    soup = BeautifulSoup(urllib.request.urlopen(link).read(), "html.parser")
    info_list.append(soup.select("p")[0].text)
    title_list.append(soup.select("strong")[3].text)
    
item = {"link": {'S':title_list[10]}, 
       "title": {"S": title_list[10]}, 
       "info": {"S":info_list[10]}, 

}
       
def lambda_handler(event, context):

    response = dynamodb.put_item(
        TableName = 'scholarship',
        Item = item)
 
    return response
