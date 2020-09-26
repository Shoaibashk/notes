chmod +x material.sh

if [ -d "docs/material" ] 
then
    echo "Directory custom-Material-theme exists." 
else
    echo "Directory custom-Material-theme does not exists."
    ./material.sh
fi


mkdocs gh-deploy