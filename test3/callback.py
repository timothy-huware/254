def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    data = message.data.decode("UTF-8")
    data = json.loads(data)

    # wait a random amount of time between 60 and 100 seconds
    rand_time = random.randint(60, 100)
    time.sleep(rand_time)

    localID = data["protoPayload"]["response"]["localId"]
    email = data["protoPayload"]["response"]["email"]
    insertID = data["insertId"]

    logger.info(
        f"{localID},{email},{insertID}, waited for {rand_time}s, message id: {message.message_id}"
    )

    ack_future = message.ack_with_response()

    try:
        # Block on result of acknowledge call.
        # When `timeout` is not set, result() will block indefinitely,
        # unless an exception is encountered first.
        ack_future.result()
        print(f"Ack for message {message.message_id} successful.")
    except sub_exceptions.AcknowledgeError as e:
        print(f"Ack for message {message.message_id} failed with error: {e.error_code}")