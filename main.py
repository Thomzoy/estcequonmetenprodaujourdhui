import datetime
import glob
import os
import pathlib
import random


def define_env(env):
    @env.macro
    def get_image_and_title():

        weekday = datetime.datetime.today().weekday()
        pick_from = glob.glob(f"docs/{weekday}/*")
        pick = random.choice(pick_from)
        files = glob.glob(os.path.join(pick, "*"))

        for f in files:
            if f.endswith(".txt"):
                with open(f, "r") as title:
                    title_str = title.read()
            else:
                image = f

        image_path = pathlib.Path(image)
        return (
            pathlib.Path(*image_path.parts[1:]),
            title_str,
        )
