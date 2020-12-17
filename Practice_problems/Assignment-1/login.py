def userLogin():
    print(
        """
          #########################################
          WELCOME TO THE DBS CONSOLE
          #########################################
          """
    )
    user_domain = input("Please enter you username: \n")
    username = user_domain.split("\\")[0]
    domain = user_domain.split("\\")[1]
    print(
        f"""
          Domain: {domain}
          Username: {username} 
          """
    )


userLogin()
