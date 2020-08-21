from pypresence import Presence
import requests
import time

client_id = "484226352191504384"
RPC = Presence(client_id=client_id)
RPC.connect()

gamesJson = requests.get("http://api.hivemc.com/v1/game").json()

uuid = input("What is your UUID? (https://mcuuid.net/)")
apiKey = input("What is your Hypixel API key? (api.hypixel.net)")

hypixelGames = {
	"QUAKECRAFT": "Quake",
	"WALLS": "Walls",
	"PAINTBALL": "Paintball",
	"SURVIVAL_GAMES": "Blitz Survival Games",
	"TNTGAMES": "TNT Games",
	"VAMPIREZ": "VampireZ",
	"WALLS3": "Mega Walls",
	"ARCADE": "Arcade",
	"ARENA": "Arena",
	"UHC": "UHC Champions",
	"MCGO": "Cops and Crims",
	"BATTLEGROUND": "Warlords",
	"SUPER_SMASH": "Smash Heroes",
	"GINGERBREAD": "Turbo Kart Racers",
	"HOUSING": "Housing",
	"SKYWARS": "SkyWars",
	"SPEED_UHC": "Speed UHC",
	"TRUE_COMBAT": "Crazy Walls",
	"SKYCLASH": "SkyClash",
	"LEGACY": "Classic Games",
	"BEDWARS": "Bed Wars",
	"MURDER_MYSTERY": "Murder Mystery",
	"BUILD_BATTLE": "Build Battle",
	"DUELS": "Duels"
}

def getIcon(server):
	if server == "HiveMC":
		return "vqjw6xg"
	if server == "Hypixel":
		return "hypixel"
	return ""

def getHiveGame(code):
	if code == "OFFLINE":
		return "Sleeping in the Land of Nod!"
	if code in gamesJson:
		return 'Playing ' + gamesJson[code]
	if code == 'HUB':
		return "Relaxing in a Regular Hub"
	if 'BED' in code:
		return 'Playing BedWars'
	if 'SKY' in code:
		return 'Playing SkyWars'
	elif code == 'PREMHUB':
		return "Chilling in a Premium Hub"
	
	return 'Who? What? Where?'

def getHypixelGame(code):
	if code in hypixelGames:
		return "Playing " + hypixelGames[code]
	return "Who? What? Where?"

while True:
	time.sleep(15) 

	server = "HiveMC"
	jsonEek = requests.get("http://api.hivemc.com/v1/player/" + uuid + "/status/raw").json()
	location = jsonEek['status']
	englishGame = getHiveGame(location)

	if location == 'OFFLINE':
		jsonEek = requests.get('https://api.hypixel.net/session?uuid=' + uuid + '&key=' + apiKey).json()
		location = jsonEek['session']
		if location == None:
			server = "Singleplayer"
			englishGame = "All alone!"
		else:
			englishGame = getHypixelGame(location['gameType'])
			server = 'Hypixel'

	RPC.update(large_image="mclogo", large_text="Playing Minecraft",
            small_image=getIcon(server), small_text="Server: "+ server,
            state = "Server: "+ server,details = englishGame)
