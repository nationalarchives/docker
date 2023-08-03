import pendulum


def app(environ, start_response):
    now = pendulum.now("Europe/London")
    data = ("<h1>Hello world</h1>"
            f"<p>The date is {now.to_iso8601_string()}")
    status = "200 OK"
    response_headers = [
        ('Content-type', 'text/html'),
        ('Content-Length', str(len(data)))
    ]
    start_response(
        status, response_headers
    )
    return [bytes(data, "utf-8")]
