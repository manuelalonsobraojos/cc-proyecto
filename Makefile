
install:
	pip install -r requirements.txt

travis:
	python setup.py install

test:
	cd bot && cd test && python test_app.py

ejecutar:
	cd bot && python app.py