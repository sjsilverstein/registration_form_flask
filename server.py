from flask import Flask, render_template, request, redirect, session, flash

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
@app.route('/') #This is the root
def index():
	return render_template('index.html')

@app.route('/validate', methods = ['POST'])
def validate():
	print "Got to /validate"
	# for key in range(0, len(request.form)):
	# 	if len(request.form[key]) < 1:
	# 		print "Are any Values Blank This is Bad Fill the Form out FOOL!"
	# 		flash("Fill out the form completely")
	# 		return render_template('index.html')
	if numFound(request.form['first_name']):
		print "Please No Numbers in Names"
		flash("Please No Numbers in Names")
		return render_template('index.html')
	if numFound(request.form['last_name']):
		print "Please No Numbers in Names"
		flash("Please No Numbers in Names")
		return render_template('index.html')
	if not EMAIL_REGEX.match(request.form['email']):
		print "Regex does not like the email"
		flash("Invalid Email Address!")
		return render_template('index.html')
	if request.form['password'] != request.form['confirm_password']:
		print "Password and Confirm do not match"
		flash("Password and Confirm Password do not match!")
		return render_template('index.html')
	if len(request.form['password']) < 8:
		print "Password must be more eight characters long"
		flash("Password must be more then eight characters long")
	print "All info is Valid!"
	flash("Thank you for submitting all of your information in a valid way!")
	return render_template('index.html')

def numFound(myString):
	numStrings = ['0','1','2','3','4','5','6','7','8','9']
	for i in range(0, len(myString)):
		for j in range(0, len(numStrings)):
			if myString[i] == numStrings[j]:
				return True
	return False
app.run(debug=True)