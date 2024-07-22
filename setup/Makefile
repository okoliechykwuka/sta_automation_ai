setup:
    @echo "Creating virtual environment..."
    python -m venv stdautomationenv

install:
    @echo "Activating virtual environment and installing dependencies..."
    bash -c "source stdautomationenv/bin/activate && pip install -r requirements.txt"

# test:
#     @echo "Running tests..."
#     bash -c "source stdautomationenv/bin/activate && robot tests"

clean:
    @echo "Cleaning up..."
    # rm -rf stdautomationenv
    find . -type f -name '*.pyc' -delete
    find . -type d -name '__pycache__' -delete

.PHONY: setup install test clean
