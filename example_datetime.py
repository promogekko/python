import datetime
import pytz
import iso8601


def utcnow():
    return datetime.datetime.now(tz=pytz.utc)

print(utcnow())
print(utcnow().isoformat())
print(iso8601.parse_date(utcnow().isoformat()))

print(iso8601.parse_date(utcnow().isoformat()) < utcnow())

