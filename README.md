# ACEest Fitness and Gym

A Flask web application for tracking workouts and managing gym activities.

## Local Setup

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

## Docker Setup

1. Build the Docker image:
```bash
docker build -t aceest-fitness .
```

2. Run the container:
```bash
docker run -p 5000:5000 aceest-fitness
```

## CI/CD Pipeline

This project uses GitHub Actions for CI/CD. The pipeline:

1. Runs on every push to main branch
2. Executes all unit tests
3. Builds Docker image
4. Tests the Docker build

The workflow configuration can be found in `.github/workflows/main.yml`
