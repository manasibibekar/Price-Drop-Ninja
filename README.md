# Price Drop Ninja

Price Drop Ninja is a web scraping tool for Amazon that extracts daily prices from a given URL and notifies users via email when a product's price drops below their specified threshold. The tool is designed to save users' valuable time and effort by automating the process of collecting accurate and up-to-date data. With Price Drop Ninja, users can make informed purchasing decisions and take advantage of cost savings opportunities.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

Python, Beautiful Soup and smtplib should be setup on the machine. You need to have a gmail account which will be used to send emails.

### Setting up app password in Google account

Go to your gmail account. 
1. Enable 2-Step Verification. Go to your Google Account > Security > Signing in to Google, and select 2-Step Verification.
2. Next, create an app password. Select ‘App passwords’ under ‘2-Step Verification’ and you will see a window. Select ‘Other’ in the ‘Select app’ dropdown.
3. Enter a name, e.g. emailsender, and click ‘GENERATE’. Note this name has no link to the Python script and it could be anything.
4. You will get a new 16-character app password (e.g. xnwbjmgvjeeevlgc). You need to store this in your password variable which will be mentioned below.


### Installing 

Clone the main branch
```
git clone https://github.com/manasibibekar/PriceDrop-Ninja.git
```
Navigate to the directory
```
cd PriceDrop-Ninja
```
create a new env file named ".env" 
Open the file and store the required variables in it. Example is shown below
```
url = <url of the amazon product whose price you want to track>

sender = <your gmail address from where you want to send emails>

password = <app password which you saved previously>

receiver = <your gmail address on which you want to receive the emails>

buy_price_threshold = <the price threshold you want to set>
```

## Built With

* Python
* Beautiful Soup 
* smtplib

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
