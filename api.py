import requests
import creds

# Blue Alliance
headers = {
    'accept': 'application/json',
    'X-TBA-Auth-Key': creds.api_key,
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


# Statbotics
statebotics_headers = {
    'accept': 'application/json'
}

def getTeamStat(team_key: str):
  return requests.get('https://api.statbotics.io/v3/team/' + team_key, headers = statebotics_headers)