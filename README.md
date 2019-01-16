# mqtt-keepalive

Simple python app to send keepalive messages to an MQTT broker to verify connectivity from the end devices

## Configuration

The application needs two environment variables to be set:

- MQTT_SERVER - address of the server to send to
- MQTT_TOPIC  - topic on the broker to publish the keepalives to
