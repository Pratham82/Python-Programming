def area_shape(base, height, shape):
	return base * height *0.5 if shape == 'triangle' else base * height

print(area_shape(2, 3, "triangle") )