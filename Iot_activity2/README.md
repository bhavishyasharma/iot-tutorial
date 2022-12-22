# Iot_activity2
## Sub task
* Get and store the client name from command line argument.
* Set this as client name for client object.
* Subscribe to the “location/client_name” topics where "client_name" are given in python list called all_clients and do not subscribe to location topic of a client itself.
* Write code to publish your current location on topic “location/<client_name>” where client_name is current client name, sleep for 2 seconds and repeat.
* Complete on_message() method.
* * Extract location data from received message.
* * Extract client name from received message.
* * Calculate Distance from your current location.(Distance function is provided).
* * Store the client name if distance is less than 20 meters in list contacts already defined
* To test your code run activity2.sh

