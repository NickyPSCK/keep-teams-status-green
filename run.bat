@ECHO OFF
title "G-TECH: Unleash Green Energy"
pushd "%~dp0"
call conda activate base
cmd /k python ./run.py --time 60 --no-color --status --logo
:: cmd /k python ./run.py --time 60 --color --status --logo
:: pause
