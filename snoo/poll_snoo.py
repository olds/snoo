from snoo import Client as SnooClient
import time

def main():
    snoo = SnooClient()
    last_status = "ONLINE"

    while True:
        if snoo.raw_status() != last_status:
            snoo.text_parent(last_status, snoo.raw_status())
            last_status = snoo.raw_status()
        if snoo.raw_status() == "TIMEOUT":
            snoo.call_parent()
        time.sleep(60)

if __name__ == "__main__":
    main()