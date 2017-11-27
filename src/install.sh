c#cd "{query}"

#!/bin/sh
echo "Welcome to Alfred Plugin"
echo "     _____ ______________  ______"
echo "    / ___// ____/_  __/ / / / __ \\"
echo "    \\__ \\/ __/   / / / / / / /_/ /"
echo "   ___/ / /___  / / / /_/ / ____/"
echo "  /____/_____/ /_/  \\____/_/"
echo "  "
echo Required pacakges will be installed to:
echo 
echo $(pwd)/lib
echo



while true; do
    read -p "Do you wish to install these dependencies? (y/n) " yn
    case $yn in
        [Yy]* ) python missing.py install; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done




osascript -e 'tell application "Alfred 3" to run trigger "open_missing_command" in workflow "org.jeef.alfred.missingPackages" with argument "missing"'
exit