import requests
import json

class Robot():
  previous_reaction_id = None
  procedures = {}

  def __init__(self, nickname):
    self.nickname = nickname

  def speak(self, keywords):
    request = requests.get(
      url=f'https://jargorobots.herokuapp.com/api/v1/robots/{self.nickname}/speak',
      data={'keywords': keywords,
            'previous_reaction_id': Robot.previous_reaction_id}
    )

    response_json = json.loads(request.content)
    interaction = response_json['interaction']

    if(interaction['id'] is None):
      print('Sem resposta')
      return

    reaction = interaction['reaction']
    Robot.previous_reaction_id = reaction['id']

    for(procedure) in reaction['procedures']:
      procedure = procedure['procedure']
      command = procedure['command']

      if not command in Robot.procedures:
        return

      arguments = procedure['arguments']

      Robot.procedures[command](arguments)

    return reaction['text']

  def exec(self, name):
    def decorator(function):
      Robot.procedures[name] = function

    return decorator

  def execute(self, command):
    function = getattr(self, command)
    function()
