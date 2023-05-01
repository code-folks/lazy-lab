#!/usr/bin/env bash
echo "- Putting all the 🔬 on table."
pip install -r ./cli/requirements.txt --exists-action s --quiet &> /dev/null
echo "- Making new command executable."
chmod u+x ./lab
./lab --install-completion &> /dev/null
echo -e "\033[1;32mSuccess! remember to wear your 🥼 in labolatory.\033[0;0m"
echo "Restart shell to use auto-completition for a new CLI."
echo -e "Use \033[1;36m./lab --help\033[0;0m to check what you can do."
