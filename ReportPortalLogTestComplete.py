import os
import subprocess
import traceback
from mimetypes import guess_type
from time import time

from reportportal_client import ReportPortalService


def timestamp():
    return str(int(time() * 1000))


endpoint = +++++++++++++++++++++++++++
project = +++++++++++++++++++++++++++
token = +++++++++++++++++++++++++++
launch_name = +++++++++++++++++++++++++++
launch_doc = "Testing logging"


def my_error_handler(exc_info):
    print("Error occurred: {}".format(exc_info[1]))
    traceback.print_exception(*exc_info)


service = ReportPortalService(endpoint=endpoint, project=project, token=token)

launch = service.start_launch(name=launch_name, start_time=timestamp(), description=launch_doc)

item_id = service.start_test_item(name="Test Case", description="First Test Case",
                                  start_time=timestamp(), item_type="STEP", parameters={"key1": "val1", "key2": "val2"})

service.log(time=timestamp(), message="Hello World!", level="INFO", item_id=item_id)

image = Log.Picture(Sys.Desktop, "Поле тип доставки")
with open(image, "rb") as fh:
    attachment = {"name": os.path.basename(image), "data": fh.read(), "mime": "image/png"}
    service.log(timestamp(), "Screen shot of issue.", "INFO", attachment, item_id=item_id)

service.finish_test_item(item_id=item_id, end_time=timestamp(), status="PASSED")

service.finish_launch(end_time=timestamp())

service.terminate()