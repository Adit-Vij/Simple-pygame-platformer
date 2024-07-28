# Sample Game Using pygame

## Dependencies
This project requires pygame to execute, to install it simple type or copy the following command: 
```pip install pygame``` 
verify the installtion using the command: 
```pip show pygame``` 

> NOTE: Please make sure you have Python installed properly on your system before running the scripts

## Project Structure
### Source Code
All the python scripts are present in the "Scripts" folder, which can be found in the "Src" folder.

- **Driver Script:** The window and the main loop is run by the ```MainWindow.py``` script.
- **Player Script:** The Player's logic is defined in the ```Player.py``` script. It has basic movements like: moving left, right jumping and some other movements like: jump dash
- **Obstacle Script:** The Obstacle script contains the obstacle class, so that it's properties like dimesnsions can be modified and multiple instances can be crteated.

## Running the game
- Open a terminal in the Src/Scripts folder of the project after downloading the project code and unzipping it.
- Type ```python MainWindow.py``` to run the game.