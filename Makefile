tests:
	python -m unittest discover tests

coverage:
	coverage run --source=./pylars -m unittest discover tests
	coverage report -m
	coverage erase

release: clean
	python setup.py sdist bdist_wheel
	twine upload --repository-url $(PYLAR_UPLOAD_URL) dist/*

clean:
	rm -rf debug.py
	rm -rf .coverage
	rm -rf build dist *.egg-info
	find pylars -iname __pycache__ | xargs rm -rf
	find tests  -iname __pycache__ | xargs rm -rf

.PHONY: tests coverage release clean