# GENAI-

# create a Ec2 instance

# configure the ubantu  machine

# Launch the instance

# AWS UBANTU COMPILE CODE
sudo apt update

sudo apt install python3-pip -y

sudo apt -get update

sudo apt upgrade -y

sudo apt install git curl unzip tar make sudo vim wget -y

# clone the Git repo

git clone https://github.com/RisAhamed/GENAI-.git

to check type-  ls

change the directory to the genai -- cd GENAI

# create a file to upload the env variables -- openai api key

touch .env

# To open the file in vi editor 
type - vi .env
and click the  insert button and  type  the env  variable like openai_appi_key in it

and add the press the esc button to save the variables in the .env file 

and type :wq to exit the page

to check the update type - cat.env

now istall all the requiremnets-
---if windows or mac machine the type -- pip3 install -r requirements.txt
---if ubantu or linux  machine  then type -- pip install -r requirements.txt

# to run the application

python3 -m streamlit run app.py


