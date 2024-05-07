import zeroconf, zeroconf._utils.ipaddress, zeroconf._handlers.answers # required by pyinstaller!
import os, json, subprocess, pychromecast

# Config file exists?
config_file = "Chromecast.json"
if os.path.exists(config_file) == False:
    input("Chromecast.json not found...")
    exit(1)

# Read config file
with open(config_file, 'r') as file:
    config = json.load(file)

# Variables
media_url = config["media_url"]
media_type = config["media_type"]
vlc_exe = config["vlc_exe"]

# Discover Chromecasts on the network
chromecasts, browser = pychromecast.get_chromecasts()

# Play on each chromecast
for chromecast in chromecasts:
    # Print chromecast name
    print("Chromecast:", chromecast.name)
    # Wait for the Chromecast to be ready
    chromecast.wait()
    # Access the media controller
    mc = chromecast.media_controller
    # Load and control media
    mc.play_media(media_url, media_type)
    # Wait for the media to be playing
    mc.block_until_active()

# Play the audio (if vlc exe exists)
if os.path.exists(vlc_exe):
    subprocess.run([vlc_exe] + [media_url, "--no-video"])
else:
    print("VLC exe not found")

# Everything OK
exit(0)
