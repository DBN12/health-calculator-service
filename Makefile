install:
	pip install --upgrade pip
	pip install -r requirements.txt

test:
	python test.py

docker-build:
	docker build  -t DNB12/health-calculator-service:latest .

run:;
	python app.py

init:
	python3 -m venv .venv
	source .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
