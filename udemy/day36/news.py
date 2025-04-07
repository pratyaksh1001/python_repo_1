import requests
import json
now="2024-10-6"
def pullnews(x):
    final=f""
    news_params={
        "qInTitle":x,
        "country":"in",
        "language":"en"
    }
    news=requests.get(url="https://newsdata.io/api/1/latest?apikey=pub_47082d694f3236bc4cd6eb10dc7561b2a0fe1",params=news_params)
    file=open("data.json","w")
    json.dump(news.json(),file,indent=4)
    results=news.json()["results"]
    final+=f"results of - {x}\n\n\n"
    for i in results:
        final+=f"{i["title"]}\n\n"#description - {i['description']}\n\n"
    final+="\n\n\n"
    print(final)
    file.close()
    print(final)
    return final


pullnews(now)