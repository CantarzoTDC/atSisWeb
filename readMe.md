# Before you run the project 

All the command lines below are to be ran on the Command Prompt (cmd) or the IDE's terminal, preferably in the project root folder

## Create the Virtual Enviroment  

The folder's name can be anything, we are using 'venv' just as a standard, but you are allowed to use whatever.  

### Using Python' inate Script
- python venv venv  

### Using the Virtualenv module
- virtualenv venv  

## Activate Virtual Enviroment (venv)
- .\venv\Scripts\activate 
    - if done right, it should show (venv) (root)/(project-folder)> on terminal
- deactivate (terminates venv)

**Obs:**  
Prefer to install the desired/needed packages/modules/requirements after activating the virtual enviroment, so that it is only installed for **this** project specificaly

## Install required modules/packages  
If you have a 'requirements.txt' file
- pip -r install requirements.txt

Else, you may install each of the needed modules individualy.  


