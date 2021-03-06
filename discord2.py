import discord
import os
import requests
import json
import random
from keep_alive import keep_alive


client = discord.Client()

happy_words = ["lipaya", "happy", "Happy", "Lipay", "Lipaya", "lipay", "smiling", "smiley","Smiling", "Smiley", "I feel better"]

starter_supports = ["good for you", "That is good to hear", "keep it up", "Sana all", "Sanaol"]

sad_words = ["maoy", "Maoy", "buwagan", "Buwagan", "hilak", "Hilak", "hilaka", "Hilaka","depressed", "Depressed", "Sad", "sad", "guol", "Guola", "guola", "Guol"]

starter_encourage = ["Hang in there!", "Everything will be alright", "Don't worry I'm here for you", "You're a great person", "Cheer up!", "Ma okay ra tanan basta salig lang sa imo kaugalingon"]

morning_greet = ["Good morning", "ohayo", "Ohayo","good morning", "Maayong Buntag", "maayong buntag", "Magandang Umaga", "magandang umaga", "goodmorning", "Goodmorning"]

morning_message = ["Good morning", "Ohayo Gozaimasu", "Hello! Good morning", "Good morning how was your sleep?", "Good Morning. Did you sleep well?"]

haler_greets = ["hi bot", "Hi bot", "hi Bot", "Hi Bot", "Hi ging", "hi ging", "Hi Ging", "Hi ging", "Hi gingski", "Hi Gingski", "Hi Gingskiki", "hi ginsgski", "hi gingskiki", "Hi guys", "hi guys"]

orayt = ["Hi guyd", "Haluu", "Hiii", "Haluu guyd",]

Good_night = ["Good night", "matog nako", "tug nako", "Matog nako", "Tug nako", "Goodnight", "good night", "Goodnight", "Oyasumi", "Oyasuminasai", "Goodnight", "goodnight"]

Sleep = ["Good Night! Sleep Well", "Good Night! Sweet Dreams", "Good Night!", "Good Night! Sleep Tight"]

Tired_words = ["Kapoy", "Kapoya", "Kapoy nako", "kapoy", "kapoya", "kapoy nako", "Gikapoy" , "gikapoy", "Gikapoy nako", "gikapoy nako", "I'm tired", "Tired", "exhausted", "tired", "exhausting", "too much work", "grabe nga trabaho", "grabe na trabaho"]

Tired = ["Please rest Master!", "You did well today! Please take a rest", "Thank you for your hardwork! Please Rest", "Take a break and enjoy life", "You will get good things from your hardwork, so please rest"]

amen = ["Uli na ging", "uli na ging", "We miss you ging", "we miss you ging", "I miss you ging", "i miss you ging"]

nema = ["I miss you too", "Gimingaw nasab ko ninyo", "Kita raman gihapon ta puhon"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

  @client.event
  async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  username = str(message.author).split('#')[0]
  user_message = str(message.content)
  channel = str(message.channel.name)
  print(f'{username}: {user_message} ({channel})')

  if message.channel.name == 'general':
    if user_message.lower() == 'hi':
      await message.channel.send(f'Hello {username}! It is nice to see you')
      return

    if user_message.lower() =='bye':
      await message.channel.send(f"Bye! {username}! See ya!")
      return

    if user_message.lower() == 'i love you zero two':
      await message.channel.send(f'I love you too {username}!')

    if user_message.lower() == 'i miss you zero two':
      await message.channel.send(f'Oh how sweet! I missed you too {username}')

    if user_message.lower() == 'fuck you zero two':
      await message.channel.send(f'Fuck you too with all your life {username}')

    if user_message.lower() == 'i miss you':
      await message.channel.send(f'I missed you too {username}!')

    if user_message.lower() == 'kamusta naman si gio?':
      await message.channel.send(f'Okay raman, malipayon gihapon')

    if user_message.lower() == 'kamusta naman si giging?':
      await message.channel.send(f'Okay raman, malipayon gihapon')

    if user_message.lower() == 'hey':
      await message.channel.send(f'Oh Hello there {username}!')

    if user_message.lower() == 'i love you':
      await message.channel.send(f'I love you too {username} <3')

    if user_message.lower() == 'unsa ni ging?':
      await message.channel.send(f'I am the bot created by Gio Daguil. Nice to meet you!')

    if user_message.lower() == 'wow':
      await message.channel.send(f'Right? It is amazing!')

    if user_message.lower() == 'choya':
      await message.channel.send(f'Right? It is amazing')

    if user_message.lower() == 'chuya':
      await message.channel.send(f'Right? It is amazing')

    if user_message.lower() == 'kinsay nag himo nimo?':
      await message.channel.send(f'I am created by Sergio M. Daguil III my Darling')

    if user_message.lower() == 'who made you?':
      await message.channel.send(f'I am created by Sergio M. Daguil III my Darling')

    if user_message.lower() == 'who is your creator?':
      await message.channel.send(f'My creator is the one and only Sergio Mendola Daguil III')


    if user_message.lower() == 'who is ugly here?':
      await message.channel.send(f'No other than {username}. It is obvious')

    if user_message.lower() == 'kinsay maot diri?':
      await message.channel.send(f'No other than {username}. It is obvious')

    if user_message.lower() == 'how are you?':
      await message.channel.send(f'I am fine. Thank you!')

  msg = message.content

  if msg.startswith('!encourage'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in happy_words):
    await message.channel.send(random.choice(starter_supports))

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encourage))

  if any(word in msg for word in morning_greet):
    await message.channel.send(random.choice(morning_message))

  if any(word in msg for word in haler_greets):
    await message.channel.send(random.choice(orayt))

  if any(word in msg for word in Good_night):
    await message.channel.send(random.choice(Sleep))

  if any(word in msg for word in Tired_words):
    await message.channel.send(random.choice(Tired))

  if any(word in msg for word in amen):
    await message.channel.send(random.choice(nema))


keep_alive()
client.run(os.environ['Ahoy'])
