# speeding_ticket.py
# Program to calculate the cost of a speeding ticket based on
# how many miles per hour over the speed limit

def main():
    limit = eval(input('Enter the speed limit of the road you were on: '))
    speed = eval(input('Enter the speed you were going: '))

    if speed <= limit:
       print('You are in the clear')
    elif speed in range(limit,90+1):
        ticket = (speed-limit)*5 + 50
        print('You ticket cost is {0}.'.format(ticket))
    else:
        ticket = (speed-limit)*5 + 250
        print('You ticket cost is {0}.'.format(ticket))

if __name__=='__main__':
    main()
