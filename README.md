from robot import Robot

bot = Robot(nickname='jargo')

@bot.exec(name='hello_world')
def hello_world(arguments):
  print('hello world')

bot.speak('hello world')
