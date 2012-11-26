#!/bin/bash

sar -u 1 | sed -u -e '1,3d' |
while read time cpu usr nice sys io steal idle;
do
    NOW=$(date +%s)

    echo put cpu.util $NOW $usr time=user
    echo put cpu.util $NOW $sys time=system
    echo put cpu.util $NOW $io time=io
    echo put cpu.util $NOW $idle time=idle
    # Report values to standard error.
    echo timestamp:$NOW user:$usr sys:$sys io:$io idle:$idle >&2
done | nc -w 30 localhost 4242
