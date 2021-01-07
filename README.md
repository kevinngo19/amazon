# amazon
A python app that tracks amazon prices and send email about it

Instructions:
1. Go to https://myaccount.google.com/lesssecureapps. Then turn on Less Secure Mode.
2. Install python 3.9 from here https://www.python.org/downloads/release/python-390/. If you already have python 3.9.0, skip this step.
3. For Windows Users:
   - Open Command Prompt
   - Type py -m pip install requests in command prompt, wait to do its thing until its finished.
   - Type py -m pip install bs4 in command prompt, wait to do its thing until its finished.
   For Linux, MacOS users:
   - Open Terminal
   - Type py -m pip install requests in command prompt, wait to do its thing until its finished.
   - Type py -m pip install bs4 in command prompt, wait to do its thing until its finished.
   
   Once you correctly entered those commands, move to Step 4. If you have errors please report it by filling a Issue report.
4. Go to <The Amazon Folder> and open login_details.txt
5. Fill in login_details (For now im not bothered adding keys and other shit):
 - First line should be your gmail
 - Second line should be the password for your gmail
 - Third line should be the email you are sending to.
   Example (This should be like this):
 
6. Save login_details.txt and close the file.
7. Open command prompt and do cd <To the folder where amazon_prices.py + data folder is located>
8. Do execute py -m venv venv
9. Once it has finished, execute py amazon_prices.py, It should start the program. 

