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

    if request.status_code == 404:
      self.response = response_json['message']
      return

    if request.status_code != 200:
      self.response = "I'm without access to my memory, try again later, sorry"
      return

    interaction = response_json['interaction']

    reaction = interaction['reaction']

    Robot.previous_reaction_id = reaction['id']
    self.response = reaction['text']
    self.procedures = reaction['procedures']

    return reaction['text']

  def get_response(self):
    return self.response

  def execute_procedures(self):
    for(procedure) in self.procedures:
      command = procedure['command']

      if not command in Robot.procedures:
        return f'not_implemented: {command}'

    for(procedure) in self.procedures:
      arguments = procedure['arguments']
      Robot.procedures[command](arguments)

  def exec(self, name):
    def decorator(function):
      Robot.procedures[name] = function

    return decorator

  def execute(self, command):
    function = getattr(self, command)
    function()
