import os
import re
import sys
import subprocess
from pathlib import Path


def colored(text, color):
    if color == "blue":
        return f"\033[94m{text}\033[0m"
    elif color == "green":
        return f"\033[92m{text}\033[0m"
    elif color == "red":
        return f"\033[91m{text}\033[0m"


def run_cmd(cmd):
    return subprocess.run(cmd, check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)


def check(cmd):
    output = run_cmd(cmd)
    if ("not recognized" in output.stderr):

        unavailable_tool = ""
        if ("atomicParsley" in output.stderr):
            unavailable_tool = "AtomicParsley"
        else:
            unavailable_tool = "mkvpropedit"

        print(colored(f"{unavailable_tool} not found!", "red"))
        print()
        print(f"Please add \"{r"C:\Program Files\metadata-editor"}\" to PATH environmental variable")
        print(colored("Tutorial: https://github.com/Tetrax-10/batch-metadata-editor?tab=readme-ov-file#installation", "blue"))
        print()

        return False

    return True


def get_file_name(file, type="name"):
    if type == "ext":
        return Path(file).suffix[1:]
    else:
        return Path(file).stem


def get_all_video_files(path):
    video_files = []
    video_extensions = ["mp4", "mkv"]

    if os.path.isfile(path):
        video_files.append(Path(path))
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                extension = get_file_name(file, "ext").lower()
                if extension in video_extensions:
                    video_files.append(Path(root) / file)
    else:
        print("Input path does not exist")
        return False

    return video_files


def extract_movie_info(filename):
    pattern = re.compile(r'^(\S+(?:\s+\S+)*) (\d+p) \[(\d{4})\]$')
    match = pattern.match(filename)

    if match:
        movie_name, movie_resolution, movie_year = match.groups()
        return [movie_name, movie_resolution, movie_year]
    else:
        return False


if __name__ == "__main__":
    print()
    if not check("mkvpropedit --version") or not check("atomicParsley -v"):
        sys.exit()

    input_path = input(colored("Enter file or folder path: ", "blue"))
    print()

    video_files = get_all_video_files(input_path)
    if video_files != False and len(video_files) > 0:
        for video_file in video_files:
            file_base_name = os.path.basename(video_file)
            file_name = get_file_name(video_file)
            file_extension = get_file_name(video_file, "ext").lower()

            movie_info = extract_movie_info(file_name)
            if (movie_info != False and len(movie_info[0]) and len(movie_info[2])):
                movie_name, movie_resolution, movie_year = movie_info

                if (file_extension == "mkv"):
                    run_cmd(f"mkvpropedit \"{video_file}\" --tags all:")  # removes all metadata
                    run_cmd(f"mkvpropedit \"{video_file}\" --edit info --set \"title={movie_name + " " + f"[{movie_year}]"}\" --set \"date={movie_year}-01-01T00:00:00+00:00\"")
                elif (file_extension == "mp4"):
                    run_cmd(f"AtomicParsley \"{video_file}\" --overWrite --metaEnema")  # removes all metadata
                    run_cmd(f"AtomicParsley \"{video_file}\" --overWrite --title \"{movie_name + " " + f"[{movie_year}]"}\" --year {movie_year}")

                print(colored(f"Done: {file_base_name}", "green"))
            else:
                print(colored(f"Unsupported naming convention: {file_base_name}", "red"))
                continue
    else:
        print(colored("No videos found in the specified folder", "red"))

    print()
