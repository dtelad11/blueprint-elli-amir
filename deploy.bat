call heroku config:set VITE_API_BASE_URL=https://blueprint-elli-amir-ac8042d2a76d.herokuapp.com --app blueprint-elli-amir

call heroku buildpacks:clear --app blueprint-elli-amir
call heroku buildpacks:add --index 1 heroku/nodejs --app blueprint-elli-amir
call heroku buildpacks:add --index 2 heroku/python --app blueprint-elli-amir

git push heroku main

