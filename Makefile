
install:
	python3 setup.py install

test:
	cd bot && cd test && python3 test_app.py && python3 test_result.py

ejecutar:
	cd bot && python3 app.py
