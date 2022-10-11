import instaloader

L = instaloader.Instaloader()


# LOGIN CREDENTIALS
username = "YOURU_USERNAME"
password = r'YOUR_PASSWORD'
L.login(username, password)  # (login)


# OBTAIN PROFILE METADATA
profile = instaloader.Profile.from_username(L.context, "THE ACCOUNT YOU WISH TO GET DATA ON")


# PRINT THE LIST OF FOLLOWERS
follow_list = []
count = 0
for followee in profile.get_followers():
    follow_list.append(followee.username)
    file = open("followers.txt", "a+")
    file.write(follow_list[count])
    file.write("\n")
    file.close()
    print(follow_list[count])
    count = count + 1
    
# (likewise with profile.get_followers())
