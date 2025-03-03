import requests
import creds
import csv

headers = {
    'accept': 'application/json',
    'X-TBA-Auth-Key': creds.api_key,
}

statebotics_headers = {
    'accept': 'application/json'
}

def getTeams(event_key: str):
  return requests.get('https://www.thebluealliance.com/api/v3/event/' + event_key + '/teams/simple', headers=headers)

def getTeamsKeys(event_key: str):
  return requests.get('https://www.thebluealliance.com/api/v3/event/' + event_key + '/teams/keys', headers=headers)

def getTeamsEvents(team_key: str, year: int):
  return requests.get('https://www.thebluealliance.com/api/v3/team/' + team_key + '/events/' + str(year) + '/keys', headers=headers)

def getTeamsEventsMatches(team_key: str, event_key: str):
  return requests.get('https://www.thebluealliance.com/api/v3/team/' + team_key + '/events/' + event_key + '/matches/keys', headers=headers)

def getMatchKeys(event_key: str):
  return requests.get('https://www.thebluealliance.com/api/v3/event/' + event_key + '/matches/simple', headers=headers)

def getMatchResult(match_key: str):
  return requests.get('https://www.thebluealliance.com/api/v3/match/' + match_key, headers=headers)

def getTeamStat(team_key: str):
  return requests.get('https://api.statbotics.io/v3/team/' + team_key, headers = statebotics_headers)


event_key = '2025casf'
file_name = event_key

r = getTeamsKeys(event_key)
if not r.ok:
    print("ERROR: Request to get teams for event key " + event_key + " failed.")
    exit()

request_json = r.json()

header = ['Team Number']

with open('output/' + file_name + '.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)

# Loop through each team at event
for team in request_json:
  team_key = team[3:]
  # stat_json = getTeamStat(team_key).json()
  # if len(stat_json) == 0:
  #   continue
  # current_epa = stat_json['norm_epa']['current']

  field = [team_key]
  
  with open('output/' + file_name + '.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(field)

print(getTeamsEventsMatches("frc5507", getTeamsEvents("frc5507", 2025).json()[0]))