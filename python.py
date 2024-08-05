from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import pymongo

app = Flask(__name__)

# Set up MongoDB connection
client = pymongo.MongoClient("your_mongo_db_connection_string")
db = client.hr_bot

@app.route('/webhook', methods=['POST'])
def webhook():
    msg = request.form.get('Body').lower()
    candidate_number = request.form.get('From')
    resp = MessagingResponse()

    if 'hi' in msg or 'hello' in msg:
        resp.message('Hi there! Welcome to the HR Bot. How can I assist you today?'
                     '\nType "job" to see available jobs.'
                     '\nType "apply" to apply for a job.'
                     '\nType "interview" to schedule an interview.'
                     '\nType "status" to check your application status.'
                     '\nType "faq" for frequently asked questions.')
    elif 'job' in msg:
        jobs = db.jobs.find()
        job_list = "\n".join([job['title'] for job in jobs])
        resp.message(f"Available jobs:\n{job_list}")
    elif 'apply' in msg:
        candidate_info = extract_candidate_info(msg)
        db.candidates.insert_one(candidate_info)
        resp.message('Thank you for applying! We will get back to you soon.')
    elif 'interview' in msg:
        resp.message('Our interview process consists of the following rounds:\n'
                     '1. Initial Screening\n'
                     '2. Technical Interview\n'
                     '3. HR Interview\n'
                     'Please choose an available slot for the initial screening by typing the number:\n'
                     '1. Tomorrow 10 AM\n2. Tomorrow 2 PM\n3. Next Monday 11 AM\n4. Next Monday 3 PM')
    elif msg in ['1', '2', '3', '4']:
        slot = get_slot(msg)
        if slot:
            db.interviews.insert_one({'slot': slot, 'candidate': candidate_number})
            resp.message(f'Your interview has been scheduled for {slot}. We look forward to speaking with you!')
        else:
            resp.message('Invalid slot. Please choose an available slot by typing the number:\n'
                         '1. Tomorrow 10 AM\n2. Tomorrow 2 PM\n3. Next Monday 11 AM\n4. Next Monday 3 PM')
    elif 'status' in msg:
        status = get_candidate_status(candidate_number)
        resp.message(f'Your application status: {status}')
        if status == 'selected':
            resp.message('Congratulations! You have been selected. Your offer letter will be sent shortly.')
            send_offer_letter(candidate_number)
        elif status == 'rejected':
            resp.message('We regret to inform you that you have not been selected. Thank you for your interest.')
    elif 'faq' in msg:
        resp.message('Here are some frequently asked questions:\n1. How to apply?\n2. What are the interview steps?\n3. What are the job requirements?')
    else:
        resp.message('I didn’t understand that. Please type "hi" to see the menu.')

    return str(resp)

def extract_candidate_info(message):
    # Function to parse candidate info from the message
    return {
        'name': 'Candidate Name',
        'email': 'candidate@example.com',
        'position': 'Applied Position'
    }

def get_slot(msg):
    slots = {
        '1': 'Tomorrow 10 AM',
        '2': 'Tomorrow 2 PM',
        '3': 'Next Monday 11 AM',
        '4': 'Next Monday 3 PM'
    }
    return slots.get(msg.strip())

def get_candidate_status(candidate_number):
    candidate = db.candidates.find_one({'contact': candidate_number})
    return candidate['status'] if candidate else 'not found'

def send_offer_letter(candidate_number):
    candidate = db.candidates.find_one({'contact': candidate_number})
    if candidate:
        # Logic to send an offer letter, e.g., via email
        print(f'Sending offer letter to {candidate["email"]}')

if __name__ == '__main__':
    app.run(debug=True)
