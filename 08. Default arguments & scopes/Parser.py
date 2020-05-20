import argparse

if __name__ == "__main__":
    # Initialize the parser
    parser = argparse.ArgumentParser(
        description="Parser script"
    )

    # Adding parameters (positional)
    # parser.add_argument("num1", help="Number 1", type=float)
    # parser.add_argument("num2", help="Number 2", type=float)
    # parser.add_argument("operators", help="Provide operator")

    # Adding parameters (optional) (either -n or --num1 can be used as arguments)
    parser.add_argument('-n1', "--num1", help="Number 1", type=float)
    parser.add_argument('-n2', "--num2", help="Number 2", type=float)
    parser.add_argument('-o', "--operators", help="Provide operator", default="+")

    # parse the arguments
    args = parser.parse_args()
    print(args)
    result = None
    if args.operators == '+':
        result = args.num1 + args.num2
    if args.operators == '-':
        result = args.num1 - args.num2
    if args.operators == '*':
        result = args.num1 * args.num2
    if args.operators == '/':
        result = args.num1 / args.num2
    if args.operators == '%':
        result = args.num1 & args.num2

    print(result)


 # Input example
 # python Parser.py -n1=12 -n2=15 -o=*
 # python Parser.py --num1=12 --num2=15 --operators=*