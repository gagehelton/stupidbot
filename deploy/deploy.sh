apt install python3-pip -y
pip3 install virtualenv -y
virtualenv ../stupidbot_env
source ../stupidbot_env/bin/activate
pip3 install -r ../requirements.txt
