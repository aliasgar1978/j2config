"""helper functions/classes for jinja variables ( aka: filters )
"""


# import fields
from .cmn.common_fn import *
from nettoolkit import IPv4





class Vrf():
	"""device vrf/instances

	Returns:
		Vrf: Instance of VRF

	Yields:
		Vrf: Instance of VRF
	"""	

	def __init__(self, table):
		self.table = table

	def __iter__(self):
		for key, data in self.table.items():
			if self.is_vrf(data): yield data

	@staticmethod
	def is_vrf(data):
		"""condition: `filter==vrf`

		Args:
			data (DataFrame): DataFrame containing a column `filter`

		Returns:
			bool: result of condition
		"""		
		return data['filter'].lower() == 'vrf'

	def vrf_not_none(self):
		"""condition: `vrf is not None` 

		Yields:
			data_slice: data from Row that matches condition
		"""		
		for key, data in self.table.items():
			if self.is_vrf(data) and data['vrf'] != "":
				yield data

	def sorted(self):
		"""list of available vrfs sorted by `vrf` field.

		Returns:
			list: sorted vrfs
		"""		
		self.sorted_vrf = sorted([ _['vrf']  for _ in self.vrf_not_none() ])
		return  self.sorted_vrf

	def sorted_vpnids(self):
		"""list of available vpnids sorted.

		Returns:
			list: sorted vpnids
		"""		
		self.sorted_vpnids = sorted([ int(_['vrf_vpnid'])  for _ in self.vrf_not_none() ])
		return self.sorted_vpnids

	def sorted_vrf_data(self):
		"""vrf data generator, sorted by vrf names

		Yields:
			data_slice: data for all vrf rows except vrf is none, sorted by vrf names
		"""		
		for vrf in self.sorted_vrf:
			for data in self.vrf_not_none():
				if data['vrf'] == vrf: 
					yield data
					break

	def sorted_vrf_data_by_vpnid(self):
		"""vrf data generator, sorted by vpnids

		Yields:
			data_slice: data for all vrf rows except vrf is none, sorted by vpnids
		"""		
		for vpnid in self.sorted_vpnids:
			for data in self.vrf_not_none():
				if int(data['vrf_vpnid']) == vpnid: 
					yield data
					break

	def vrf_get(self, vrf):
		"""get a particular vrf data

		Args:
			vrf (str): vrf name

		Yields:
			data_slice: data for matching vrf row 
		"""		
		for data in self.vrf_not_none():
			if data['vrf'] == vrf: 
				yield data




class Vlan():
	"""device Vlan/instances
	"""	
	def __init__(self, table):
		self.table = table

	def __iter__(self):
		for key, data in self.table.items():
			if self.is_vlan(data): yield data

	@staticmethod
	def is_vlan(data):
		"""Condition: Checks if provided data is vlan data

		Args:
			data (DataFrame): Pandas DataFrame containing `filter` column

		Returns:
			bool: result of condition
		"""		
		return data['filter'].lower() == 'vlan'


	def __vlans_range(self, start, stop):
		for data in self:
			if start <= int(data['int_number']) < stop:
				yield data

	def _sorted_vl_range(self, start, stop):
		vlans = [ int(data['int_number']) for data in self if start <= int(data['int_number']) < stop ]
		return vlans	

	def vlans_sorted_range(self, start, stop):
		"""yields data slice(s) for the vlans matching for the provided range

		Args:
			start (int): starting vlan number
			stop (int): ends vlan number

		Yields:
			data_slice: of matching vlan numbers
		"""		
		for vlan in self._sorted_vl_range(start, stop):
			for data in self:
				if start <= int(data['int_number']) < stop:
					if int(data['int_number']) == vlan:
						yield data
						break

	def vlan(self, n):
		"""returns data slice for the matching vlan number

		Args:
			n (int): vlan number

		Yields:
			data_slice: of matching vlan number
		"""		
		for data in self:
			if int(data['int_number']) == n:
				yield data
				break

	def of_instance(self, vrf):
		"""yields data slice(s) for the vrf matching with `intvrf` column

		Args:
			vrf (str): vrf name

		Yields:
			data_slice: of matching vrf with `intvrf`
		"""		
		for data in self:
			if data and data['intvrf'] == vrf: yield data


