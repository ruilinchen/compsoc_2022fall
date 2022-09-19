import zipfile as zipf
import os
import json

os.chdir("C:\\Users\\foolo\\OneDrive\\School\\2022\\compSoc\\Assignments\\Assignment_4")
# rename for easy handiling
zf_2019 = "MA_cbg_human_mobility_2019.zip"

# look into zip folder
with zipf.ZipFile(zf_2019, "r") as zf:
    # for every file in the list of files
    # see if file ends with csv and if it is in the window folder (not the MACOS one)
    # if yes, extract the file, can add "new folder" if needed
    # print file (with path)
    for file in zf.namelist():
        if file.endswith(".csv") and os.path.dirname(file) == "MA_cbg_human_mobility_2019":
            zf.extract(file)
            print(file)

# change working directory to the one just extracted
os.chdir(".\MA_cbg_human_mobility_2019")
# check working directory
print(os.getcwd())

# set working directory as variable
workcsvdir = os.listdir()


# define function to count lines
def countlines(workcsvdir):
    # set line counter to 0
    # create an empty dictionary
    nl = 0
    countdict = {}
    # for each file in the working dir
    # open the file and count the number of lines using len(file)
    # add new entry to dictionary with file name as key and number of lines as values
    # add on tally for line counter
    for csvfile in workcsvdir:
        if csvfile.endswith("csv"):
            with open(csvfile, "r") as f:
                lines = len(f.readlines())
            countdict[csvfile] = lines
            nl += lines
    print(f"total lines: {nl}")
    # write new json file with json.dump, store the new dictionary inside
    with open(".\countdict.json", "w") as nj:
        json.dump(countdict, nj, indent=2)
        print("new json file is created")


countlines(workcsvdir)
with open("countdict.json", "r") as f:
    example = json.load(f)
    print(example)
