# Notifier

The notifier app for notifying the visa interviw appointment slots message thread in the Telegram USVN Nepal Channel.


### How app works?

Listens to the message (which is update given in the slot update group) in channel, and if contains specified date string in the message then sends the rings the siren and sends the sms accordingly.
There must be a telegram channel which is a source for the information 
   about the visa appointment. The  messages casted in the telegram is listened by the application 
   and consumed for further implementation. 

   **Eg. of source channel:** SVN F1 Slot Update[No Discussion] 
                          [channel-link](https://t.me/+g7--U_SaNBpmMDU1)
   **Reference Usage:** ``` credentials.py``` --> ```CHANNEL_USERNAME```

### To execute the program

1. Install dependencies using ```pip install -r requirements.py```
2. Configure telegram api account and update the ``` credentials.py``` accordingly.
3. Configure twillio api account for the sms configuration and update the ``` credentials.py``` accordingly.


 ```
 python main.py

 ```

### Note: 
This repo also contains the file named app.py which is the Flask application (server)
         if in case you want to host the request.
