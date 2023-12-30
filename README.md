
# Auto Honeygain Luckypot collector with Notification to ANDROID/iOS Daily

email - to your honeygain email address <br>
pass - enter password  <br>
subscription - create custom ntfy subscription from https://ntfy.sh/ and enter the subscriber name <br>

## Usage/Examples

Setup a cronjob as below to run automatically and daily
``` shell
7 08 * * * python3 /home/alpha/honeygain.py >> /home/alpha/logs/honeygain.log 2>&1
```

