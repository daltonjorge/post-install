function restart-sound --description 'restart sound config'
  rm -rf ~/.config/pulse
  systemctl --user restart wireplumber pipewire pipewire-pulse
  systemctl --user daemon-reload
end
