# Insta-meet

## This is a simple web app to create a zoom meeting using zoom api and django.

## There are two endpoints:

### 1. <i>generate_token</i> : this endpoint takes a post request where your give the Api key and secret as data and the response is the jwt token generated for creating meeting.

### 2. <i>create_meet</i> : here your provide the details of the meeting and a jwt token and this returns the meeting link or the error if generated.
