The scripts are written such that you need to run them from the respective year directory.
Otherwise, they will not find the input files.  
Remember that most participants get different input data so the results in the comments and unit tests will likely be different from yours.  
I use python 3.10, and I think you need at least Python 3.9 to run these scripts.
This is how I set up my virtual environment with `venv`:
```
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

I wrote the little helper `aoc.py` which creates a solution template and downloads the input data for a given day.
The optional arguments are `year` and `day` with the current year and day as default values.  
Example: `./aoc.py 2020 7`  
For it to be able to download the input data you need to have your session cookie stored in the file `secrets.json` in the root of this repository.
Remember that the session cookie expires after a month.
You can get your current one from the website while being logged in.
In Firefox: Right click -> Inspect Element -> Storage tab.
