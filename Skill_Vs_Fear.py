import numpy as np
import csv
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap



#Count the ammount of skills and fears for each one
with open('SkillLevel.csv') as content_file:
    content = content_file.read()
    #using the skill variable as a list down low. Not sure if i'll need this stuff but I left it here
    #skill = content.count("Technically Savvy:   I know my way around a computer pretty well. When anyone in my family needs technical help, I'm the one they call.")

with open('SkillLevel.csv') as content_file:
    content = content_file.read()
    average = content.count("Average User:   I know enough to get by.")

with open('SkillLevel.csv') as content_file:
    content = content_file.read()
    nerd = content.count("Ultra Nerd:  I build my own computers, run my own servers, code my own apps. I'm basically Mr. Robot.")

with open('SkillLevel.csv') as content_file:
    content = content_file.read()
    Luddite = content.count("Luddite:  Technology scares me! I only use it when I have to.")


with open('BiggestFear.csv') as content_file:
    content = content_file.read()
    privacy = content.count("The loss of privacy")

with open('BiggestFear.csv') as content_file:
    content = content_file.read()
    loseTouch = content.count("We'll lose touch with one another")

with open('BiggestFear.csv') as content_file:
    content = content_file.read()
    noFear = content.count("I have no fears about a more connected future")

with open('BiggestFear.csv') as content_file:
    content = content_file.read()
    lessSafe = content.count("We'll be less safe")


#Be able to look at the data and assign each point to a list. Skill holds skills and fear holds biggest fears
o = open('BiggestFear.csv')
skill = []
fear = []
csv_o = csv.reader(o)
for row in csv_o:
	skill.append(str(row[0]))
	fear.append(str(row[1]))
	#if (fear[-1] == "The loss of privacy"):
o.close()



TechPrivacy = 0
TechLoseTouch = 0
TechLessSafe = 0
TechNoFear = 0
TechOther = 0

for value in range(len(skill)):
	if (skill[value] == "Technically Savvy:   I know my way around a computer pretty well. When anyone in my family needs technical help, I'm the one they call."):
		if (fear[value] == "The loss of privacy"):
			TechPrivacy += 1
		elif (fear[value] == "We'll lose touch with one another"):
			TechLoseTouch += 1
		elif (fear[value] == "We'll be less safe"):
			TechLessSafe += 1
		elif (fear[value] == "I have no fears about a more connected future"):
			TechNoFear += 1
		elif (fear[value] == "Other (please specify)"):
			TechOther += 1
fruits = ["Tech Savy/No Privacy", "Tech Savvy/Lose Touch", "Tech Savvy/Less Safe", "Tech Savvy/None Fear", "Tech Savvy/Other"]

p = figure(x_range=fruits, plot_height=350, title="Fruit Counts",
           toolbar_location=None, tools="")

p.vbar(x=fruits, top=[TechPrivacy, TechLoseTouch, TechLessSafe, TechNoFear, TechOther], width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)
output_file("Skill_Vs_Fear.html", title="Skill Level Vs Biggest Fear")