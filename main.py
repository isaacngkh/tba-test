import requests
import creds
import csv

headers = {
    'accept': 'application/json',
    'X-TBA-Auth-Key': creds.api_key,
}

def getTeams(event_key: str):
  return requests.get('https://www.thebluealliance.com/api/v3/event/' + event_key + '/teams/simple', headers=headers)

def getMatchKeys(event_key: str):
  return requests.get('https://www.thebluealliance.com/api/v3/event/' + event_key + '/matches/simple', headers=headers)

def getMatchResult(match_key: str):
  return requests.get('https://www.thebluealliance.com/api/v3/match/' + match_key, headers=headers)


event_key = '2024cabe'
r = getMatchKeys(event_key)
if not r.ok:
    print("ERROR: Request to get teams for event key " + event_key + " failed.")
    exit()

request_json = r.json()

# with open('output/match_keys.json', 'w') as f:
#   json.dump(request_json, f, ensure_ascii=True, indent = 2)

fields = ['Match Key',
          'Alliance',
          'Team Number', 
          'Total Score', 
          'Auto Leave', 
          'Auto Amp Count', 
          'Auto Speaker Count', 
          'Teleop Amp Count',
          'Teleop Speaker Unamp Count',
          'Teleop Speaker Amp Count',
          'End Game',
          'Trap Count']

with open('output/output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fields)

for match in request_json:
  match_key = match['key']
  r = getMatchResult(match_key)

  if not r.ok:
    print("ERROR: Request to get match result for match key " + match_key + " failed.")
    exit()

  request_json = r.json()

  # with open('output/' + match_key + '.json', 'w') as f:
  #   json.dump(request_json, f, ensure_ascii=True, indent = 2)

  for alliance in ['blue', 'red']:
    i = 1
    for team_key in request_json['alliances'][alliance]['team_keys']:
      team_number = team_key[3:]
      total_score = request_json['alliances'][alliance]['score']

      score_breakdown = request_json['score_breakdown'][alliance]
      auto_leave = 2 if score_breakdown["autoLineRobot" + str(i)] == 'Yes' else 0
      auto_amp_count = score_breakdown['autoAmpNoteCount']
      auto_speaker_count = score_breakdown['autoSpeakerNoteCount']
      teleop_amp_count = score_breakdown['teleopAmpNoteCount']
      teleop_speaker_unamp_count = score_breakdown['teleopSpeakerNoteCount']
      teleop_speaker_amp_count = score_breakdown['teleopSpeakerNoteAmplifiedCount']

      stage = score_breakdown['endGameRobot' + str(i)]
      climb_point = 0
      trap_count = 0
      if stage == 'StageLeft':
        climb_point = 3
        if(score_breakdown['trapStageLeft']):
          trap_count = 1
      
      elif stage == 'CenterStage':
        climb_point = 3
        if(score_breakdown['trapCenterStage']):
          trap_count = 1

      elif stage == 'StageRight':
        climb_point = 3
        if(score_breakdown['trapStageRight']):
          trap_count = 1

      elif stage == 'Parked':
        climb_point = 1

      fields = [match_key[9:], 
                alliance,
                team_number, 
                total_score, 
                auto_leave, 
                auto_amp_count, 
                auto_speaker_count, 
                teleop_amp_count,
                teleop_speaker_unamp_count,
                teleop_speaker_amp_count,
                climb_point,
                trap_count]

      with open('output/output.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
      
      i += 1