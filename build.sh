chmod +x material.sh

if [ -d "docs/material" ] 
then
    echo "Directory custom-Material-theme exists." 
    mkdocs gh-deploy
else
    echo "Directory custom-Material-theme does not exists."
    ./material.sh
fi


