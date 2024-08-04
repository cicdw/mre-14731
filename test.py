from prefect import flow, task
from my_14731_sub.blocktypes.test_block import TestBlock


@flow(log_prints=True)
def process_function():
    print("I'm here")
