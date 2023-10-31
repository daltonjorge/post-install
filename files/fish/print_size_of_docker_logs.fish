function print-size-of-docker-logs
  sudo sh -c "du -ch /var/lib/docker/containers/*/*-json.log";
end
