from flask import Flask, jsonify,request
import random

app = Flask(__name__)
@app.route("/bot", methods=["POST"])

# response
def response():
    query = dict(request.form)['query']

    ques = related(query)

    if ques in responses:
        res = random.choice(responses[ques])
    else:
        res = random.choice(responses[ques == 'not understand'])

    return jsonify({"response" : res})

def related(x_text): 
    if "name" in x_text: 
        y_text = "what's your name?"
    elif "robot" in x_text: 
        y_text = "are you a robot?"
    elif "how are" in x_text: 
        y_text = "how are you?"
    elif "video" in x_text: 
        y_text = "how do I upload videos?"
    elif "order medications" in x_text: 
        y_text = "how do I order medications"
    elif "side effect" in x_text: 
        y_text = "how do I report side effects?"
    elif "treatment" in x_text: 
        y_text = "where can I find common treatment side effect?"
    elif "tb" in x_text: 
        y_text = "where can I find information about tuberculosis/TB treatment?"
    elif "reminders" in x_text: 
        y_text = "how do I switch on/off reminders to consume my medication?"
    elif "orange" in x_text: 
        y_text = "why is my urine orange in colour?"
    elif "how to take" in x_text: 
        y_text = "how should I take the medications?"
    elif "discharged" in x_text: 
        y_text = "how should about my day since discharged from hospital?"
    elif "eye clinic" in x_text: 
        y_text = "referral to eye clinic"
    elif "family" in x_text: 
        y_text = "should my family members that I live with get screened for TB?"
    elif "default" in x_text: 
        y_text = "this is a default message"
    elif "tb test" in x_text:
        y_text = "where can I go for a tb test?"
    elif "nearest hospital" in x_text:
        y_text = "where are the nearest hospital?"
    elif "gombak" in x_text:
        y_text = "gombak"
    elif "hulu langat" in x_text:
        y_text = "hulu langat"
    elif "hulu selangor" in x_text:
        y_text = "hulu selangor"
    elif "klang" in x_text:
        y_text = "klang"
    elif "kuala langat" in x_text:
        y_text = "kuala langat"
    elif "kuala selangor" in x_text:
        y_text = "kuala selangor"
    elif "petaling" in x_text:
        y_text = "petaling"
    elif "sabak bernam" in x_text:
        y_text = "sabak bernam"
    elif " " in x_text: 
        y_text = " "
    else: 
        y_text = "not understand"
    return y_text

if __name__== "__main__":
    app.run(host="0.0.0.0",)


# QnA template
name = "Umi"
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

    " ": [ 
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

    "where can I go for a tb test?": [
        '''
        There are 2 approved hospital that you can go for TB test.
        1. Dr Ong Kee Liang - Life Care Diagnostic Medical Centre
            Life Care Diagnostic Medical Centre SDN BHD
            1st Floor, Wisma Life Care
            No. 5, Jalan Kerinchi, Bangsar South
            59200 Kuala Lumpur
            Tel: +6 03 2241 3610
            SMS/Whatsapp: +6 012 234 3610
            Fax: +6 03 2241 3617
            Email: info@lifecare.com.my
            Website: www.lifecare.com.my
        
        2. Janice Lim - Health Screening Centre
            Gleneagles Hospital (Kuala Lumpur)
            282 and 286 Jalan Ampang,
            50450 Kuala Lumpur, Malaysia
            Tel: 603-4141 3282
            Fax: 603-4141 3280
            janicelim@gleneagleskl.com.my
            www.gleneagleskl.com.my
        '''
    ],

    "what should I bring for tb test": [
        '''
        You need to bring with you:

        1. proof of identification, which contains your photograph, such as your passport
        2. TB test fee
        3. details of previous screenings and, if possible, medical notes and x-ray results, if you have had TB in the past or have any other lung disease
        '''
    ],

    "where are the nearest hospital?" : [
        '''
        Where do you mean nearest??? Can you select the area that listed below?
        1. Gombak
        2. Hulu Langat
        3. Hulu Selangor
        4. Klang 
        5. Kuala Langat 
        6. Kuala Selangor
        7. Petaling
        8. Sabak Bernam
        '''
    ],

    "gombak": [
        '''
        1. Hospital Orang Asli Gombak                            
        2. Hospital Selayang 
        '''
    ],

    "hulu langat": [
        '''
        1. Hospital Ampang                                       
        2. Hospital Kajang                                       
        3. Hospital PUSRAWARI SMC                                
        4. Hospital Pakar Ampang Puteri                          
        5. Hospital Pakar An-Nur Hasanah                         
        6. Hospital Pantai Ampang                                
        7. Hospital Serdang                                      
        8. KPJ Kajang Specelish Hospital                         
        9. Kajang Medical Centre                                 
        10.Kajang Plaza Medical Centre
        '''
    ],

    "hulu selangor": [
        '''
        1. Hospital Kuala Kubu Bharu                             
        2. Klinik Pakar Bersalin & Bedah Serendah 
        '''
    ],

    "klang": [
        "Hospital Tengku Ampuan Rahimah (HTAR)"
    ],

    "kuala Langat": [
        "Hospital Banting"
    ],

    "kuala Selangor": [
        "Hospital Tanjung Karang"
    ],

    "petaling": [
        '''
        Assunta Hospital                                      
            1. Columbia Asia Medical Centre, Puchong                 
            2. Darul Ehsan Medical Centre                            
            3. Hospital Bersalin, Klinik Pakar & Poliklinik Pusat    
            4. Hospital Mata Tun Hussien Onn                         
            5. Hospital Pakar Damansara                              
            6. Hospital Rawatan Lanjutan Columbia Asia               
            7. Hospital Shah Alam                                    
            8. Hospital Sungai Buloh                                 
            9. KPJ Selangor Specialist Hospital                      
            10. KPMC Puchong Medical Centre                           
            11. Kelana Jaya Medical Centre                            
            12. Klinik Pakar Wanita dan Bersalin Subang Permai        
            13. Pusat Jagaan Ambulatori Swasta                        
            14. Pusat Perubatan Damansara Damai                       
            15. Pusat Peubatan Putra                                  
            16. QHC Medical Centre                                    
            17. Shah Alam Specialist Hospital                         
            18. Sime Darby Specialist Centre Megah Sdn Bhd            
            19. Subang Jaya Medical Centre                            
            20. Sunway Medical Centre                                 
            21. Tropicana Medical Centre                              
            22. Wijaya International Medical Centre 
        '''
    ],

    "sabak bernam": [
        "Hospital Tengku Ampuan Jemaah (HTAJ)"
    ],

    "not understand": [
        "This is me telling you I didn't understand what you just said. I'm learning, you see. Could you try again?"
    ],

    "default": [
        "this is a default message"
    ],
}