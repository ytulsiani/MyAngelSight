# MyAngelSight
## Project that looks at the behavior of a driver to detect if they are distracted
This project uses a camera from a computer or a Raspberry Pi fitted into a device to see if a driver is paying attention to the road and is not distracted by looking on their cell phone, looking in their back seat, or falling asleep. We took advantage of the OpenCV library and a convolutional neural network to detect what a human looks like when they are facing the road versus when they are looking away from the road.
This app also integrates with [TSYS developer API](https://developers.tsys.com/) to keep track of user rewards to help reward them with extra credit card rewards for safe driving.
We connect our face detection library (written in Python) to a [Google Compute Function](https://cloud.google.com/functions/) to process the data and send it to our database and to the API we are writing to. 



## How to set-up

#### OpenCV
1. Install [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
1. Run `source .env`
1. Run `python head_pose_estimation.py`
#### GCP Function
1. Create a [GCP account](https://cloud.google.com/functions/)
1. Deploy the code in the function folder using the steps on Google Cloud Functions to upload a function
1. Deploy a datastore using GCP to store a username and score (we used a MySQL database to test with)
1. Test the function using the GCP tester

#### Front-end
TBD


### Team:
Natalie Wilkinson (@natwilkinson)
Sanjana Jampana (@sanjujampana)
Alberto Li (@albertoli)
Yash Tulsiani (@ytulsiani)