FROM tna-python

COPY --chown=app . .

RUN tna-build

CMD ["tna-run", "my-tna-app:app"]
