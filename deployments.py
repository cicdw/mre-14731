from test import process_function
from prefect.runner.storage import GitRepository
from prefect.blocks.system import Secret

if __name__ == "__main__":
    process_function.from_source(
        source=GitRepository(
            url="https://github.com/cicdw/mre-14731.git",
            include_submodules=True,
        ),
        entrypoint="test.py:process_function",
    ).deploy(name="test", work_pool_name="test")
