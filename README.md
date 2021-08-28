# UAT for 3rd parties' compatibility

## Preparation

### Globally
```
brew install python
brew install pipenv
brew install node
brew install npm
```

### Solution-level Node.js
```
cd neon-uat
npm i
npm audit fix --force
```
### Solution-level Python
```
cd neon-uat
pipenv sync
```

### Network
Copy content of an envviroonment file into .env in the root of the solution
| File name     | Goal                                 |
| ------------- | ------------------------------------ |
| .env          | Test solution uses this one as input |
| .env.internal.testnet  | Our internal testnet        |
| .env.local   | Connection to a dockerizedd env       |

## Run
```
cd neon-uat
pipenv shell
pytest -rP --alluredir=allure-results
allure serve
```
