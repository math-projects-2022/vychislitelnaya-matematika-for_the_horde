from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import numpy as np

def simpson(not_pars_integral, b, a, n):
	
	init_printing()
	x = Symbol('x')
	
	integral = parse_expr(not_pars_integral)
	
	width = (b-a)/n
	simpson_integral = 0
	for step in range(n):
		x1 = a + step*width
		x2 = a + (step+1)*width
		
		simpson_integral += (x2-x1)/6*(integral.subs(x,x1) + 4*integral.subs(x,(x1+x2)*0.5) + integral.subs(x,x2))
	
	f4 = prime(integral, 4)
	f = f4.subs(x,x2).evalf()
	
	R = -((b-a)/2)**5 * f / (90*n**4)
	
	it = [simpson_integral, R]
	return it
	

def prime(funk, n):
	for i in range(n):
		funk = diff(funk)
	return funk
