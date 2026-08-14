
def fnc_lines() -> None:
    with open('collect_proj_files.txt', 'r', encoding='UTF-8') as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith('File:'):
            line = line.strip()
            line = line.split("\\/")
            print(line)


fnc_lines()
