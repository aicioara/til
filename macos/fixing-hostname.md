# Fixing Hostname

Sometimes, on macOS, the terminal will display the IP address instead of the hostname.

Expected

```
aicioara@matrix
```

Actual

```
aicioara@192-168-0-102
```

This is because the HostName is not set. We can check, then fix this using

```bash
# Check that there is no host name set
scutil --get HostName

# Set the hostname
sudo scutil --set HostName 'matrix'
```
