#be sure to modify paths in plist and monitor programbrew install python3

pip3 install watchdog

sudo chown root /Library/LaunchDaemons/com.zeke.monitor.plist
sudo chgrp wheel /Library/LaunchDaemons/com.zeke.monitor.plist