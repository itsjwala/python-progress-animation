import os


def generate_progress_bars():
    """
        function used for creating the progress bars shown below <progress_bars>
        customize the length of <progress_bar> with appending or removing '#'
    """
    progress_bar = "##########################"
    progress_bars = []

    for i in range(len(progress_bar)):
        progress_bars.append(progress_bar[0:i] + progress_bar[i:].replace('#', '.'))
    progress_bars.append(progress_bar)

    return progress_bars


progress_bars = [
    "[..........................]",
    "[#.........................]",
    "[##........................]",
    "[###.......................]",
    "[####......................]",
    "[#####.....................]",
    "[######....................]",
    "[#######...................]",
    "[########..................]",
    "[#########.................]",
    "[##########................]",
    "[###########...............]",
    "[############..............]",
    "[#############.............]",
    "[##############............]",
    "[###############...........]",
    "[################..........]",
    "[#################.........]",
    "[##################........]",
    "[###################.......]",
    "[####################......]",
    "[#####################.....]",
    "[######################....]",
    "[#######################...]",
    "[########################..]",
    "[#########################.]",
    "[##########################]"

]

done = False


def show_progress():
    """
        function that loops through the <progress_bars> array until done is set to True
    """
    os.system(r'printf "The task is in progress, please wait a few seconds\n" ')
    while not done:
        for progress_bar in progress_bars:
            os.system(r'printf "\r{} Processing..." '.format(progress_bar))
            os.system("sleep 0.1")
    os.system(r'printf "\rDone!" '.format(progress_bar))
