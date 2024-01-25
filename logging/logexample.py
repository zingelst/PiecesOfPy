# System level logging facility, more flexible than print
import logging
import logging.handlers
# Create a logger for this module
LOG = logging.getLogger(__name__)
# StreamHandler will print to the stdout, lke print
LOGHANDLER = logging.StreamHandler()
# Give the logmessage a format-> Time:filename:lineno(function) - message
LOGFORMAT = logging.Formatter("%(asctime)s:[%(filename)s:%(lineno)d](%(funcName)s) %(message)s")
# Add the handler and formatter to the Log object and we can now use it
# albeit it will be at the ERROR level, so LOG.info and LOG.debug will not print
# until you set LOG.setLevel(logging.DEBUG) or some other level.
LOGHANDLER.setFormatter(LOGFORMAT)
LOG.addHandler(LOGHANDLER)

LOG.setLevel(logging.DEBUG)

log.debug("Hello")
