install:
	pip install --upgrade pip
	pip install -r requirement.txt

test:
	python test.py

docker-build:
	docker build  -t DNB12/health-calculator-service:latest .

run:;
	python app.py
