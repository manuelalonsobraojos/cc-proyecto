
install:
	pip install -r requirements.txt

travis:
	python install setup.py

test:
	cd bot && python ResultTest.py

ejecutar:
	cd bot && python app.py