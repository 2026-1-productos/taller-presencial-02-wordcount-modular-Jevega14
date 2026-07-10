import os


def read_all_lines(input_folder):
    all_lines = []
    input_file_list = sorted(os.listdir(input_folder))
    for filename in input_file_list:
        file_path = os.path.join(input_folder, filename)
        if not os.path.isfile(file_path):
            continue

        with open(file_path, "r", encoding="utf8") as f:
            lines = f.readlines()
            all_lines.extend(lines)
    return all_lines
