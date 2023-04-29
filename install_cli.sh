#!/usr/bin/env bash
echo ">>  Installing 🌊 so your 🐋 can start swimming."
pip install -r ./cli/requirements.txt --exists-action s --quiet &> /dev/null
echo ">>  Making new command executable."
chmod --reference=install_cli.sh ./lab
./lab --install-completion &> /dev/null
echo ">>  Success... ✅"
echo -e ">>  Use \033[1;36m./lab --help\033[0;0m to check what you can do."
echo -e ">>  📬 Restart shell to use auto-completition for a new CLI."
