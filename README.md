# MyAngelSight
### Project that looks at the behavior of a driver to detect if they are distracted
The goal of our project to help reduce distracted driving by providing positive reinforcements to drive safe. This tool can be used by companies like insurance companies to predict the risk factor of drivers and reward drivers that are safer. Driver privacy is a concern in a tool that is constantly recording a driver, so we are careful to process all of our image data locally before sending the final score over to the cloud. For the purposes of this demo, we have a day set to 30 seconds, where a good driver starts the day with 50 points and can earn a maximum of 100 points a day and a minimum of 0 points, depending on their level of distraction. After the driver earns a certain number of points, they would be elegible for extra cash back on their credit cards.
## Technical Details
This project uses a camera from a computer or a Raspberry Pi fitted into a device. We took advantage of the OpenCV library and a convolutional neural network to detect what a human looks like when they are facing the road versus when they are looking away from the road.
This app also integrates with [TSYS developer API](https://developers.tsys.com/) to keep track of user rewards to help reward them with extra credit card rewards for safe driving.
We connect our face detection library (written in Python) to a [Google Compute Function](https://cloud.google.com/functions/) to process the data and send it to our database and to the API we are writing to. 

![Distracted Person](Site/images/noFaceDetected.png?raw=true "Person is distracted")
Here is an image of a driver that is distracted. We looked at certain facial points to detect the direction of a person to see if they are facing forwards or not.
![Not Distracted Person](Site/images/faceDetected.png?raw=true "Person is not distracted")
Here is an image of a driver that is not distracted. As you can see, the facial points show the direction of the persons eyes as forward.


## How to set-up

#### OpenCV
1. Install [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
1. `cd OpenCV`
1. `source .env`
1. `python head_pose_estimation.py`
#### GCP Function
1. Create a [GCP account](https://cloud.google.com/functions/)
1. Deploy the code in the `Lambda` folder using the steps on Google Cloud Functions to upload a function
1. Deploy a datastore using GCP to store a username and score (we used a MySQL database to test with)
1. Test the function using the GCP tester

#### Front-end
1. All code for the site is in the `Site` folder
1. We used Netlify to host our static product page/demo site. This is hosted [here](https://myangelsight.com/).


### Team:
[Natalie Wilkinson](https://nwilkinson.me/)
[Sanjana Jampana](https://github.com/sanjujampana/)
[Alberto Li](https://albertoli.tech/)
[Yash Tulsiani](https://ytulsiani.com/)
