To run our program we use python which comes from our main installation into our system.

This is not a good practice. A good practice is to have a virtual environment which will have clean installation of python which will be used only for our application.So in this installation we will install the libraries according to our own need to run our application

So we need to create virtual environment , we will issue a command:
			 pip install virtualenv.
Now we need to create virtual environment which should be created at same level at which our main application in stored .For this we issue a command :
			python -m venv virtual

venv is the name of the library of virtual module, -m  is an argument which allows python to locate modules for execution as scripts, virtual is name of folder where virtual environment file would be stored

Then to run any python script of our application we issue the command:
		virtual/bin/python script_name.py ,    virtual/bin/python this is location where python installation comes for our virtual environment

To install any library according to our requirement we use(say flask) :
		virtual/bin/pip install flask

