# Python SQL Reporting Services Download


This python module automates the download of SQL Reporting Services (SSRS) reports using a list of dates


## Overview
This project was created to make the mundane task of downloading reports scalable.  I originally created it because a client needed dozens of copies of a report, each run with slightly different parameters.  It was too cumbersome for them to run the report manually so they asked for an automated solution.  This was the result.  

I use it every few months when a big request comes through.  

## Configuration

The file is driven by a configuration file.  It is a JSON formatted file that will download a report from the SSRS server for every JSON object in an array.  Each JSON object contains a new set of parameters to pass to the report.  

## Usage

The functions in download_ssrs can be called from a script, or a package can be created using the "setup.py" file.  

An example of how to call the script is provided in main.py.  
