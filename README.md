Git Chess Game
===================================

I am going to propose a realistic and detailed scenario of collaborative work in a Git project for a chess game in Python, where each programmer (killer1, killer2, killer3 and killer4) contributes. The game code will include advanced programming concepts, such as classes, design patterns (e.g., state pattern), error handling, and efficient data structures.

## Scenery
### Project requirements
* A [ Git repository](https://www.git-tower.com/learn/ebook)  that all programmers work on..

* Each programmer develops a part of the game (board, pieces, movement logic, and turn control).

* Use of Git for version control, including branches, merge, conflict resolution, and error handling in commits. 

### Step 1: Repository Initialization


killer1 creates a repository in Git and uploads a basic structure.

```bash 
# killer1
git init chess-game
cd chess-game
touch README.md main.py
git add README.md main.py
git commit -m "Initial commit with basic structure"
git remote add origin https://github.com/killer1/chess-game.git
git push -u origin master

```

### Step 2: Creating branches for each part of the project

Each programmer has his branch. killer1 creates the branches and assigns tasks:


* killer1: Create the game controller.
* killer2: Deploy the dashboard.
* killer3: Implement the pieces.
* killer4: Manage the rules and the game turn.

```bash 
# killer1
git branch controller
git branch board
git branch pieces
git branch rules
git push origin controller board pieces rules
```

### Step 3: Development of each programmer

killer1 works in game controller:

```python 
# killer1 en la rama 'controller'
class GameController:
    def __init__(self):
        self.board = None
        self.players = []

    def start_game(self):
        self.board = ChessBoard()
        self.players = [Player("White"), Player("Black")]
        print("Game started!")

```
```bash 
git checkout controller
git add main.py
git commit -m "Game controller class with start_game method"
git push origin controller

```

killer 2 works on the Chess Board class in the board branch:
```python 
# killer2 en la rama 'board'
class ChessBoard:
    def __init__(self):
        self.grid = self.create_board()

    def create_board(self):
        return [["" for _ in range(8)] for _ in range(8)]

    def display_board(self):
        for row in self.grid:
            print(row)


```

```bash 
git checkout board
git add main.py
git commit -m "ChessBoard class with create_board and display_board methods"
git push origin board


```

killer4 manages the game rules in the rules branch:

```python 
# killer4 en la rama 'rules'
class TurnManager:
    def __init__(self):
        self.turn = 0

    def next_turn(self):
        self.turn += 1
        print(f"Turn {self.turn}: Now it's {'White' if self.turn % 2 == 1 else 'Black'}'s turn")

```

```bash 
git checkout rules
git add main.py
git commit -m "TurnManager class with next_turn method"
git push origin rules
```
### Step 4: Integration of the branches

killer1 tries to merge all branches into master to integrate the game.

```bash 
git checkout master
git merge controller
git merge board
git merge pieces
git merge rules
```
Merge error between killer1 and killer3

While merging pieces, a merge conflict occurs between killer1 and killer3 in main.py:

```bash 
Auto-merging main.py
CONFLICT (content): Merge conflict in main.py

```
killer1 resolves the conflict manually in main.py (for example, by fixing duplicate lines).

```bash 
git add main.py
git commit -m "Merge conflict resolved between controller and pieces"

```

### Step 5: Testing and bug fixing


All programmers work together to fix bugs, perform tests, and make final adjustments. For example, if killer2 finds an error in the way the board is drawn:

```bash 
# killer2 corrige un bug en 'ChessBoard'
git checkout board
# Actualiza el método display_board
git add main.py
git commit -m "Fixed display_board method to properly print the chessboard"
git push origin board

```

After fixing the errors, everyone merges their branches back to master, pushing and verifying the final operation.

### Step 6: Using Advanced Git

* Rebase: If killer4 is behind on work and your branch is out of date, you can do a rebase to keep up to date:

```bash 
git checkout rules
git rebase master

```

* Stash: If killer1 has to switch branches without losing its current work:

```bash 
git stash
git checkout pieces

```
### Step 7: Project Completion
When everything is ready, killer1 merges the final branches and tags version 1.0 of the game:


```bash 
git checkout master
git merge board
git merge pieces
git merge rules
git tag -a v1.0 -m "First release of Chess Game"
git push origin --tags

```

Advanced commands

==================

To work collaboratively and efficiently with Git on a project like the Python chess game, you could use more advanced commands that allow you to perform more refined version control, manage large changes, and avoid problems during merges. Here is a list of commands, combinations and variants applied to the chess example, as well as some strategies for their use:

### 1. Cloning and initial configuration of the repository

When working as a team, the first thing is to clone the repository:


```bash 
git clone https://github.com/killer1/chess-game.git
cd chess-game

```
Additionally, it is good practice to configure your user in Git (if you haven't already):

```bash 
git config --global user.name "killer1"
git config --global user.email "killer1@example.com"

```

2. Working with branches

It is always good practice to work in branches for each new feature or major change, to avoid breaking the code in master.

- Create a new branch to implement a chess move (e.g. the bishop move):

```bash 
git checkout -b feature-bishop-move

```

- Push this new branch to the remote repository:


```bash 
git push -u origin feature-bishop-move

```

3. Add and commit changes

- Check which files have been modified:

```bash 
git status

```
- Add only the files you want to commit (for example, only changes related to the bishop's movement):

```bash 
git add bishop.py
```

- Confirm the changes with a clear and descriptive message:

```bash 
git add bishop.py
```

If you want to combine several steps (add and confirm at the same time):

```bash 
git commit -am "Fixed display bug in chessboard and implemented bishop movement"

```


A way to think about Git and Github.
------------
Milestones of milestones of milestones. In other words:

- Open up a text editor.
- Type "Hello World".
- Save this file.
  - You have now created a "milestone" on your hard drive of this text.
	- You can now retreive that milestone by double clicking it to re-open it in your text editor.
	- This should be a concept you already understand quite well.
- Change the contents of that file again. Add in your own text. Save it again.
	- By saving it again you've overwritten the previous milestone.
	- You can certainly redo the work (e.g. replacing all the text with "Hello World" and saving again) but the original work is gone otherwise.
- Git saves milestones of milestones.

		git commit -am "By typing this command I am saving a collection of saved files."

- This is great because now we can roll back to old versions of files without having to retype. Aka "source control".
- However, wouldn't it be great if we could further save milestones in the cloud?
	- Aka milestones of milestones of milestones.
		- Github -> Git -> Save
- Github is two things:
	- git, in the cloud
	- a social network around source code
- All you need to do to push to Github:

		git push origin master

- Now one could "clone" that repository on another computer and not just get the latest code but the complete revision history on another computer.



Setting up
------------
Assuming your project is in a folder named "Project" on your Desktop.

### Starting from scratch
	cd ~/Desktop/Project
	git init
	git checkout -b develop
	touch README.md

- Open the README.md file you just created in your text editor. Describe your project. I've provided a basic template below for what it's worth. Save it.
- Go to Github (or Bitbucket or whereever you want to save your code in the cloud). Create a new project.
	- If you're on Github, ***do not check*** Initialize this project with a README since you just made one.
- Determine your SSH clone url. On Github it's probably something like ***git@github.com:USERNAME/PROJECT.git***. Should be on the project's page somewhere.
- Add your remote.
	
		git remote add origin {{the link you just copied}}

- Breaking that down
	- git :: The git command
	- remote add :: We're adding a remote connection for this repository
	- origin :: We're naming the remote "origin". You can also call this "github" or "bananasauraus" if you'd like.


### Cloning an existing repository.

- Determine your SSH clone url. On Github it's probably something like ***git@github.com:USERNAME/PROJECT.git***. Should be on the project's page somewhere.

		cd ~/Desktop
		git clone {{the link you just copied}} Project

- This creates a directory named "Project", clones the repository there and adds a remote named "origin" back to the source.

		cd Project
		git checkout develop

- If that last command fails

		git checkout -b develop

Updating/The Development Cycle
------------
You now have a git repository, likely with two branches: master and develop. Now bake these laws into your mind and process:

####You will never commit to ***master*** directly.
####You will never commit to ***develop*** directly.

Instead, you will create ***feature branches*** on your machine that exist for the purpose of solving singular issues. You will always base your features off the develop branch.

		git checkout develop
		git checkout -b my-feature-branch

This last command creates a new branch named "my-feature-branch" based off of develop. You can name that branch whatever you like. You should not have to push it to Github unless you intend to work on multiple machines on that feature.

Make changes.

	git add .
	git commit -am "I have made some changes."

This adds any new files to be tracked and makes a commit. Now let's add them to develop.

	git checkout develop
	git merge --no-ff my-feature-branch
	git push origin develop

Releasing
------------
Finished with your project?

- Create a feature branch as normal.
- Update the version history in the README.md file
- Update this to develop as normal.

		git checkout master
		git merge --no-ff develop
		git push origin master
		git tag v1.0.0
		git push origin v1.0.0

Replace 1.0.0 in the snippet here with your appropriate versions. Now you have a tag saved.