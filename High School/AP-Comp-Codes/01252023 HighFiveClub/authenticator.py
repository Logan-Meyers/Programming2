import json


accountFileName = "accounts.json"

def getAccounts():
    accountFile = open(accountFileName, "r")
    accountFileData = accountFile.read()
    accounts = json.loads(accountFileData)
    accountFile.close()
    return accounts

def writeAccounts(accountsDict):
    accountFile = open(accountFileName, "w")
    accountFile.write(json.dumps(accountsDict))
    accountFile.close()

def isAccountCreated(username=None, email=None):
    accounts = getAccounts()
    if username:
        for account in accounts:
            if account == username:
                return True
    elif email:
        for account in accounts:
            if accounts[account]["Email"] == email:
                return True
    return False

def addAccount(username, email, password, isEmployee):
    accounts = getAccounts()
    accType = 1 if isEmployee else 0
    accounts[username] = {"Username": username, "Email": email, "Password": password, "Type": accType}
    writeAccounts(accounts)

def attemptAddAccount(username, email, password, isEmployee):
    doesAccountExist = isAccountCreated(username, email)
    if doesAccountExist:
        return -1  # account exists, not possible
    else:
        addAccount(username, email, password, isEmployee)
    return 0  # success

def attemptLogin(usernameOrEmail, password):
    accounts = getAccounts()
    returnCode = -1  # 0 = user | 1 = employee | -1 = no account | -2 = wrong password
    for account in accounts:
        # check user or email 
        if (accounts[account]["Username"] == usernameOrEmail) or (accounts[account]["Email"] == usernameOrEmail):
            # check if password exists
            if (accounts[account]["Password"] == password):
                # account exists, login successful, return account type
                return accounts[account]["Type"]
            # account exists, password incorrect
            returnCode = -2
        else:
            # no account
            returnCode = -1 if returnCode != -2 else -2
    return returnCode

if __name__ == "__main__":
    addAccount("Bob", "Bob2@gmail.com", "bobobobo", False)
