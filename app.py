from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():

    name = request.form['name']
    feedback = request.form['feedback']

    positive_words = ["good","excellent","great","awesome","happy"]

    negative_words = ["bad","poor","worst","hate","terrible"]

    sentiment = "Neutral"

    for word in positive_words:
        if word in feedback.lower():
            sentiment = "Positive"

    for word in negative_words:
        if word in feedback.lower():
            sentiment = "Negative"

    sender_email = "dhivyadharshinibalasubramani@gmail.com"
    sender_password = "dhivibalu47s"
    owner_email = "dhivibalu04@gmail.com"

    subject = "Customer Feedback"

    message = f"""Subject:{subject}

Customer Name : {name}

Feedback :
{feedback}

Sentiment :
{sentiment}
"""

    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(sender_email,sender_password)
        server.sendmail(sender_email,owner_email,message)
        server.quit()

    except Exception as e:
        print(e)

    return render_template("result.html",
                           sentiment=sentiment,
                           feedback=feedback)

if __name__=="__main__":
    app.run(debug=True)