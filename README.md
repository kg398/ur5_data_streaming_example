min working example in ur5_data_streaming_example.py, seems to work okay with >100hz frequency
after stopping stream you need to wait a bit for all the data to come through before flushing with robot.ping()
keep in mind that during streaming you won't be able to get any other data from the robot so you cannot do any .get functions and other functions should be run with wait=False to stop them sending data back
