from apscheduler.schedulers.blocking import BlockingScheduler

def job_function():
    print("Hello World")

sched = BlockingScheduler()

# Schedules job_function to be run 6 times per hour
sched.add_job(job_function, 'cron', minute='0,10,20,30,40,50')

sched.start()
