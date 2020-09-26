all:
	./build.sh

build:
	mkdocs build

deploy:
	mkdocs gh-deploy


	