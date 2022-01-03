import pathlib, subprocess, sense_hat, getopt, sys

proj_path = '.'
run_deamons = False

opts, args = getopt.getopt(sys.argv, 'hpd')
for opt, arg in opts:
    if opt == '-p':
        proj_path = arg
    elif opt == '-d':
        run_deamons = True

p = pathlib.Path(proj_path)

# run all files
deamons = list(p.glob('deamon/*.py'))

if run_deamons:
    for script in deamons:
        subprocess.call(['python3 {0} &'.format(script.absolute())], shell=True)

# run one interactive app
apps = list(p.glob('interactive/*.py'))

# FSM to select interactive app
sense = sense_hat.SenseHat()

i = 0
sense.clear()
sense.show_message(apps[i].name, text_colour = (0, 255, 0), scroll_speed=0.05)
while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "down" and i < len(apps):
                i = i + 1

            if event.direction == "up" and i > 0:
                i = i - 1
                
            if event.direction == "middle":
                subprocess.call(['python3 {0} &'.format(apps[i].absolute())], shell=True)
                sys.exit()

    sense.clear()
    sense.show_message(apps[i].name, text_colour = (0, 255, 0), scroll_speed=0.05)

