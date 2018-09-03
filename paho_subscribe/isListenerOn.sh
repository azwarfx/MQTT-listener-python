#!/bin/bash
RESULTPYTHON=`pgrep -x python`

if [ "${RESULTPYTHON:-null}" = null ]; then
   python /root/paho_subscribe/subscriber.py
fi