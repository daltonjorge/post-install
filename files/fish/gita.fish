function gita --description "Run git command for all git repositories inside current dir"
  find . -type d -name .git -execdir git $argv \; 
end
