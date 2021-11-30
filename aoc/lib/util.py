import inspect
from pathlib import Path


def get_problem_input(strip: bool = True, test: bool = False) -> str:
    """
    Get problem input automagically, solution file is inferred from the call stack

    Input files are located in the `solution/inputs` folder

    Note that input files have to be named /day{n}/a|b.txt
    """

    caller_file = inspect.stack()[1].filename

    part = Path(caller_file).stem.split(".")[0]
    day = Path(caller_file).parent.stem
    input_path = (
        Path(caller_file).parent.parent
        / "inputs"
        / day
        / f"{part}{'.test' if test else ''}.txt"
    )

    with open(input_path) as f:
        content = f.read()

    if strip:
        content = content.strip()

    return content
