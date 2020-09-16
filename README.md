# PDF to Audio
A python script that automatically converts any pdf into an audio and reads it to you.

## What does it do?
It performs the following processes:
1. Reads the PDF provided
2. Uses the text extracted from the PDF and reads it to you

## How to use?
1. The best way to use my script is to firstly clone the git repo where you want to.
2. Select PDF to convert

## What happens behind the scene?
1. The function "convert_pdf_to_txt" parses the pdf and saves the text 
2. Using pyttsx3, the text is fed to the function say() which produces an audio of the whole text
