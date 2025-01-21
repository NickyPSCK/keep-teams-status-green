@ECHO OFF
title "G-TEC: Unleash Green Energy"
pushd "%~dp0"
call conda activate base
cmd /k python ./run.py --time 60
:: cmd /k python ./run.py --time 60 --classic
:: pause
