import csv
import api

event_key = '2025camb'
file_name = event_key

r = api.getMatchKeys(event_key)
if not r.ok:
    print("ERROR: Request to get teams for event key " + event_key + " failed.")
    exit()

request_json = r.json()

header = ['Team Number']

with open('output/' + file_name + '.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)

match_count = 0
coop = 0

for match in request_json:
  match_key = match["key"]
  match_result = api.getMatchResult(match_key)

  match_result_json = match_result.json()

  if(match_result_json["comp_level"] != "qm"):
    continue

  match_count += 1
  coop += match_result_json["score_breakdown"]["blue"]["coopertitionCriteriaMet"] or match_result_json["score_breakdown"]["red"]["coopertitionCriteriaMet"]


print("Match Count: " + str(match_count))
print("Coop Total: " + str(coop))
print("Percentage: " + str(coop / match_count))