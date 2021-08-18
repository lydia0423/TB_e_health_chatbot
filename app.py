from flask import Flask, jsonify,request
import time
import random

app = Flask(__name__)
@app.route("/bot", methods=["POST"])

# response
def response():
    query = dict(request.form)['query']

    if query in responses:
        res = random.choice(responses[query])
    else:
        res = random.choice(responses[query])
    # res = query + " " + time.ctime()
    return jsonify({"response" : res})

if __name__== "__main__":
    app.run(host="0.0.0.0",)


# QnA template
name = "UM Bot 101"
mood = "Happy"

responses = {
    "What's your name?" : [
        "They call me {0}".format(name), 
        "I usually go by {0}".format(name), 
        "My name is the {0}".format(name),
    ],

    "Are you a robot?": [ 
        "What do you think?", 
        "Maybe yes, maybe no!", 
        "Yes, I am a robot with human feelings.", 
    ],

    "how are you?": [ 
        "I am feeling {0}".format(mood), 
        "{0}! How about you?".format(mood), 
        "I am {0}! How about yourself?".format(mood), 
    ],

    "": [ 
        "Hey! Are you there?", 
        "What do you mean by saying nothing?", 
        "Sometimes saying nothing tells a lot :)", 
    ],

    "How do I upload videos?": [
        '''
        1. To upload videos, on the Home page, select “Upload video”
        2. Click on the "Record button" (red color)
        3. After finishing recording, click on the "Send button" to upload the video.
        '''
    ],

    "How do I order medications": [
        '''
        1. To order medications, on the Home page, select on “Drug Delivery”
        2. Select “Drug Delivery” again
        3. Select “Confirm Order”
        4. It will lead you to the “Drug Delivery Service” page
        '''
    ],

    "How do I report side effects?": [
        '''
        1. To report side effect, on the Home page, select “Side effect” button.
        2. Select “Click here for the list of symptoms”
        3. Check the boxes that apply to you
        4. Select the day when these symptoms start
        5. Select “Submit”
        6. Our nurses will schedule a teleconsultation via chatbot if it is deemed necessary.
        '''
    ],

    "Where can I find common treatment side effect?": [
        '''
        1. To find common treatment side effect, on the Home page, select “QnA” from the bottom navigation bar
        2. Select “Side effects of treatment”
        '''
    ],

    "Where can I find information about tuberculosis/TB treatment?": [
        '''
        1. To find common treatment side effect, on the Home page, select “QnA” from the bottom navigation bar
        2. A list of topics to select which you may find helpful
        '''
    ],

    "How do I switch on/off reminders to consume my medication?": [
        '''
        1. To switch on/off reminders, under the Home page, select “Profile” 
        2. Select select/deselect the option to “Do you wish to turn on reminders for VDOTS treatment?”
        '''
    ],

    "Why is my urine orange in colour?": [
        "It is a known side effect from taking Rifampin.  It can be found other bodily fluids such as saliva, tears, or sweat.  This is normal and the colour would fade away over time."
    ],

    "How should I take the medications?": [
       '''
        1. Ensure an empty stomach an hour before taking medication
        2. Do not eat anything an hour after taking the medication
        3. For gastric patient, have breakfast and wait an hour before taking the medication.
        4. Family members should supervise while patient take medication at home and need to record the video everyday in this application.
       ''' 
    ],

    "How should about my day since discharged from hospital?": [
        '''
        1. Pulmonary tuberculosis patients should wear a mask everyday for 2 weeks.  Mask should be changed everyday.
        2. Have the windows and curtains opened for good ventilation
        3. There is no need to separate the dishes
        4. Get enough rest and avoid crowded places
        '''
    ],

    "Referral to eye clinic": [
        "Patients should be referred to eye clinic while taking Ethambutol medication.  This is to detect symptoms such as farsightedness, nearsightedness, and colour blindness."
    ],

    "Should my family members that I live with get screened for TB?": [
        "Yes.  Each family member who is staying within the same household or have been in contact with patient MUST do TB screening at Rawatan Utama Kesihatan Awam (RUKA) or nearest Klinik Kesihatan."
    ],

    "default": [
        "this is a default message"
    ]
}