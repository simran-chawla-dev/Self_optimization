This template folder will save you the hassle of starting a new project from scratch.

To take advantage of this template folder, you should copy it and rename it to your new project.

1) Open up your command prompt (e.g. ssh in from your computer or open up a new Terminal session)

2) Navigate to the jupyter/tutorials folder (i.e. the folder that contains the template folder)

3) Replace new_app_folder_name with your new folder name and run the command in the command line:

cp -r template ../notebooks/new_app_folder_name

4) Update your text_ux.py file's first line.
The first line in the script is #TESTWITH workflows/1.0
#TESTWITH is required to specify the kernel you are using for testing.
The default kernel, workflows/1.0, may not have all the libraries you are using.
This means your tests will fail! 

Be sure to update the kernel if you are using anything other than the workflows kernel.
e.g. #TESTWITH matsci/1.2

5) You're all set! Navigate to your newly copied folder and start developing your application.
