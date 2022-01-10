def make_car(manufacturer, model, **kwargs):
	kwargs['manufacturer'] = manufacturer
	kwargs['model'] = model
	return kwargs

car = make_car('chevro', 'camaro', color='blue', size='medium')

print(car)