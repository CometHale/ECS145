from SimPy.Simulation import *
import thread
import os 
from random import gammavariate, seed
# from SimPy.SimulationTrace import *
# from SimPy.SimulationStep import *
# from SimPy.SimulationRT import *
# from SimPy.SimulationGUIDebug import *


#SimPy classes:
#Process: used  to model active components like messages, customers, etc. 

#Resource: ordinary queues

#Level: supply of quantities of material 

#Store: collections of individual items

#Monitors & Tallys: record data like queue lengths,
#delay times, and to calculate simple averages

class InventorySource(Process):

	def gen(self,alphai,betai,inventory):
		global max_time

		for i in range(max_time):
			# inventory._put()
			next_inv_arrival = gammavariate(alphai,betai)
			yield hold, self, next_create

class OrderSource(Process):
	# Randomly generates customers

	def gen(self,alphac,betac,inventory):
		global ordernum, max_time

		for i in range(max_time):
			o = Order(name = "Order#%i"%(i))
			activate(o,o.submit(inventory),at=now()) #at=now() isn't necessary; activate automatically 
			#sets at to now() if no at is provided, but this helps with readability.
			next_create = gammavariate(alphac,betac)
			yield hold, self, next_create


class Order(Process): # a customer order

	def submit(self,inventory): #submits an order to the store's order queue
		inventory._get()

	def deliver(self): #order has been served so remove one unit from inventory
		pass

def storesim(maxsimtime,alphac,betac,alphai,betai):

	# The function returns the following in a tuple:
	# 	the mean time it takes for a customer's order to be filled (0 if immediate)
	# 	the proportion of customer orders that are filled immediately
	# 	the proportion of inventory deliveries that are immediately used to fill a customer order upon arrival of the delivery
	
	#Note From Haley: Read the SimPy Getting Started and Cheatsheet
	#Otherwise none of this will make sense
	#The first bank tutorial helped a lot

	global result, max_time, ordernum, initial_cap, inventory
	
	ordernum = 0 # name of the last order created
	max_time = maxsimtime
	initial_cap = 100 # use 'unbounded' for capacity that is "infinite" (actuall sysmaxint)
	seed(99999)
	# result = tuple()

	initialize() # sets up the sim system to be ready to recieve activate calls

	inventory = Store(name="inventory",unitName="game",capacity=initial_cap) #Read through the Store class in simpy/SimPy/Lib.py
	
	inventory_source = InventorySource()
	activate(inventory_source,inventory_source.gen(alphai,betai,inventory),at=0.0)

	order_source = OrderSource()
	activate(order_source,order_source.gen(alphac,betac),at=0.0)

	simulate(until=max_time)
	
	return result