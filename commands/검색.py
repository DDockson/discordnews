import discord
from discord import app_commands
from discord.ext import commands
import json
import urllib.request
import os
from datetime import datetime

class 검색(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="검색", description="네이버에서 뉴스를 검색합니다")
    @app_commands.describe(text = "원하는 검색어를 입력하세요")
    @app_commands.describe(display = "검색 결과 수를 입력하세요 (1~10)")
    async def 검색(self, interaction: discord.Interaction, text: str, display: app_commands.Range[int, 1, 10]): #검색어 및 검색 결과 수 입력받기

        with open("token.json", 'r', encoding='utf-8') as f:
            config = json.load(f)
        client_id = config['client_id']
        client_secret = config['client_secret'] #token.json에서 client_id와 client_secret을 가져옴

        encText = urllib.parse.quote(text)

        url = "https://openapi.naver.com/v1/search/news?query=" + encText + "&display=" + str(display) # JSON 결과
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode() #네이버 API를 이용하여 검색 결과를 가져옴

        if(rescode==200): #검색 결과가 정상적으로 가져와졌을 때
            response_body = response.read()
            s = json.loads(response_body.decode('utf-8')) #검색 결과를 json으로 변환
            if os.path.exists("response.json"):
                with open("response.json", 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    max_key = max(map(int, data.keys()))
            else:
                data = {}
                max_key = 0 #response.json 파일이 존재하면 데이터 딕셔너리를 읽어오고, 존재하지 않으면 새로 만듦

            while len(data) + display > 10:
                data.pop(next(iter(data))) #검색 결과 수 및 기존 데이터의 개수가 10개를 넘어가면 가장 오래된 결과부터 삭제 (Queue 구조)

            i = 1

            while (display > 0):
                data[max_key + i] = {"title": s['items'][i-1]['title'], "description": s['items'][i-1]['description'], "link": s['items'][i-1]['link']}
                data[max_key + i]['title'] = data[max_key + i]['title'].replace("<b>", "**").replace("</b>", "**").replace("&quot;", '"').replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
                data[max_key + i]['description'] = data[max_key + i]['description'].replace("<b>", "**").replace("</b>", "**").replace("&quot;", '"').replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
                display -= 1
                i+=1 #검색 결과를 데이터 딕셔너리에 저장
            
            json_data = json.dumps(data, ensure_ascii=False)

            with open("response.json", 'w', encoding='utf-8') as f:
                f.write(json_data) #데이터 딕셔너리를 response.json 파일에 저장

            embed = discord.Embed(title=f"현재까지의 검색 결과", color=0x03C75A, timestamp=datetime.now())
            embed.set_author(name="네이버 뉴스", icon_url="https://media.discordapp.net/attachments/757793115204616287/1248347487195107339/btnG_.png")
            for i in data.keys():
                embed.add_field(name=f"{data[i]['title']}", value=f"{data[i]['description']}\n[기사 보러가기]({data[i]['link']})", inline=False)

            await interaction.response.send_message(embed=embed)

        else:
            print("Error Code:" + rescode)
                
async def setup(bot):
    await bot.add_cog(검색(bot))