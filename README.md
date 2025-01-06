***<p align=center style="text-align:center; font-family:'Jaini Purva'">![image info](assets/obsidian_with_transparent_background.png)</p>***

# ***<p align=center">Obsidian Synchronizer</p>***

Installation Steps:
1. Install python (https://www.python.org/downloads/) and git (https://git-scm.com/downloads)
2. Create git repo for your vault (on Github, Github etc.)
3. In your vault's location init your repo:

```
git init
git remote add origin link-to-your-repo # (e.g. https://github.com/SpeedfireV/test.git)
git branch -M main
git add .
git commit -m 'init'
git push --set-upstream origin main
```

4. Copy THIS repo to your local machine `git clone https://github.com/SpeedfireV/obsidian_synchronizer.git`
5. Run `pip install -r requirements.txt` in this copied repo location to install required dependencies
6. Go to _repo_info.env_ and change data accordingly with instruction inside the file

**AND NOW YOU CAN RUN SUCCESSFULLY YOUR SYNCHRONIZER BY CALLING `py main.py`!🥳🥳🥳**, But...

You can also automate synchronizer to run each time you run the device you work on. To do so:

For Windows:
1. Open **Task Scheduler** (`Win + R`, type `taskschd.msc`, and press Enter).
2. Click **Create Basic Task** in the right panel.
3. Follow the wizard:
- **Name**: Enter a name for the task (e.g., Run My Script).
- **Trigger**: Select When I log on.
- **Action**: Select Start a Program.
- **Program**: Enter the path to your Python executable (e.g., `C:\Python310\pythonw.exe` OR your **venv**'s Python executable `C:\...\obsidian_repo_synchronizer\.venv\Scripts\pythonw.exe`!).
- **Add arguments**: Enter the path to your script, e.g., `C:\...\obsidian_repo_synchronizer\main.py`.
- **Run inside**: Enter the path to your script location, e.g., `C:\...\obsidian_repo_synchronizer\`.
4. Click **Finish**.