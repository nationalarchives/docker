import pendulum

def application(env, start_response):
    now = pendulum.now("Europe/Paris")

    # Changing timezone
    now.in_timezone("America/Toronto")

    # Default support for common datetime formats
    now.to_iso8601_string()

    # Shifting
    now.add(days=2)

    data = ""
    data = data + "Hello world"
    # data = data + now
    start_response(
        "200 OK", [("Content-Type", "text/plain"), ("Content-Length", str(len(data)))]
    )
    return [bytes(data, "utf-8")]