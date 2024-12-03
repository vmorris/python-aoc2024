import os
import pathlib

import click
from jinja2 import Environment, PackageLoader, select_autoescape

year = 2024


@click.command()
@click.argument("day")
def newday(day):
    """Create new day in advent of code."""
    if len(day) == 1:
        day = f"0{day}"
    click.echo(f"Creating new environment for day {day} ...")
    solution_path = os.path.abspath(f"aoc2024/day{day}")
    test_path = os.path.abspath(f"tests")

    # render from templates
    env = Environment(
        loader=PackageLoader("newday"),
        autoescape=select_autoescape(),
    )
    solution_template = env.get_template("solution.py.j2")
    test_template = env.get_template("_test_day.py.j2")
    solution_render = solution_template.render(day_number=day, year=year)
    test_render = test_template.render(day_number=day, year=year)

    # initialize solution and test for given day
    try:
        os.mkdir(solution_path)
        pathlib.Path(solution_path, "input").touch()
        with open(os.path.join(solution_path, "solution.py"), "w") as f:
            f.write(solution_render)

        pathlib.Path(test_path, f"testinput.day{day}").touch()
        with open(os.path.join(test_path, f"test_day{day}.py"), "w") as f:
            f.write(test_render)
    except FileExistsError as exc:
        print(exc)
        exit(1)
