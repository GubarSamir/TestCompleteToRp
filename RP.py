import os
import traceback
import subprocess
from time import time
from mimetypes import guess_type
from reportportal_client import ReportPortalService


def timestamp():
    return str(int(time() * 1000))


def screenshot():
    image = Log.Picture(Sys.Desktop, "screen")
    with open(image, "rb") as fh:
        screen = fh.read()
    attachment = {"name": os.path.basename(image), "data": screen, "mime": "image/png"}
    return attachment


class LogerRP:
    endpoint = "http://ubuntu-testers:8080"
    project = "import"
    token = "99117b70-e70f-46ba-9056-f5c2440c26af"
    launch_name = "sa.gubar_TEST_EXAMPLE"
    launch_doc = "Testing logging"

    def __init__(self):
        self.os = os
        self.traceback = traceback
        self.subprocess = subprocess
        self.guess_type = guess_type
        self.ReportPortalService = ReportPortalService

    def my_error_handler(self, exc_info):
        print("Error occurred: {}".format(exc_info[1]))
        self.traceback.print_exception(*exc_info)

    service = ReportPortalService(endpoint=endpoint, project=project, token=token)

    ################## Запуск лаунча и установка имени ##################
    # launch = service.start_launch(name=launch_name, start_time=timestamp(), description=launch_doc)

    ################## Запуск теста и установка имени теста ##################
    # item_id = service.start_test_item(name="Test Case", description="First Test Case",
    #      start_time=timestamp(), item_type="STEP", parameters={"key1": "val1", "key2": "val2"})

    ################## Лог сообщение ##################
    # service.log(time=timestamp(), message="Hello World!", level="INFO", item_id=item_id)

    ################## Добавление скриншота ##################
    # attachment = {"name": os.path.basename(image), "data": screenshot(image), "mime": "image/png"}
    # service.log(timestamp(), "Screen shot of issue.", "INFO", attachment, item_id=item_id)

    ################## Завершение теста ##################
    # service.finish_test_item(item_id=item_id, end_time=timestamp(), status="PASSED")

    ################## Завершение лаунча ##################
    # service.finish_launch(end_time=timestamp())

    ################## Отключение сервиса ##################
    # service.terminate()

# def start():
#  launch = service.start_launch(name=launch_name, start_time=timestamp(), description=launch_doc)
#  return launch
#
#
# def start_rp(function):
#  def wrapper():
#    func = function()
#    start_suite = func.start()
#    return start_suite
#  return wrapper


# import os
# import subprocess
# import traceback
# from mimetypes import guess_type
# from time import time
#
# from reportportal_client import ReportPortalService
#
#
# def timestamp():
#    return str(int(time() * 1000))
#
#
# endpoint = "http://ubuntu-testers:8080"
# project = "import"
# token = "99117b70-e70f-46ba-9056-f5c2440c26af"
# launch_name = "sa.gubar_TEST_EXAMPLE"
# launch_doc = "Testing logging"
#
#
# def my_error_handler(exc_info):
#    print("Error occurred: {}".format(exc_info[1]))
#    traceback.print_exception(*exc_info)
#
#
# service = ReportPortalService(endpoint=endpoint, project=project, token=token)
#
#
# launch = service.start_launch(name=launch_name, start_time=timestamp(), description=launch_doc)
#
#
# item_id = service.start_test_item(name="Test Case", description="First Test Case",
#          start_time=timestamp(), item_type="STEP", parameters={"key1": "val1", "key2": "val2"})
#
#
# service.log(time=timestamp(), message="Hello World!", level="INFO", item_id=item_id)
#
#
# image = Log.Picture(Sys.Desktop, "Поле тип доставки")
# with open(image, "rb") as fh:
#    attachment = {"name": os.path.basename(image), "data": fh.read(), "mime": "image/png"}
#    service.log(timestamp(), "Screen shot of issue.", "INFO", attachment, item_id=item_id)
#
#
# service.finish_test_item(item_id=item_id, end_time=timestamp(), status="PASSED")
#
# service.finish_launch(end_time=timestamp())
#
# service.terminate()