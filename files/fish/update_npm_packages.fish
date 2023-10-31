function update_npm_packages --description 'Update NPM packages'
  if not test -e package.json
    echo "OH NO... WE NEED A NODE PROJECT WITH PACKAGE.JSON file !"
    return 1
  end
  set -l PACOTES (npm ls | grep -o -E "(@\w*/)?(\w|-)*@[0-9.]+\$")
  for word in $PACOTES
    echo "UPDATING $word..."
    npm install $word
  end
end
