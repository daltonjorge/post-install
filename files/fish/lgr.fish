function lgr -d 'List Git Repos'
  find . -name .git -type d -exec dirname {} \;
end
