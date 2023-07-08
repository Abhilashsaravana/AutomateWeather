import requests
import json
from datetime import date
from PIL import Image, ImageDraw, ImageFont

apikey = "2aa11ac3bf663f2db7f0d1790a6d27f9"
cities = ["Dubai","New York","Delhi","London","Sydney"]
img  = Image.open('post.png')
title_font = ImageFont.truetype('Inter-Medium.ttf',size=50)
title_text = "Weather Forecast"
draw = ImageDraw.Draw(img)
draw.text((330,55),title_text,(255,255,255),font=title_font)
title_font = ImageFont.truetype('Inter-Medium.ttf',size=30)
title_text = date.today().strftime("%A,  %d-%B-%Y")
draw.text((55,145),title_text,(255,255,255),font=title_font)
title_font = ImageFont.truetype('Inter-Medium.ttf',size=40)
k = 0
for i in cities:
    url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=metric" %(i,apikey)

    data = requests.get(url)
    data = json.loads(data.text)
    
    draw.text((250,300+k),i,(0,0,0),font=title_font)
    title_text = data['main']['temp']
    draw.text((600,300+k),str(title_text)+" C",(255,255,255),font=title_font)
    title_text = data['main']['humidity']
    draw.text((810,300+k),str(title_text)+" %",(255,255,255),font=title_font)
    k+=130
    
img.show()
img.save('test1.png')
        
    
