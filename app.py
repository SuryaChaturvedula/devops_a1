from flask import Flask, render_template, request, redirect, url_for, flash
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flashing messages

# Store workouts in memory (in a real app, you'd use a database)
workouts = []

@app.route('/')
def index():
    return render_template('index.html', workouts=workouts)

@app.route('/add_workout', methods=['POST'])
def add_workout():
    workout = request.form.get('workout')
    duration = request.form.get('duration')
    
    if not workout or not duration:
        flash('Please enter both workout and duration.', 'error')
        return redirect(url_for('index'))
    
    try:
        duration = int(duration)
        workouts.append({
            "workout": workout,
            "duration": duration,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        flash(f"'{workout}' added successfully!", 'success')
    except ValueError:
        flash('Duration must be a number.', 'error')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
