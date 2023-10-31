function create-ts-project --description "Create a blank typescript project"
  git init
  npx license (npm get init.license) -o "(npm get init.author.name)" > LICENSE
  npx gitignore node
  npx covgen "(npm get init.author.email)"
  npm init -y
  npm i typescript @types/node jest ts-jest @types/jest -D
  npm i commitizen git-cz -g
  npx ts-jest config:init
  commitizen init git-cz --save-dev --save-exact
  npx tsc --init
  mkdir src
  touch src/index.ts
  mkdir test
  touch test/index.spec.ts
  git add -A
  git commit -m "Initial commit"
end
