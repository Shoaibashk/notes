all: check convert build deploy
	

build: 
	mkdocs build

check:
	git pull

convert:
	python3 convert.py

deploy:
	mkdocs gh-deploy

serve: convert
	mkdocs serve
	