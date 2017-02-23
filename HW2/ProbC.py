from SimPy.Simulation import *
import thread
import os 
from random import gammavariate, seed, Random
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

#bakery_OO.py in SimPyModels is helpful

class G: #globals
	Rnd = Random(12345)
	TotalCustomers = 0.0 #make them floats for easier readability (no float conversions everywhere)
	TotalWaitTime = 0.0
	NumCustImmFill = 0.0 #number of customers whose orders were immediately filled
	NumInvImmFill = 0.0 #number of inventory delivs used to complete orders immediately
	NumDeliv = 0.0
	
class InventorySource(Process): #makin the goods
	def gen(self,alphai,betai,stock):
		while 1: #or now() < max_time? idk but simulation will end either way i think
			# stock._put()
			next_inv_arrival = G.Rnd.gammavariate(alphai,betai)
			yield hold, self, next_inv_arrival
			yield put, self, stock, 1 # Each delivery of new stock is a quantity of 1.
			G.NumDeliv += 1
			
class CustomerSource(Process):
	# Randomly generates customers
	def gen(self,alphac,betac,stock):
		while 1:
			yield hold, self, G.Rnd.gammavariate(alphac, betac) #block thread till time 
			c = Customer()
			activate(c,c.run(stock),at=now()) #at=now() isn't necessary; activate automatically 
			#sets at to now() if no at is provided, but this helps with readability.

class Customer(Process): # a customer order
	def run(self,stock): #submits an order to the store's order queue
			self.startWait = now() #actual time they waited (later we subtract to get actual time)
			if stock.getamount() >= 1: #number of items
				G.NumCustImmFill += 1 #if stock is available then customer doesnt wait
				yield get, self, stock, 1
			else: #stock is 0, so the newest inventory delivery is used
				G.NumInvImmFill += 1
				yield get, self, stock, 1 #request for 1 item from stock
				G.TotalWaitTime += now() - self.startWait
			G.TotalCustomers +=1 #only increment when order is complete

def storesim(maxsimtime,alphac,betac,alphai,betai):

	# The function returns the following in a tuple:
	# 	the mean time it takes for a customer's order to be filled (0 if immediate)
	# 	the proportion of customer orders that are filled immediately
	# 	the proportion of inventory deliveries that are immediately used to fill a customer order upon arrival of the delivery
	
	#Note From Haley: Read the SimPy parts of DESimIntro.pdf, it explains SimPy well

	initialize() # sets up the sim system to be ready to recieve activate calls
	
	stock= Level(initialBuffered=0) #use Level instead of Store since only one item? 


	customer_source = CustomerSource()
	activate(customer_source,customer_source.gen(alphac, betac, stock),at=0.0)

	
	inv = InventorySource()
	activate(inv,inv.gen(alphai,betai,stock),at=0.0)
	
	simulate(until=maxsimtime)
	# print "Wait Time: ", G.TotalWaitTime
	# print "Total Customers: ", G.TotalCustomers
	# print "Customers Imm: ", G.NumCustImmFill
	# print "Deliv Imm: ", G.NumInvImmFill
	# print "Total Deliveries: ", G.NumDeliv
	return (G.TotalWaitTime/G.TotalCustomers, G.NumCustImmFill/G.TotalCustomers, G.NumInvImmFill/G.NumDeliv)