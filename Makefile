
install:
	pip install -r requirements.txt

travis:
	pip install -r requirements.txt

test:
	cd bot && python ResultTest.py

ejecutar:
	cd bot && python app.py