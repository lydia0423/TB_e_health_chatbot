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
    elif "track record" in x_text:
        y_text = "how can I check my track record of uploading the videos?"
    elif "order medications" in x_text: 
        y_text = "how do I order medications"
    elif "side effect" in x_text: 
        y_text = "how do I report side effects?"
    elif "information" in x_text: 
        y_text = "where can I find useful information regarding the use of the app?"
    elif "tb" in x_text: 
        y_text = "where can I find useful information regarding tuberculosis?"
    elif "contact" in x_text: 
        y_text = "who can I contact if I encounter a problem with the regarding app?"
    elif "orange" in x_text: 
        y_text = "why is my urine orange in colour?"
    elif "how to take" in x_text: 
        y_text = "how should I take the medications?"
    elif "discharged" in x_text: 
        y_text = "how should I get about my day after being discharged from hospital?"
    elif "eye clinic" in x_text: 
        y_text = "referral to eye clinic"
    elif "household" in x_text: 
        y_text = "should my family members that I live with any of my household close contact get screened for TB?"
    elif "default" in x_text: 
        y_text = "this is a default message"
    elif "test" in x_text:
        y_text = "where can I go for a tb test?"
    elif "bring" in x_text:
        y_text = "what should I bring for tb testing?"
    elif "nearest hospitals" in x_text:
        y_text = "where are the nearest hospitals?"
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
    elif "x-ray" in x_text:
        y_text = "where are the nearest hospitals that provide x-ray service?"
    elif "selangor" in x_text:
        y_text = "selangor"
    elif "gombak area" in x_text:
        y_text = "gombak area"
    elif "hulu langat area" in x_text:
        y_text = "hulu langat area"
    elif "hulu selangor area" in x_text:
        y_text = "hulu selangor area"
    elif "kelang area" in x_text:
        y_text = "kelang area"
    elif "kuala selangor area" in x_text:
        y_text = "kuala selangor area"
    elif "petaling area" in x_text:
        y_text = "petaling area"
    elif "sabak area" in x_text:
        y_text = "sabak area"
    elif "sepang area" in x_text:
        y_text = "sepang area"
    elif "putrajaya" in x_text:
        y_text = "putrajaya"
    elif "labuan" in x_text:
        y_text = "labuan"
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
        1. Select VDOTS Therapy
        2. Select Video, record yourself
        3. Select Upload
        4. You will receive a confirmation message
        '''
    ],

    "how can I check my track record of uploading the videos?": [
        "Please check My VDOTS Therapy progress in your user profile"
    ],

    "how do I order medications?": [
        '''
        1. Select Drug Delivery
        2. Select Confirm Order
        '''
    ],

    "how do I report side effects?": [
        '''
        1. Select Side-effect
        2. Check the side-effects that apply to you
        3. Select the day when these symptoms start
        4. Select Submit
        5. Our healthcare staff will get in touch with you
        '''
    ],

    "where can I find useful information regarding the use of the app?": [
        '''
        1. To find common treatment side effect, on the Home page, select “QnA” from the bottom navigation bar
        2. Select “Side effects of treatment”
        '''
    ],

    "where can I find useful information regarding tuberculosis?": [
        '''
        1. To find common treatment side effect, on the Home page, select “QnA” from the bottom navigation bar
        2. A list of topics to select which you may find helpful
        '''
    ],

    "who can I contact if I encounter a problem with the regarding app?": [
        "You may call us at 03-79492389 during office hours or email us at tb@ummc.edu.my"
    ],

    "why is my urine orange in colour?": [
        "It is a known side effect from taking Rifampicin.  It can be found other bodily fluids such as saliva, tears, or sweat.  This is normal and the colour would fade away over time."
    ],

    "how should I take the medications?": [
       '''
        1. Ensure an empty stomach an hour before taking medication
        2. Do not eat anything 2 hours after taking the medication
        3. If you have a gastric problem, wait an hour before taking the medication after you have your breakfast.
        4. An identified treatment supporter by the VDOTS clinic should supervise you while you are  taking medication at home and you need to record the video everyday in this application as evidence of you taking the medications.
       ''' 
    ],

    "how should I get about my day after being discharged from hospital?": [
        '''
        1. You should wear a mask everyday for the next 2 weeks to prevent the TB infection to others.  Masks should be changed regularly.
        2. Make sure your house and room is well ventilated by opening up
        3. There is no need to separate the dishes
        4. Get enough rest and avoid crowded places
        '''
    ],

    "referral to eye clinic": [
        "You will receive a referral letter to the eye clinic to monitor your vision while taking the TB medications. Please ask for the referral letter from the DOTS clinic if you have not received it yet."
    ],

    "should my family members that I live with any of my household close contact get screened for TB?": [
        "Yes.  Anyone who is staying within the same household or has been in contact with the TB patient you MUST be screened for possible TB infection at our Rawatan Utama Kesihatan Awam (RUKA) or nearest Klinik Kesihatan."
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

    "what should I bring for tb testing?": [
        '''
        You need to bring with you:

        1. proof of identification, which contains your photograph, such as your passport
        2. TB test fee
        3. details of previous screenings and, if possible, medical notes and x-ray results, if you have had TB in the past or have any other lung disease
        '''
    ],

    "where are the nearest hospitals?" : [
        '''
        Where are the nearest hospitals? Type the area name listed below, i.e gombak
        1. gombak
        2. hulu Langat
        3. hulu Selangor
        4. klang 
        5. kuala langat 
        6. kuala selangor
        7. petaling
        8. sabak bernam
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
            1. Assunta Hospital                                      
            2. Columbia Asia Medical Centre, Puchong                 
            3. Darul Ehsan Medical Centre                            
            4. Hospital Bersalin, Klinik Pakar & Poliklinik Pusat    
            5. Hospital Mata Tun Hussien Onn                         
            6. Hospital Pakar Damansara                              
            7. Hospital Rawatan Lanjutan Columbia Asia               
            8. Hospital Shah Alam                                    
            9. Hospital Sungai Buloh                                 
            10. KPJ Selangor Specialist Hospital                      
            11. KPMC Puchong Medical Centre                           
            12. Kelana Jaya Medical Centre                            
            13. Klinik Pakar Wanita dan Bersalin Subang Permai        
            14. Pusat Jagaan Ambulatori Swasta                        
            15. Pusat Perubatan Damansara Damai                       
            16. Pusat Peubatan Putra                                  
            17. QHC Medical Centre                                    
            18. Shah Alam Specialist Hospital                         
            19. Sime Darby Specialist Centre Megah Sdn Bhd            
            20. Subang Jaya Medical Centre                            
            21. Sunway Medical Centre                                 
            22. Tropicana Medical Centre                              
            23. Wijaya International Medical Centre 
        '''
    ],

    "sabak bernam": [
        "Hospital Tengku Ampuan Jemaah (HTAJ)"
    ],

    "where are the nearest hospitals that provide x-ray service?": [
        '''
        Where are the nearest hospitals? Type the area name listed below, i.e gombak
        1. selangor
        2. kuala lumpur
        3. labuan
        4. putrajaya
        '''
    ],

    "selangor": [
        '''
        Type the area name listed below (i.e gombak area):
        1. gombak area
        2. hulu langat area
        3. hulu Selangor area
        4. kelang area
        5. kuala selangor area
        6. petaling area
        7. sabak area
        8. sepang area
        '''
    ],

    'gombak area': [
        '''
        1. Klinik Kesihatan Rawang (Functioning)
        2. Klinik Kesihatan Sungai Buloh (Non functioning)
        3. Klinik Kesihatan Taman Ehsan	(Functioning)
        '''
    ],

    "hulu langat area": [
        '''
        1. Klinik Kesihatan Kajang (Non functioning)
        2. Klinik Kesihatan Batu 9 (Non functioning)
        3. Klinik Kesihatan Bandar Baru Bangi (Functioning)
        4. Klinik Kesihatan Bandar Seri Putra (Functioning)
        5. Klinik Kesihatan Sungai Chua	(Functioning)
        6. klinik Bandar Tun Hussien Onn (Functioning)
        '''
    ],

    "hulu selangor area": [
        "Klinik Kesihatan Serendah (Functioning)"
    ],

    "kelang area": [
        '''
        1. Klinik Kesihatan Bukit Kuda (Functioning)
        2. Klinik Kesihatan Pandamaran (Non functioning)
        3. Klinik Kesihatan Pelabuhan Klang	(Functioning)
        4. Klinik Kesihatan Bandar Botanik (Functioning)
        '''
    ],

    "kuala selangor area": [
        "Klinik Kesihatan Bestari Jaya (Functioning)"
    ],

    "petaling area": [
        '''
        1. Klinik Kesihatan Kelana Jaya	(Non functioning)
        2. Klinik Kesihatan Seri Kembangan (Functioning)
        3. Klinik Kesihatan Seksyen 7 Shah Alam	(Non functioning)
        4. Klinik Kesihatan Medan Maju Jaya	(Functioning)
        5. Klinik Kesihatan Seksyen 19 (Non functioning)
        6. Klinik kesihatan Kota Damansara (Functioning)
        '''
    ],

    "sabak area": [
        "Kilinik Kesihatan Simpang Lima (Functioning)"
    ],

    "sepang area": [
        '''
        1. Klinik Kesihatan Salak (Non functioning)
        2. Klinik Kesihatan Sungai Pelek (Non functioning)
        '''
    ],

    "kuala lumpur": [
        '''
        1. Klinik Kesihatan Cheras (Functioning)
        2. Klinik Kesihatan Jinjang	(Functioning)
        3. Klinik Kesihatan Kuala Lumpur (Functioning)
        4. Klinik Kesihatan Tanglin	(Non functioning)
        '''
    ],

    "putrajaya": [
        '''
        1. Klinik Kesihatan Putrajaya Presint 9	(Functioning)
        2. Klinik Kesihatan Putrajaya Presint 18 (Functioning)
        '''
    ],

    "labuan": [
        "Klinik Kesihatan WP Labuan	(Functioning)"
    ],

    "not understand": [
        "This is me telling you I didn't understand what you just said. I'm learning, you see. Could you try again?"
    ],

    "default": [
        "this is a default message"
    ],
}