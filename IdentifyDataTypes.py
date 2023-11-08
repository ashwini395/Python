print(type(3))
print(type("Hello World"))
print(type(False))
print(type(2.0))
print(type(
    34785344234675234567124345679871223456756234565466543534645657563444412758539467473653455452323423523534534634646))
print(type(0x80000000))
print(type(65536 * 65536))
print(type(0x7FFFFFFF + 1))

num3 = 1 + 2j
print(num3, 'is of type', type(num3))

no_of_landings = 356
no_of_takeoffs = 245
initial_no_of_flights = 100
current_no_of_flights = initial_no_of_flights + no_of_landings - no_of_takeoffs
print("Current number of flights:", current_no_of_flights)
print(type(current_no_of_flights))

