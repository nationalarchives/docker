FROM tna-python

ENV TNA_APPLICATION_ENTRYPOINT=test-app

COPY --chown=app . .

RUN tna-build

CMD ["tna-run"]
