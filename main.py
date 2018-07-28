print "hello"
print "let's get started"
spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
if len(spy_name) > 0:
    print 'Welcome ' + spy_name + '. Glad to have you back with us.'
    spy_salutation = input("What should we call you (Mr. or Ms.)?")
    spy_name = spy_salutation + " " + spy_name
    print "Alright " + spy_name + ". I'd like to know a little bit more about..."

    spy_age = 0
    spy_rating = 0.0
    spy_is_online = True

    spy_age = input("what is your age?")

    if spy_age > 18 and spy_age < 50:
        print "valid spy"
        spy_rating = input("what is your rating ?")
        if spy_rating > 4.5:
            print 'Great ace!'
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print 'You are one of the good ones.'
        elif spy_rating >= 2.5 and spy_rating <= 3.5:
            print 'You can always do better'
        else:
            print 'We can always use somebody to help in the office.'

        spy_is_online = True

        print "Authentication complete. Welcome " + spy_name + " age: " + spy_age + " and rating of: " + spy_rating + " Proud to have you onboard"

    else:
        print "age is not valid"

else:
    print "please Enter Name "