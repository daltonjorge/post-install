function rando
  alias rando="cat /dev/urandom | base64 | tr -dc 'a-km-zA-KM-Z02-9-_!@#\$%^&*+|' | fold -w 16 | head -n 4"
end
