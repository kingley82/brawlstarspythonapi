import requests
import json

token = ""
player_tag = ""
club_tag = ""
county_code = ""

headers = {
	"Accept": "application/json",
	"Authorization": "Bearer: " + token
}

def getPlayerInfo(player_tag):
	return requests.get(f"https://api.brawlstars.com/v1/players/%23{player_tag}", headers=headers).json()

def getPlayerBattleLogs(player_tag):
	return requests.get(f"https://api.brawlstars.com/v1/players/%23{player_tag}/battlelog", headers=headers).json()

def getClubInfo(club_tag):
	return requests.get(f"https://api.brawlstars.com/v1/clubs/%23{club_tag}", headers=headers).json()

def getClubsRating(country_code):
	#Country code - two letter (RU, EN etc.) or global for global
	return requests.get(f"https://api.brawlstars.com/v1/rankings/{country_code}/clubs", headers=headers).json()

def getPlayersRating(country_code):
	#Country code - two letter (RU, EN etc.) or global for global
	return requests.get(f"https://api.brawlstars.com/v1/rankings/{country_code}/players", headers=headers).json()