git clone https://github.com/squidfunk/mkdocs-material

cd mkdocs-material

python setup.py build

mv build/lib/material ../docs

cd ..

rm -rf mkdocs-material

