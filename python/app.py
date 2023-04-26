from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Process form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Do something with the data (e.g. save to database)

        # Render thank you page
        return render_template('thankyou.html', name=name)

    # Render form page
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
