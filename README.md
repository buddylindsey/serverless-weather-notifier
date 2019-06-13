# Serverless Weather Notifier

This is a simple notification tool to deploy and get weather updates at certain times for specific locations. I use this to know what the weather is in the morning and the afternoon. This is great for the afternoon as I need to work on my farm 🚜, and this automates knowing the weather before I go outside to know whether I should go now or in an hour or two.

The goal of this is/was to be self-contained in a single serverless function so it is deployable for anyone and "Just Works"™️. 

## Deployment

### Step 1 - Environment

We need to set environment variables. Those are pulled from SSM Parameter store. So you need to set the following.

```
darksky.api.key
twilio.sid
twilio.token
twilio.from
```

### Step 2 - Location and People

Set your location data of where, and who, you want to get the data. Also set the hours in UTC you want messages to go out.

```python
LOCATIONS = [
    {
        "location": "36.153980,-95.992775",
        "number": "+11233211234",
        "preferred_times": [13, 20],
    },
    {
        "location": "35.481918,-97.508469",
        "number": "+11233211234",
        "preferred_times": [14, 20],
    },
]
```

### Step 3 - Deploy

```bash
$ sls deploy
```

## Development

Development is pretty easy right now here are some general steps.

1. Fork the repo
1. Checkout the code from your fork
1. Set the environment variables (check below)
1. Make tweaks
1. Set `LOCATIONS` based on section above in deployment
1. Run the code `python handler.py`

```
DARK_SKY_API_KEY
TWILIO_ACCOUNT_SID
TWILIO_AUTH_TOKEN
TWILIO_FROM
```

## Contributions

If you would like to contribute back I would be very appreciative. Feel free to open up some PR's.