class Bgp():
	"""device Bgp/instances
	"""	

	def __init__(self, table):
		self.table = table

	def __iter__(self):
		for key, data in self.table.items():
			if self.is_bgp(data): yield data

	@staticmethod
	def is_bgp(data):
		"""Condition: Checks if provided data is bgp data

		Args:
			data (DataFrame): Pandas DataFrame containing `filter` column

		Returns:
			bool: result of condition
		"""		
		return data['filter'].lower() == 'bgp'

	def vrf_not_none(self):
		"""yields data slice(s) for the bgp information where `bgp_vrf` is not none

		Yields:
			data_slice: of matching bgp details
		"""		
		for key, data in self.table.items():
			if self.is_bgp(data) and data['bgp_vrf'] != "":
				yield data

	def bgp_peers(self, vrf):
		"""yields data slice(s) for the bgp information where `bgp_vrf` matches with provided vrf name

		Args:
			vrf (str): vrf name

		Yields:
			data_slice: of matching bgp details
		"""		
		for data in self:
			if data['bgp_vrf'] == vrf:
				yield data


class Physical():
	"""device Physical/instances
	"""	
	def __init__(self, table):
		self.table = table

	@staticmethod
	def is_physical(data):
		"""Condition: Checks if provided data is Physical Interface data

		Args:
			data (DataFrame): Pandas DataFrame containing `filter` column

		Returns:
			bool: result of condition
		"""		
		return data['filter'].lower() == 'physical'

	def __iter__(self):
		for key, data in self.table.items():
			if self.is_physical(data): yield data

	def sorted(self):
		"""provides list of sorted interface numbers

		Returns:
			list: of interface numbers sorted
		"""		
		return  sorted([ int(_['int_number'])  for _ in self ])

	def uplinks(self):
		"""yields data slice(s) for the physical interface information,
		where `int_filter` information starts with uplink.

		Yields:
			data_slice: of matching physical interfaces details
		"""		
		for data in self:
			if data['int_filter'].lower().startswith('uplink'):
				yield data		

	def sorted_interfaces(self):
		"""yields data slice(s) for the sorted physical interfaces informations

		Yields:
			data_slice: sorted physical interfaces
		"""		
		for intf in self.sorted():
			for data in self:
				if int(data['int_number']) == intf:
					yield data
					break

	def interface(self, n):
		"""yields data slice(s) for the sorted physical interfaces informations

		Args:
			n (int): interface number

		Yields:
			data_slice: of matched interface
		"""		
		for data in self:
			if int(data['int_number']) == n:
				yield data
				break

	# @staticmethod     # removed since older python not support
	def interface_type(data, intf_type):
		"""condition: is provided dataslice is of given interface type

		Args:
			data (data_slice): Pandas DataFrame slice
			intf_type (str): interface type to be verify

		Returns:
			bool: result of condition
		"""		
		return data['int_filter'].lower().startswith(intf_type)

	# @staticmethod     # removed since older python not support
	def interface_type_ends(data, x):
		"""condition: is provided dataslice ends with given argument `x`

		Args:
			data (data_slice):  Pandas DataFrame slice
			x (str): interface type ending identifier to be verify with

		Returns:
			bool: result of condition
		"""		
		return data['int_filter'].lower().endswith(x)


class Aggregated():
	"""device Aggregated/instances
	"""	
	def __init__(self, table):
		self.table = table

	def __iter__(self):
		for key, data in self.table.items():
			if self.is_aggregated(data): yield data

	@staticmethod
	def is_aggregated(data):
		"""Condition: Checks if provided data is Aggregated Interface data

		Args:
			data (DataFrame): Pandas DataFrame containing `filter` column

		Returns:
			bool: result of condition
		"""			
		return data['filter'].lower() == 'aggregated'


class Loopback():
	"""device Loopback/instances
	"""	
	def __init__(self, table):
		self.table = table

	def __iter__(self):
		for key, data in self.table.items():
			if self.is_loopback(data): yield data

	@staticmethod
	def is_loopback(data):
		"""Condition: Checks if provided data is Loopback Interface data

		Args:
			data (DataFrame): Pandas DataFrame containing `filter` column

		Returns:
			bool: result of condition
		"""				
		return data['filter'].lower() == 'loopback'



def sort(obj):
	"""exectes sorted method on provided object

	Args:
		obj (dynamic): Any object object instance declaring sorted method

	Returns:
		dynamic: sorted method output from object.
	"""	
	return obj.sorted()

