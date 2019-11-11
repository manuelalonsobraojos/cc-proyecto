
install:
	pip install -r requirements.txt

travis:
	python setup.py install

test:
	cd bot && python app.py && python ResultTest.py

ejecutar:
	cd bot && python app.py