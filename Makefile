all:
	./build.sh

build:
	mkdocs build

deploy:
	mkdocs gh-deploy

check:
	git pull
	