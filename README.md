# ACEest Fitness and Gym 🏋️‍♂️

A user-friendly web application for tracking your workouts and managing gym activities. This project is built with Flask and includes automated testing and deployment features.

## What Does This App Do? 🎯

- Track your workouts easily
- Record workout duration
- View your workout history
- Simple and clean interface

## Project Structure 📁

```
devops_a1/
│
├── app.py                 # Main Flask application
├── templates/            
│   └── index.html        # Web page template
├── tests/                
│   └── test_app.py       # Test cases
├── Dockerfile            # Container configuration
├── requirements.txt      # Python dependencies
└── .github/workflows/    # CI/CD configuration
```

## Local Setup 🚀

1. Clone the repository:
```bash
git clone <your-repository-url>
cd devops_a1
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Access the application at `http://localhost:5000`

## Running Tests

To run the tests:
```bash
pytest
```

## Docker Setup 🐳

Docker makes it easy to run the application anywhere! Here's how:

1. Build the Docker image:
```bash
docker build -t aceest-fitness .
```

2. Run the container:
```bash
docker run -p 5000:5000 aceest-fitness
```

The application will be available at `http://localhost:5000`

## Understanding the CI/CD Pipeline 🔄

Every time you push code to GitHub, the following happens automatically:

1. **Testing Stage** ✅
   - GitHub creates a fresh environment
   - Installs Python and all dependencies
   - Runs all the test cases
   - If tests fail, stops here and notifies you

2. **Build Stage** 🏗️
   - Only starts if all tests pass
   - Builds a Docker container
   - Verifies the container works
   - Prepares for deployment

### How to Know If It Worked? 🤔

1. Go to your GitHub repository
2. Click on "Actions" tab
3. Look for your latest commit
4. Green checkmark ✅ = Everything worked!
   Red X ❌ = Something needs fixing

## Common Issues and Solutions 🔧

1. **Tests Failing?**
   - Check the Actions tab for error details
   - Run tests locally first: `pytest`
   - Make sure all dependencies are installed

2. **Docker Issues?**
   - Ensure Docker is running on your machine
   - Try building locally first
   - Check port 5000 isn't already in use

## Need Help? 🆘

1. Check the error messages in GitHub Actions
2. Run the tests locally to debug
3. Make sure all files are committed and pushed
4. Check if Docker is running properly

## Development Tips 💡

This project uses GitHub Actions for CI/CD. The pipeline:

1. Runs on every push to main branch
2. Executes all unit tests
3. Builds Docker image
4. Tests the Docker build

The workflow configuration can be found in `.github/workflows/main.yml`
