import requests
from env import RIOT_API, SUMMONER

headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "{}".format(RIOT_API)
}

r = requests.get('https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}'.format(SUMMONER), headers=headers)
summoner_id = r.json()['id']

r = requests.get('https://euw1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{}'.format(summoner_id), headers=headers)

json = r.json()
for x in json['participants']:
    r= requests.get('https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/{}'.format(x['summonerId']), headers=headers)
    summoner = r.json()[0]
    print('name {}, rank {} {}, elo {}, wins/loses {}/{}, winstreak : {}'.format(summoner['summonerName'], summoner['tier'], summoner['rank'], summoner['leaguePoints'], summoner['wins'], summoner['losses'], str(summoner['hotStreak'])))
