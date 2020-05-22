
test: 
	pytest -v -s
results:
	pytest --html="tests/results.html"

lint:
	flake8 graph

export-conda:
	conda env export > environment.yml

biped-spine:
	python mightyRig/guides/biped/spineGuide.py

add:
	conda env export > environment.yml 
	git add .

run:
	python mightyRig.py

clean:
	find . -name "*.pyc" -type f -delete
	find . -name "__pycache__" -delete
