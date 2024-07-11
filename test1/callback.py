def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    data = message.data.decode("UTF-8")
    data = json.loads(data)

    localID = data["protoPayload"]["response"]["localId"]
    email = data["protoPayload"]["response"]["email"]
    insertID = data["insertId"]

    logger.info(f"{localID},{email},{insertID}")
    message.ack()