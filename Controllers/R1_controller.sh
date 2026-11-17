#!/bin/sh

SECRET="REPLACE_WITH_YOUR_CONTROLLER_SECRET"
LOG="/root/controller.log"

echo "Adaptive Routing Controller Started: $(date)" >> "$LOG"

while true; do
    nc -l -p 5050 | while IFS=: read -r received status || [ -n "$received$status" ]; do

        [ "$received" = "$SECRET" ] || continue

        case "$status" in
            CONGESTED)
                vtysh -c "configure terminal" \
                      -c "interface eth0" \
                      -c "ip ospf cost 500" \
                      -c "end"
                echo "$(date) CONGESTED: OSPF cost set to 500" >> "$LOG"
                ;;
            NORMAL)
                vtysh -c "configure terminal" \
                      -c "interface eth0" \
                      -c "ip ospf cost 100" \
                      -c "end"
                echo "$(date) NORMAL: OSPF cost set to 100" >> "$LOG"
                ;;
        esac
    done
done
