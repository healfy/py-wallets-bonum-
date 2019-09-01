import pytz
import requests
from decimal import Decimal
from datetime import datetime
from threading import Thread
from marshmallow import fields
from google.protobuf import timestamp_pb2
from wallets import app


def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        thread.join()
        return thread
    return wrapper


def get_msg_timestamp_from_datetime(value):
    msg = timestamp_pb2.Timestamp()
    if value is not None:
        msg.FromDatetime(value.astimezone(pytz.utc).replace(tzinfo=None))
    return msg


class DecimalStringField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        return str(value) if value is not None else None

    def _deserialize(self, value, attr, obj, **kwargs):
        if not value or value == 'None':
            return None
        return Decimal(value)


class DatetimeField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        return get_msg_timestamp_from_datetime(value)

    def _deserialize(self, value, attr, obj, **kwargs):
        if value is not None and value != 'None' and type(value) != str:
            return value.ToDatetime().replace(tzinfo=pytz.utc)
        elif type(value) == str:
            return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=pytz.utc)
        return value


def send_message(html, subject):

    url = f'https://api.mailgun.net/v3/{app.config["MAIL_DOMAIN"]}/messages'
    auth = ('api', f'{app.config["MAIL_PASSWORD"]}')
    data = {
        'from': f'Mailgun User <{app.config["MAIL_USERNAME"]}>',
        'to': app.config["RECIPIENTS"],
        'subject': subject,
        'html': html,
    }
    response = requests.post(url, auth=auth, data=data)
    response.raise_for_status()
