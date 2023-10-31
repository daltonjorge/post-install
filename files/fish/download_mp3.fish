function download_mp3 --description "Download mp3 audio from youtube url"
  yt-dlp -x --audio-format mp3 --embed-thumbnail --metadata-from-title "%(artist)s - %(title)s" $argv
end

