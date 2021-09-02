#!/usr/bin/python3

import random
import sys

from time import sleep


def read_stdin():
    readline = sys.stdin.readline()
    while readline:
        yield readline
        readline = sys.stdin.readline()


if __name__ == '__main__':
    start_stress = 0
    nick = ''
    channel = ''
    stress_sleep = 1

    for line in read_stdin():
        line = line.split()

        if line[0].startswith('PASS'):
            try:
                stress_sleep = int(''.join(filter(str.isdigit, line[1])))
            except ValueError:
                stress_sleep = 1

        if line[0].startswith('NICK'):
            nick = line[1]
            print(f":tmi.twitch.tv 001 {nick} :Welcome, GLHF!")
            print(f":tmi.twitch.tv 002 {nick} :Your host is tmi.twitch.tv")
            print(f":tmi.twitch.tv 003 {nick} :This server is rather new")
            print(f":tmi.twitch.tv 004 {nick} :-")
            print(f":tmi.twitch.tv 375 {nick} :-")
            print(f":tmi.twitch.tv 372 {nick} :You are in a maze of twisty passages, all alike.")
            print(f":tmi.twitch.tv 376 {nick} :>")
            sys.stdout.flush()

        if line[0].startswith('JOIN'):
            channel = line[1]
            print(f":{nick}!{nick}@{nick}.tmi.twitch.tv JOIN {channel}")
            print(f":{nick}.tmi.twitch.tv 353 {nick} = {channel} :{nick}")
            print(f":{nick}.tmi.twitch.tv 366 {nick} {channel} :End of /NAMES list")
            sys.stdout.flush()
            start_stress = 1

        if start_stress == 1 :
            random_num = random.randint(1, 5)
            random_user_num= "%06d" % random.randint(1, 999999)
            random_nick = f"twUser{random_user_num}"
            while True:
                print(f":{random_nick}!{random_nick}@{random_nick}.tmi.twitch.tv PRIVMSG {channel} :{random_num}")
                sys.stdout.flush()
                random_num = random.randint(1, 5)
                random_user_num = "%06d" % random.randint(1, 999999)
                random_nick = f"twUser{random_user_num}"
                sleep(stress_sleep/1000)


