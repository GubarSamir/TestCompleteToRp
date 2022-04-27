from ReportPortalLoger import LogerRP, timestamp, screenshot

loger = LogerRP()

launch = loger.service.start_launch(name='Test Complete first test', start_time=timestamp(), description='Launch1')

item_id = loger.service.start_test_item(name="Test 1", description="First Test Complete Case",
                                        start_time=timestamp(), item_type="STEP",
                                        parameters={"key1": "val1", "key2": "val2"})


def simple_test():
    x = 2 + 2
    return x


if simple_test() == 4:
    loger.service.log(time=timestamp(), message="x = 4", level="INFO", item_id=item_id, attachment=screenshot())
    loger.service.finish_test_item(item_id=item_id, end_time=timestamp(), status="PASSED")
else:
    loger.service.log(time=timestamp(), message="x != 4", level="INFO", item_id=item_id, attachment=screenshot())
    loger.service.finish_test_item(item_id=item_id, end_time=timestamp(), status="FAILED")

# ---------------------------------------------------------------------------------------------------


item_id = loger.service.start_test_item(name="Test 2", description="Second Test Complete Case",
                                        start_time=timestamp(), item_type="STEP",
                                        parameters={"key1": "val1", "key2": "val2"})


def simple_test2():
    x = 2 + 3
    return x


if simple_test2() == 4:
    loger.service.log(time=timestamp(), message="x = 4", level="INFO", item_id=item_id, attachment=screenshot())
    loger.service.finish_test_item(item_id=item_id, end_time=timestamp(), status="PASSED")
else:
    loger.service.log(time=timestamp(), message="x != 4", level="INFO", item_id=item_id, attachment=screenshot())
    loger.service.finish_test_item(item_id=item_id, end_time=timestamp(), status="FAILED")

loger.service.finish_launch(end_time=timestamp())
loger.service.terminate()