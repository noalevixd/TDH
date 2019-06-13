import wikipediaapi

class Character(object):
    def __init__(self, name, line,gender,house):
        self.name = name
        self.lines = [line]
        self.wordCounte =0
        self.gender=gender
        self.house=house

wiki = wikipediaapi.Wikipedia('en')
mutcd = wiki.page('List_of_Game_of_Thrones_characters')
characters = mutcd.section_by_title('Main characters')
main_characters=[]
houses=['Targaryen','Stark','Lannister','Greyjoy','Arryn','Baratheon','Tully','Tyrell']
for character in characters.sections:
     name = character.title
     for house in houses:
         if (house in name):
             ch_house=house
     if("She" in character.text or 'she' in character.text):
         gender = 'Female'
     elif ("He" in character.text or 'he' in character.text):
         gender= 'Male'
     else:
         gender=' '
     new_character = Character(name,' ',gender,ch_house)
     main_characters.append(new_character)


for c in main_characters:
    print ('Name: '+c.name)
    print('Gender: '+ c.gender)
    print('House: '+c.house)



