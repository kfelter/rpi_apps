import pathlib, subprocess, sense_hat

p = pathlib.Path('.')

# run all files
deamons = list(p.glob('deamon/*.py'))

for script in deamons:
    subprocess.call(['python3 {0} &'.format(script.absolute())], shell=True)

# run one interactive app
apps = list(p.glob('interactive/*.py'))

# FSM to select interactive app
sense = sense_hat.SenseHat()

i = 0
sense.clear()
sense.show_message(apps[i].name, text_colour = (255, 0, 0))
while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up" and i < len(apps):
                i = i + 1

            if event.direction == "down" and i > 0:
                i = i - 1
                
            if event.direction == "middle":
                subprocess.call(['python3 {0}'.format(apps[i].absolute())], shell=True)

        sense.clear()
        sense.show_message(apps[i].name, text_colour = (255, 0, 0))

