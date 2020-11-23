# earnings-stock-calendar
Leveraging browerstack to grab upcoming earnings report for canadian stock tickers and label my dedicated calendars.


In order to encode secret files in repos, I tend to use base64 by default this words the output unless the `-w 0` flag is given.

```
base64 stocks.json -w 0 > stocks.txt
```

To set environment variable in windows

```
setx GOOGLE_SERVICE_CREDS "%USERPROFILE%\aws\cert.pem"
```

This is based on a private repo called stock-scrapper-selenium.

