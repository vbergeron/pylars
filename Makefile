tests:
	python -m unittest discover tests

coverage:
	coverage run --source=./pylars -m unittest discover tests
	coverage report -m
	coverage erase

setup: clean
	python setup.py sdist bdist_wheel

release: setup
	twine upload --repository-url $(PYLAR_UPLOAD_URL) dist/*

release-public: setup
	twine upload dist/*

clean:
	rm -rf debug.py
	rm -rf .coverage
	rm -rf build dist *.egg-info
	find pylars -iname __pycache__ | xargs rm -rf
	find tests  -iname __pycache__ | xargs rm -rf

.PHONY: tests coverage setup release release-public clean