# ...existing code...
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def index_html():
    return render_template('index.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        contact = request.form['contact']
        message = request.form['message']
        fb = Feedback(fullname=fullname, email=email, contact=contact, message=message)
        db.session.add(fb)
        db.session.commit()
        flash('Thank you for your feedback!', 'success')
        return redirect(url_for('feedback'))
    return render_template('feedback.html')

@app.route('/culture.html')
def culture_html():
    return render_template('culture.html')


# Route for Cultural/gaura.html
@app.route('/Cultural/gaura.html')
def gaura_html():
    return render_template('Cultural/gaura.html')



# Route for Cultural/festivals-identity.html
@app.route('/Cultural/festivals-identity.html')
def festivals_identity_html():
    return render_template('Cultural/festivals-identity.html')


# Route for Cultural/folk-culture.html
@app.route('/Cultural/folk-culture.html')
def folk_culture_html():
    return render_template('Cultural/folk-culture.html')


# Route for youth.html
@app.route('/youth.html')
def youth_html():
    return render_template('youth.html')



# Route for Youth/lifestyle.html
@app.route('/Youth/lifestyle.html')
def youth_lifestyle_html():
    return render_template('Youth/lifestyle.html')


# Route for Youth/technology.html
@app.route('/Youth/technology.html')
def youth_technology_html():
    return render_template('Youth/technology.html')

# Route for Youth/education.html
@app.route('/Youth/education.html')
def youth_education_html():
    return render_template('Youth/education.html')

# Route for direct access to feedback.html
@app.route('/feedback.html')
def feedback_html():
    return render_template('feedback.html')

@app.route('/issues.html')
def issues_html():
    return render_template('issues.html')

# Route for Socialissues/gender.html
@app.route('/Socialissues/gender.html')
def socialissues_gender_html():
    return render_template('Socialissues/gender.html')

# Route for Socialissues/youthempower.html
@app.route('/Socialissues/youthempower.html')
def socialissues_youthempower_html():
    return render_template('Socialissues/youthempower.html')

# Route for Socialissues/socialawarness.html
@app.route('/Socialissues/socialawarness.html')
def socialissues_socialawarness_html():
    return render_template('Socialissues/socialawarness.html')

# Route for festivals.html
@app.route('/festivals.html')
def festivals_html():
    return render_template('festivals.html')

# Route for Festivals/dashain.html
@app.route('/Festivals/dashain.html')
def festivals_dashain_html():
    return render_template('Festivals/dashain.html')

# Route for Festivals/holi.html
@app.route('/Festivals/holi.html')
def festivals_holi_html():
    return render_template('Festivals/holi.html')

# Route for Festivals/maghi.html
@app.route('/Festivals/maghi.html')
def festivals_maghi_html():
    return render_template('Festivals/maghi.html')

# Route for community.html
@app.route('/community.html')
def community_html():
    return render_template('community.html')

# Route for Community/village-life.html
@app.route('/Community/village-life.html')
def community_village_life_html():
    return render_template('Community/village-life.html')

# Route for Community/joint-family.html
@app.route('/Community/joint-family.html')
def community_joint_family_html():
    return render_template('Community/joint-family.html')

# Route for Community/ethnic-harmony.html
@app.route('/Community/ethnic-harmony.html')
def community_ethnic_harmony_html():
    return render_template('Community/ethnic-harmony.html')


if __name__ == '__main__':
    if not os.path.exists('site.db'):
        with app.app_context():
            db.create_all()
    app.run(debug=True)
