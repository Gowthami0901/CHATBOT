# HOW TO CREATE WHATSAPP CHATBOT

* [Method 1](#Method-1)
   - [Prerequisities](#Prerequisites)
   - [Subscription](#Subscription)

* [Method 2](#Method-2)
   - [Prerequisities](#Prerequisites-2)
   - [Subscription](#Subscriptions)

* [Twilio's free trial](#Twilio's-free_trial)
   - [Prerequisities](#Prerequisites-3)
   - [Summary of Free Subscriptions](#Free_trail-subscriptions)

* [Reference](#reference)


# Method-1

## Prerequisites

1. **WhatsApp Business Account**: You need a WhatsApp Business API account. Sign up on the [WhatsApp Business API page](https://www.whatsapp.com/business/api) or through a WhatsApp Business Solution Provider like Twilio, MessageBird, or others.
   
2. **Business Verification**: Ensure your business is verified by Facebook to use the WhatsApp Business API.

3. **Developer Skills**: Basic understanding of programming (JavaScript, Python, or any other language) and familiarity with APIs.

4. **Hosting Service**: A server to host your chatbot application (e.g., AWS, Heroku, or any other hosting provider).

## Steps to Create a WhatsApp Chatbot

1. **Sign Up for WhatsApp Business API**
   - Register and get your WhatsApp Business API setup through a solution provider like Twilio, MessageBird, or others.

   - Follow the provider’s instructions to configure your WhatsApp Business API.

2. **Choose a Platform/Framework**
   - Use platforms like **Twilio**, **Dialogflow**, **Botpress**, or **ManyChat** which provide integrations for WhatsApp chatbots.

   - For this guide, we'll use Twilio and a simple Node.js setup as an example.

3. **Set Up Your Development Environment**
   - Install Node.js and npm (Node Package Manager) on your system.

   - Create a new directory for your project and initialize it with `npm init`.

   - Install necessary packages:

    
```bash
npm install express twilio body-parser
```
    

4. **Write the Chatbot Logic**
   - Create a simple Express server and integrate Twilio’s WhatsApp API:

     Certainly! Here is the provided JavaScript code for setting up a simple Express server and integrating Twilio’s WhatsApp API:

```javascript
const express = require('express');
const bodyParser = require('body-parser');
const twilio = require('twilio');

const app = express();
app.use(bodyParser.urlencoded({ extended: false }));

const accountSid = 'your_twilio_account_sid';
const authToken = 'your_twilio_auth_token';
const client = new twilio(accountSid, authToken);

app.post('/whatsapp', (req, res) => {
    const messageBody = req.body.Body;
    const fromNumber = req.body.From;

    let responseMessage = 'Welcome to HR Bot. How can I assist you today?';

    if (messageBody.toLowerCase().includes('job')) {
        responseMessage = 'Please send your resume to hr@company.com';
    }

    client.messages
        .create({
            body: responseMessage,
            from: 'whatsapp:+14155238886', // Twilio Sandbox number
            to: fromNumber
        })
        .then((message) => console.log(message.sid));

    res.send('<Response></Response>');
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
```

   - Replace `'your_twilio_account_sid'` and `'your_twilio_auth_token'` with your actual Twilio credentials.

   - This example responds with a message based on the user’s input.

5. **Configure Webhook in Twilio**
   - Go to your Twilio console and configure the webhook URL to point to your server (e.g., `http://yourserver.com/whatsapp`).

6. **Test Your Chatbot**
   - Use Twilio’s sandbox environment to test your chatbot.

   - Send messages to your WhatsApp bot and check if it responds appropriately.

## Additional Features
- **Resume Parsing**: Integrate a resume parser to extract details from submitted resumes.

- **Database Integration**: Store user data and interactions in a database like MongoDB or Firebase.

- **Natural Language Processing**: Use Dialogflow or similar NLP services to handle complex queries and responses.

- **Interactive Menus**: Create menus for users to navigate through different options.

## Deployment
- Deploy your application on a hosting service (e.g., Heroku, AWS).

- Ensure your server is secure and can handle incoming requests efficiently.

Creating a WhatsApp chatbot using the method you described involves several steps and components, which might have associated costs. Below are the possible subscriptions and costs involved:


# Subscription

## 1. **WhatsApp Business API Subscription:**

- **WhatsApp Business Solution Provider**: Providers like Twilio, MessageBird, and others typically charge for using their WhatsApp Business API services. The costs can vary based on the number of messages sent and received, as well as any additional services provided (e.g., message templates, media messages).

  - **Twilio Pricing**: Twilio charges per message. As of the last update, the cost is typically around $0.005 per message, but it can vary based on the country and type of message.
  - **Other Providers**: Each provider has its own pricing structure. You will need to check the respective provider's website for detailed pricing.

## 2. **Hosting Service:**

- **Heroku**: Offers a free tier with limited resources. For more robust performance, you may need to upgrade to a paid plan. Pricing starts at $7/month for the Hobby tier.
- **AWS**: Offers a free tier for the first 12 months. After that, costs are based on usage. For a small application, it might cost around $10-$20 per month.
- **Other Hosting Providers**: Each hosting service has its own pricing structure. Check their websites for detailed pricing.

## 3. **Twilio Account:**

- **Twilio Account**: Signing up for a Twilio account is free, and they provide a limited free trial balance. Beyond that, you will need to pay for usage. This includes costs for phone numbers, message sending, and any additional services.

## 4. **Additional Services:**

- **Database Services**: If you plan to use a cloud database like MongoDB Atlas, Firebase, or others, these services also have free tiers but will charge based on usage beyond the free tier.
- **Natural Language Processing (NLP) Services**: Using services like Dialogflow might incur additional costs based on the number of queries processed.


## Summary of Potential Costs:

1. **WhatsApp Business API Provider**:
   - Twilio, MessageBird, etc.: Varies (approximately $0.005 per message)

2. **Hosting**:
   - Heroku: Free to $7/month (or more for higher tiers)
   - AWS: Free tier for 12 months, then pay-as-you-go (approximately $10-$20/month for small applications)

3. **Twilio Account**:
   - Free trial available, then pay per message and for phone numbers

4. **Additional Services**:
   - Database: Free tier available, then pay-as-you-go
   - NLP Services: Free tier available, then pay-as-you-go


## No-Cost Option (For Development and Testing):

- Use Twilio’s free trial balance for initial testing.
- Use Heroku’s free tier for hosting.
- Use the free tier of cloud databases and NLP services for initial development.


## Conclusion:

To start, you can use the free tiers of these services to develop and test your chatbot. As you scale and move towards production, you will need to budget for the costs associated with message sending, hosting, and any additional services you require. Always check the latest pricing on the respective service providers' websites to get the most accurate and up-to-date information.



# Method-2

## Prerequisites-2

1. **WhatsApp Business Account**:
   - You need a WhatsApp Business account. You can sign up for one on the [WhatsApp Business website](https://www.whatsapp.com/business/).

2. **Facebook Developer Account**:
   - Since WhatsApp is owned by Facebook, you need a Facebook Developer account to use the WhatsApp Business API. Sign up at the [Facebook Developers website](https://developers.facebook.com/).

3. **WhatsApp Business API**:
   - Apply for access to the WhatsApp Business API. You can do this through the Facebook Developer portal.

4. **Hosting**:
   - A server to host your chatbot. You can use services like AWS, Heroku, or any other cloud provider.

5. **Programming Knowledge**:
   - Familiarity with a programming language like Python, Node.js, or any language that can make HTTP requests.

6. **Webhook URL**:
   - Set up a webhook URL where WhatsApp will send incoming messages.

## Steps to Create the Chatbot

1. **Set Up Facebook Developer Account**:
   - Create a new app in the Facebook Developer portal.
   - Under "Add a Product," select "WhatsApp" and configure it.

2. **Configure WhatsApp Business API**:
   - Once approved for the API, you’ll get access to your WhatsApp Business account settings.
   - Set up your phone number and verify it.

3. **Set Up Webhook**:
   - Create a server (e.g., using Flask or Express) that listens for incoming HTTP requests from WhatsApp.
   - Configure the webhook URL in the Facebook Developer portal under your app settings.

4. **Write Code for the Chatbot**:
   - Use your chosen programming language to handle incoming messages and send responses.
   - You can use libraries like `twilio` for Python or `whatsapp-web.js` for Node.js to simplify the process.


   **Example in Python using Flask and Twilio:**
   Here is the Python code formatted properly for use with Flask and Twilio's WhatsApp API:

```python
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
```

5. **Deploy Your Server**:
   - Deploy your server to a hosting provider. Ensure the webhook URL is publicly accessible.

6. **Test Your Chatbot**:
   - Send messages to your WhatsApp number and verify that the bot responds as expected.


## Subscriptions

- **WhatsApp Business API**: 
  - The API itself is free, but you may incur charges for sending messages. This usually depends on the number of messages you send and receive.
  
- **Cloud Hosting**:
  - Depending on your choice of hosting provider, you may have to pay for server resources.

- **Third-Party Services**:
  - If you use third-party services like Twilio to manage messaging, you’ll need a subscription to their services. Twilio, for instance, charges based on the number of messages sent and received.

**Example Pricing from Twilio**:
- Twilio charges $0.005 per message sent or received for WhatsApp messages. 
- Monthly fees for the WhatsApp Business API may vary based on your usage and the number of messages sent.



# Twilio's-free_trial 

Creating a free WhatsApp chatbot involves using free trials and free tiers offered by various services. Here’s how you can do it with Twilio and Heroku, including the prerequisites and any necessary subscriptions.

## Prerequisites-3

1. **WhatsApp Business Account**: You’ll need to use the WhatsApp Business API. To get started for free, you can use Twilio’s sandbox for WhatsApp.
2. **Twilio Account**: Sign up for a free Twilio account, which provides trial credits.
3. **Heroku Account**: Sign up for a free Heroku account to deploy your chatbot.
4. **Node.js and npm**: Install Node.js and npm on your development machine.

## Step-by-Step Guide

## 1. Sign Up for Twilio Free Trial

1. Go to the [Twilio Signup Page](https://www.twilio.com/try-twilio) and create an account.

2. Verify your email and phone number.

3. Get your Twilio Account SID and Auth Token from the Twilio Console.

4. Activate the Twilio Sandbox for WhatsApp:
   - Navigate to the Twilio Console and go to "Messaging" > "Try it Out" > "WhatsApp Sandbox."
   - Follow the instructions to join the sandbox.

## 2. Set Up Your Development Environment

1. **Install Node.js and npm**:
   - Download and install Node.js from [nodejs.org](https://nodejs.org/).
   - Verify the installation by running:
     ```bash
     node -v
     npm -v
     ```

2. **Create a new project directory**:
   ```bash
   mkdir whatsapp-chatbot
   cd whatsapp-chatbot
   ```

3. **Initialize the project**:
   ```bash
   npm init -y
   ```

4. **Install necessary packages**:
   ```bash
   npm install express twilio body-parser
   ```

## 3. Write the Chatbot Logic

1. Create a new file `index.js` and add the following code:
   ```javascript
   const express = require('express');
   const bodyParser = require('body-parser');
   const twilio = require('twilio');

   const app = express();
   app.use(bodyParser.urlencoded({ extended: false }));

   const accountSid = process.env.TWILIO_ACCOUNT_SID;
   const authToken = process.env.TWILIO_AUTH_TOKEN;
   const client = new twilio(accountSid, authToken);

   app.post('/whatsapp', (req, res) => {
       const messageBody = req.body.Body.toLowerCase();
       const fromNumber = req.body.From;

       let responseMessage = 'Welcome to HR Bot. How can I assist you today?';

       if (messageBody.includes('job')) {
           responseMessage = 'Please send your resume to hr@company.com';
       }

       client.messages
           .create({
               body: responseMessage,
               from: 'whatsapp:+14155238886', // Twilio Sandbox number
               to: fromNumber
           })
           .then((message) => console.log(message.sid))
           .catch((error) => console.error(error));

       res.send('<Response></Response>');
   });

   const PORT = process.env.PORT || 3000;
   app.listen(PORT, () => {
       console.log(`Server is running on port ${PORT}`);
   });
   ```

2. Create a `.env` file to store your Twilio credentials securely:
   ```
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   ```

3. Install the `dotenv` package to load environment variables from the `.env` file:
   ```bash
   npm install dotenv
   ```

4. Modify `index.js` to load the environment variables:
   ```javascript
   require('dotenv').config();
   ```


## 4. Deploy to Heroku

1. **Install the Heroku CLI**:
   - Follow the instructions to install the Heroku CLI from [here](https://devcenter.heroku.com/articles/heroku-cli).

2. **Log in to Heroku and create a new app**:
   ```bash
   heroku login
   heroku create your-app-name
   ```

3. **Initialize a Git repository, commit your code, and push to Heroku**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push heroku master
   ```

4. **Set environment variables on Heroku**:
   ```bash
   heroku config:set TWILIO_ACCOUNT_SID=your_account_sid TWILIO_AUTH_TOKEN=your_auth_token
   ```

5. **Open your app in a browser to verify deployment**:
   ```bash
   heroku open
   ```

## 5. Configure Webhook in Twilio

1. Go to the Twilio Console, navigate to "Messaging" > "Try it Out" > "WhatsApp Sandbox."

2. Set the "WHEN A MESSAGE COMES IN" webhook to point to your Heroku app URL, e.g., `https://your-app-name.herokuapp.com/whatsapp`.


## 6. Test Your Chatbot

1. Use the WhatsApp number provided by Twilio’s sandbox.
2. Send a message to the number and test the responses based on your chatbot logic.


## Free_Trail-Subscriptions

- **Twilio**: Free trial with limited credits.
- **Heroku**: Free tier for hosting the chatbot.
- **Node.js and npm**: Free and open-source.


# Reference

https://docs.rapidbott.com/help-center/platform/whatsapp-channel/connect-with-whatsapp-cloud-api


You can use this link to access the detailed guide on connecting with the WhatsApp Cloud API.
