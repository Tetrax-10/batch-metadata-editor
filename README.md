# Batch metadata editor

This python script removes all metadata from mp4, mkv files and sets the title and year tag from the file name in batch.

This is a sponsored project by [xxxxxxxxxxxxxxx]()

Need a website, tool, or script that you've always dreamed of having, contact me I will create it for you.

[u/Raghavan_Rave10](https://www.reddit.com/user/Raghavan_Rave10)

(or)

Send friend request to @tetrax10 on Discord, I will get in touch ASAP.

## Installation

1. Install python, make sure "Add python 3.xx to PATH" is checked while installing else it wont work.
2. Download the [latest version](https://github.com/Tetrax-10/batch-metadata-editor/releases/latest) of this script
3. Extract the zip and copy the `metadata-editor` folder to `C:\Program Files`
4. Now open start menu and search for `Edit environment variables for your account` and click the first result
5. Now select path and click edit, a new tab should open
   ![environment variables tab](/assets/environment-variables-tab.png)
6. In that new tab click `new` and paste this path `C:\Program Files\metadata-editor`, click ok, Done 🎉
   ![new-environment-variable](/assets/new-environment-variable.png)

## How to run it?

1. Open terminal and run

```sh
python "C:\Program Files\metadata-editor\script.py"
```

2. It will ask for path, So give the file or folder path of your video(s) as the input.

for **batch processing** give folder path. example: `D:\Media\movies`

for single file metadata editing give video file (mp4 or mkv) path. example: `D:\Media\movies\Oldboy 2160p DC [2003]`
