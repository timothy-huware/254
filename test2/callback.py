def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    data = message.data.decode("UTF-8")
    data = json.loads(data)

    type = "protoPayload" if "protoPayload" in data else "jsonPayload"

    localID = data[type]["response"]["localId"]
    email = data[type]["response"]["email"]
    insertID = data["insertId"]

    logger.info(f"{localID},{email},{insertID}, message id: {message.message_id}")

    ack_future = message.ack_with_response()

    try:
        # Block on result of acknowledge call.
        # When `timeout` is not set, result() will block indefinitely,
        # unless an exception is encountered first.
        ack_future.result()
        print(f"Ack for message {message.message_id} successful.")
    except sub_exceptions.AcknowledgeError as e:
        print(f"Ack for message {message.message_id} failed with error: {e.error_code}")