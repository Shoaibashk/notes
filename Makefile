all: check convert build deploy
	

build: convert
	mkdocs build

check:
	git pull

convert:
	python3 convert.py

deploy: pull build convert
	mkdocs gh-deploy

serve: convert
	mkdocs serve
	