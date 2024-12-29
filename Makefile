install:
	pip install --upgrade pip
	pip install -r requirements.txt

test:
	python test.py

docker-build:
	docker build  -t DNB12/health-calculator-service:latest .

run:;
	. .venv/bin/activate && python app.py

init:
	@which python3 || echo "Python3 is not installed"
	python3 -m venv .venv || echo "Failed to create virtual environment"
	. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt || echo "Failed to install dependencies"
