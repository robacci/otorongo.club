if ! crontab -l | grep -q 'send_tweet'; then
  echo 'entry does not exist'
  (crontab -l 2>/dev/null; echo "20,40,59 13-3/1 * * * /code/python manage.py send_tweet") | crontab -
fi
