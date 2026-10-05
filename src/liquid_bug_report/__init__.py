from liquid import parse


def main():
    for expr in ["1 >= 1", "1 <= 1", "1.5 >= 1.5", '"a" >= "a"', "2 >= 1"]:
        print(expr, parse("{% if " + expr + " %}true{% else %}false{% endif %}").render())
