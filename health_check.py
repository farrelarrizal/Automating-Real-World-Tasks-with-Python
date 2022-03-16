#!/usr/bin/env python3

import socket
import shutil
import psutil
import emails

username = 'student-04-47458cb06c80'


def check_cpu_usage():
    # verify that's have enough unused cpu
    usage = psutil.cpu_percent()
    return usage < 80


def check_disk_usage(disk):
    # verify that's have enough capacity
    disk = shutil.disk_usage(disk)
    free = disk.free/disk.total * 100
    return free > 20


def check_memory_usage():
    memory = psutil.virtual_memory().available
    total = memory / (1024.0 ** 2)
    return total > 500


def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost


def send_notification_alert(messages):
    sender = 'automation@example.com'
    recipient = '{}@example.com'.format(username)
    subject = messages
    body = 'Please check your system and resolve the issue as soon as possible.'
    attachment_file = ''
    email = emails.generate_email(sender, recipient, subject, body, attachment_file)
    emails.send_email(email)


def main():
    # condition notification
    message = ''
    if not check_cpu_usage():
        message = 'Error - CPU usage is over 80%'
    if not check_disk_usage('/'):
        message = 'Error - Available disk space is less than 20%'
    if not check_memory_usage():
        message = 'Error - Available memory is less than 500MB'
    if not check_localhost():
        message = 'Error - localhost cannot be resolved to 127.0.0.1'
    if message:
        send_notification_alert(message)
    else:
        print('SYSTEM OK!')


if __name__ == "__main__":
    main()