from robot import Robot

bot = Robot(nickname='jargo')

@bot.exec(name='drawing')
def drawing(arguments):
  print('hello world')

bot.speak('desenho')
