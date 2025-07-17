@ECHO OFF
title "G-TEC: Unleash Green Energy"
pushd "%~dp0"
call conda activate base
cmd /k python ./run.py --time 60 --exemped-period 11:30:00-13:00:00 17:15:00-19:00:00
:: cmd /k python ./run.py --time 60 --classic
:: pause
