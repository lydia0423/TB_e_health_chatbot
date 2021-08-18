from flask import Flask, jsonify,request
import random

app = Flask(__name__)
@app.route("/bot", methods=["POST"])

# response
def response():
    query = dict(request.form)['query'].lower()

    ques = related(query)

    if ques in responses:
        res = random.choice(responses[ques])
    else:
        res = random.choice(responses[ques])

    return jsonify({"response" : res})

def related(x_text): 
    if "name" in x_text: 
        y_text = "what's your name?"
    elif "robot" in x_text: 
        y_text = "are you a robot?"
    elif "how are" in x_text: 
        y_text = "how are you?"
    elif "video": 
        y_text = "how do I upload videos?"
    elif "order medications":
        y_text = "how do I order medications"
    elif "report":
        y_text = "how do I report side effects?"
    elif "treatment":
        y_text = "where can I find common treatment side effect?"
    elif "tb":
        y_text = "where can I find information about tuberculosis/TB treatment?"
    elif "reminders":
        y_text = "how do I switch on/off reminders to consume my medication?"
    elif "orange color":
        y_text = "Why is my urine orange in colour?"
    elif "how to take":
        y_text = "how should I take the medications?"
    elif "discharged":
        y_text = "how should about my day since discharged from hospital?"
    elif "eye clinic":
        y_text = "referral to eye clinic"
    elif "family":
        y_text = "should my family members that I live with get screened for TB?"
    elif "default":
        y_text = "this is a default message"
    elif " ":
        y_text = ""
    else: 
        y_text = ""
    return y_text

if __name__== "__main__":
    app.run(host="0.0.0.0",)


# QnA template
name = "UM Bot 101"
mood = "Happy"

responses = {
    "what's your name?" : [
        "They call me {0}".format(name), 
        "I usually go by {0}".format(name), 
        "My name is the {0}".format(name),
    ],

    "are you a robot?": [ 
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

    "how do I upload videos?": [
        '''
        1. To upload videos, on the Home page, select “Upload video”
        2. Click on the "Record button" (red color)
        3. After finishing recording, click on the "Send button" to upload the video.
        '''
    ],

    "how do I order medications?": [
        '''
        1. To order medications, on the Home page, select on “Drug Delivery”
        2. Select “Drug Delivery” again
        3. Select “Confirm Order”
        4. It will lead you to the “Drug Delivery Service” page
        '''
    ],

    "how do I report side effects?": [
        '''
        1. To report side effect, on the Home page, select “Side effect” button.
        2. Select “Click here for the list of symptoms”
        3. Check the boxes that apply to you
        4. Select the day when these symptoms start
        5. Select “Submit”
        6. Our nurses will schedule a teleconsultation via chatbot if it is deemed necessary.
        '''
    ],

    "where can I find common treatment side effect?": [
        '''
        1. To find common treatment side effect, on the Home page, select “QnA” from the bottom navigation bar
        2. Select “Side effects of treatment”
        '''
    ],

    "where can I find information about tuberculosis/TB treatment?": [
        '''
        1. To find common treatment side effect, on the Home page, select “QnA” from the bottom navigation bar
        2. A list of topics to select which you may find helpful
        '''
    ],

    "how do I switch on/off reminders to consume my medication?": [
        '''
        1. To switch on/off reminders, under the Home page, select “Profile” 
        2. Select select/deselect the option to “Do you wish to turn on reminders for VDOTS treatment?”
        '''
    ],

    "why is my urine orange in colour?": [
        "It is a known side effect from taking Rifampicin.  It can be found other bodily fluids such as saliva, tears, or sweat.  This is normal and the colour would fade away over time."
    ],

    "how should I take the medications?": [
       '''
        1. Ensure an empty stomach an hour before taking medication
        2. Do not eat anything an hour after taking the medication
        3. For gastric patient, have breakfast and wait an hour before taking the medication.
        4. Family members should supervise while patient take medication at home and need to record the video everyday in this application.
       ''' 
    ],

    "how should about my day since discharged from hospital?": [
        '''
        1. Pulmonary tuberculosis patients should wear a mask everyday for 2 weeks.  Mask should be changed everyday.
        2. Have the windows and curtains opened for good ventilation
        3. There is no need to separate the dishes
        4. Get enough rest and avoid crowded places
        '''
    ],

    "referral to eye clinic": [
        "Patients should be referred to eye clinic while taking Ethambutol medication.  This is to detect symptoms such as farsightedness, nearsightedness, and colour blindness."
    ],

    "should my family members that I live with get screened for TB?": [
        "Yes.  Each family member who is staying within the same household or have been in contact with patient MUST do TB screening at Rawatan Utama Kesihatan Awam (RUKA) or nearest Klinik Kesihatan."
    ],

    "default": [
        "this is a default message"
    ]
}