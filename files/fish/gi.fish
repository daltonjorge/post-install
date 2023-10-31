function gi --description "get an gitignore file"
  curl -sLw n https://www.gitignore.io/api/$argv ;
end

