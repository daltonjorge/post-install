function webcrawler --description "Download a site"
  wget -r -np -nc -k -c $argv
end

