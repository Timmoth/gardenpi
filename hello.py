from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import sys


def runJob():
    print("hello, world")


scheduler = BlockingScheduler()
scheduler.add_job(runJob, 'interval', seconds=2)
scheduler.start()
