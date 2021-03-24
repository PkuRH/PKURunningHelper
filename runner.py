#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: runner.py

from util import (
     Config, Logger,
     json,
)

config = Config()
logger = Logger("runner")

from PKURunner import PKURunnerClient as Client


try:
    client = Client()
    client.run()
except Exception as err:
    logger.error("upload record failed !")
    raise err
else:
    logger.info("upload record success !")
