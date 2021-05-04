import math


def f(x: float) -> float:
	"""Calculates the expression.
	This function is define for x >= 10
	If x type is str, then TypeError will be raised
	Else if x = 15 or x = -12, then ZeroDivisionError will be raised
	Else if x < 10, then ValueError will be raised

	:param x: the parameter of expression
	:return: the calculated value
	:raises: ZeroDivisionError, ValueError, TypeError
	"""

	return math.cos(3/45) - 16*math.pi + 55*math.e * 8 / ((x-15)*(x+12)) - 4*math.sin(x-6) + math.sqrt(x - 10)


def is_defined(x: float) -> bool:
	"""Check definition area of expression in f(x).

	:param x: the value that must be ckecked
	:return: True if function is define in x else False
	"""

	return (x >= 10) and (x != 15) and (x != math.nan) and (x != math.inf)


def calculate(inp: float):
	"""Check the definition area for f(x) and return value if is defined, else None

	:param inp: argument for f(x)
	:return: result of f(x) or None
	:rtype: float or None
	"""
	if not is_defined(inp):
		return None

	return f(inp)


def display_result(inp: float, out = None) -> None:
	"""Display the result (out) of f(x) for inp

	:param inp: argument for f(x)
	:param out: result of f(x) with definition area
	:type out: float or None
	"""

	print(f"for x = {inp:.8f}")
	if out is None:
		print(f"result = undefined")
	else:
		print(f"result = {out:.8f}")


def main():
	"""Program entry point"""

	print("This program is coded by Holovko Eugene, K-12.")
	print("This program calculates the expression depending in the param x.")

	try:
		input_data = float(input("Enter the value of param x(number with floating point): "))
	except Exception:
		print("wrong input")
		return

	print("***** do calculations ... ", end="")

	output_data = calculate(input_data)

	print("done")

	display_result(input_data, output_data)


try:
	main()
except KeyboardInterrupt:
	print("wrong input")


