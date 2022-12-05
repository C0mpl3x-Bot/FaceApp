Instructions


To run this app you would need to install the following:


-First install pip


-Then install pipenv by doing 

    	- pip install pipenv


-Then open pipenv shell by typing pipenv shell into the zsh terminal in Visual Studio Code

-Then install dlib By doing the following 

		- git clone https://github.com/davisking/dlib.git

		- cd dlib 

		- mkdir build; 

		- cd build; 

		- cmake ..; 

		- cmake --build .

		- cd ..

		- python3 setup.py install


-Then download CMAKE by doing 

		- /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"


-Then do 

		- brew install cmake


-Then get out of the dlib folder and go back to the FaceApp folder by doing 

		- cd ..


-Then install face_recognition by doing 

		- pipenv install face_recognition
	

-Then install CV2 by doing 

		- pip install opencv-python


-Then install numpy by doing 

    	- pip install numpy


-Then install os by doing 

   		- pip install os-sys


To run the application you would need to run the LoginWindow.py file by doing python LoginWindow.py and the app will run Run the app whilst in the pipenv shell. To be able to use the app remove the photo from the img/knownAdmin folder. This is because if there is a file within the knownAdmin folder then the app would not let you signup and you cannot login as well preventing you from using the application.

I have also added a PDF of my report on this project which can be found within this repo.
		