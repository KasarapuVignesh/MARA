from apscheduler.schedulers.blocking import BlockingScheduler
from graph.pipeline import build_graph
import datetime

def run_pipeline():
    print(f"🚀 Running pipeline at {datetime.datetime.now()}")
    graph = build_graph()
    graph.invoke({})

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    # Run daily at 7AM
    scheduler.add_job(run_pipeline, "cron", hour=23, minute=51)
    print("✅ Scheduler started. Waiting for 7AM daily jobs.")
    scheduler.start()
