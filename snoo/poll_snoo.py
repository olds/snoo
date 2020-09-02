from snoo import Client as SnooClient
import time

def main():
    snoo = SnooClient()
    last_call = '2000 01-01-01 00:00:00'

    while True:
        if snoo.raw_status() == "TIMEOUT":
            snoo.call_parent()
        time.sleep(60)

if __name__ == "__main__":
    main()