import requests
import api
import csv

event_key = '2025casf'
file_name = event_key

r = api.getTeamsKeys(event_key)
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

print(api.getTeamsEventsMatches("frc5507", api.getTeamsEvents("frc5507", 2025).json()[0]))